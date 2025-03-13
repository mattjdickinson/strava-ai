import os
import requests
from dotenv import load_dotenv
import anthropic

# Load API credentials from .env
load_dotenv()
STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
STRAVA_REFRESH_TOKEN = os.getenv("STRAVA_REFRESH_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

def get_access_token():
    """ Fetch a fresh access token using the refresh token. """
    url = "https://www.strava.com/oauth/token"
    data = {
        "client_id": STRAVA_CLIENT_ID,
        "client_secret": STRAVA_CLIENT_SECRET,
        "refresh_token": STRAVA_REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        token_data = response.json()
        return token_data["access_token"]
    else:
        print(f"❌ Error fetching access token: {response.json()}")
        return None

def get_recent_activities(access_token, num_activities=20):
    """ Fetch the last 'num_activities' from Strava. """
    url = f"https://www.strava.com/api/v3/athlete/activities?per_page={num_activities}"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Error fetching activities: {response.json()}")
        return None

def get_laps_for_activity(access_token, activity_id):
    """ Fetches lap data for a given activity. """
    url = f"https://www.strava.com/api/v3/activities/{activity_id}/laps"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Error fetching laps for activity {activity_id}: {response.json()}")
        return []

def generate_workout_name(activity, laps):
    """ Uses Claude AI to generate a workout name based on activity and lap data. """
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # Format lap details for AI
    lap_details = "\n".join([
        f"- Lap {i+1}: {lap['distance']/1000:.2f} km @ {lap['elapsed_time']/lap['distance']:.2f} sec/m" 
        for i, lap in enumerate(laps)
    ])

    prompt = f"""
    Generate an appropriate Strava workout title based on this workout:

    - Name: {activity['name']}
    - Distance: {activity['distance']/1000:.2f} km
    - Moving Time: {activity['moving_time'] // 60} min
    - Elapsed Time: {activity['elapsed_time'] // 60} min
    - Average Pace: {activity['average_speed']:.2f} m/s
    - Max Speed: {activity['max_speed']:.2f} m/s
    - Type: {activity['type']}
    - Workout Type: {activity.get('workout_type', 'Unknown')}
    - Lap Splits:
    {lap_details}

    Provide a short, natural workout name that best describes the session.
    """

    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=50,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # ✅ Extract text correctly from Claude's response
    ai_response = response.content[0].text if isinstance(response.content, list) else response.content.text
    return ai_response.strip()


if __name__ == "__main__":
    access_token = get_access_token()
    
    if access_token:
        activities = get_recent_activities(access_token)

        if activities:
            print("\n📋 **Workout Activities Before & After AI Naming:**\n")
            for activity in activities:
                if activity['type'] == "Run" and activity.get('workout_type') == 3:  # 3 = 'Workout' in Strava
                    old_name = activity["name"]
                    
                    # Fetch lap data
                    laps = get_laps_for_activity(access_token, activity["id"])

                    if laps:
                        new_name = generate_workout_name(activity, laps)
                        print(f"🏃 **Before:** {old_name}")
                        print(f"🤖 **After:** {new_name}\n")
                    else:
                        print(f"⚠️ Skipping {old_name} (no lap data).")
