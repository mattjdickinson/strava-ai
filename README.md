# 🏃‍♂️ Strava AI - Automated Workout Naming & Analysis  
Automatically renames Strava workout sessions using AI based on **lap data, pacing insights, and past session comparisons**.  

---

## **🚀 Features**
👉 Fetches the last **20 activities** from your Strava account  
👉 Filters workouts where `Type = Run` and `Workout Type = Workout`  
👉 Retrieves **lap data** (manual splits from watch)  
👉 Uses **Claude AI** to generate intelligent workout names  
👉 Prints **before & after names** for review  
🚀 (Upcoming) **Adds detailed analysis to descriptions**  
   - **Fastest pace recorded**  
   - **Average pace of reps**  
   - **Comparison with past sessions**  

---

## **📀 1. Prerequisites**
Before using this project, ensure you have:
- Python **3.8+** installed.
- A **Strava API Client ID, Client Secret, and Refresh Token** ([Get one here](https://developers.strava.com/)).
- An **Anthropic API Key** ([Sign up here](https://www.anthropic.com/)).
- GitHub account (for cloning the repo).

---

## **📚 2. Installation**
### **Clone the Repository**
Run the following command in your terminal:
```sh
git clone https://github.com/YOUR_USERNAME/strava-ai.git
cd strava-ai
```

### **Create a Virtual Environment**
To keep dependencies isolated, create a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **Install Dependencies**
Once inside the virtual environment, install all required dependencies:
```sh
pip install -r requirements.txt
```

---

## **🔐 3. Setting Up API Keys**
### **🔒 Step 1: Get Strava API Credentials**
To connect to the Strava API, you need to generate credentials:  
1. Go to [Strava Developers](https://www.strava.com/settings/api).
2. Click **"Create & Manage Your App"**.
3. Fill in the details:
   - **Application Name**: `Strava AI`
   - **Website**: `https://your-website.com` (or `http://localhost` for testing)
   - **Authorization Callback Domain**: `http://localhost`
   - **App Type**: Personal
4. Click **Save**.
5. Copy your **Client ID** and **Client Secret**.

---

### **🔑 Step 2: Get Your Strava Refresh Token**
After creating the Strava app:
1. Open this URL (replace `YOUR_CLIENT_ID`):
   ```
   https://www.strava.com/oauth/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=http://localhost&scope=activity:read_all
   ```
2. Click **Authorize** and Strava will redirect you to `http://localhost?code=YOUR_AUTH_CODE`.
3. Copy the `code` from the URL.
4. Exchange it for an **access token and refresh token** by running:
   ```sh
   curl -X POST https://www.strava.com/oauth/token \
   -d client_id=YOUR_CLIENT_ID \
   -d client_secret=YOUR_CLIENT_SECRET \
   -d code=YOUR_AUTH_CODE \
   -d grant_type=authorization_code
   ```
5. Strava will return an access token **and refresh token**.
6. Copy the **refresh token**—you’ll need it in the next step.

---

### **🤖 Step 3: Get an Anthropic API Key**
To use **Claude AI**, you need an **Anthropic API Key**:
1. Sign up at [Anthropic](https://www.anthropic.com/).
2. Go to **API Dashboard** and click **Generate API Key**.
3. Copy your **Anthropic API Key**.

---

### **🔧 Step 4: Create a `.env` File**
1. Create a `.env` file in the root directory:
   ```sh
   touch .env
   ```
2. Open `.env` and add:
   ```ini
   STRAVA_CLIENT_ID=your_client_id
   STRAVA_CLIENT_SECRET=your_client_secret
   STRAVA_REFRESH_TOKEN=your_refresh_token
   ANTHROPIC_API_KEY=your_anthropic_key
   ```
3. **Do not share this file**—add `.env` to `.gitignore`:
   ```
   .env
   ```

---

## **💡 4. Running the AI-Powered Workout Naming**
Once authentication is set up, run:
```sh
python main.py
```
This will:
1. Fetch your **last 20 Strava activities**.
2. **Filter workouts** (Type = Run, Workout Type = Workout).
3. Fetch **lap data** for structured workouts.
4. Use **Claude AI** to generate a workout name.
5. Print the **before & after names**.

---

## **📝 5. Example Output**
```sh
💼 **Workout Activities Before & After AI Naming:**

🏃 **Before:** Tuesday Track Session  
🤖 **After:** 10 × 400m (90s static recovery)  

🏃 **Before:** Evening Hill Sprints  
🤖 **After:** 8 × 200m Hills (~2 min recovery)  

🏃 **Before:** Long Run with Intervals  
🤖 **After:** 3 × 3km @ Threshold (90s jog)  
```

---

## **🚀 6. Upcoming Features**
🚀 **Automatically update Strava workout titles** with AI-generated names.  
🚀 **Set up a webhook (`webhook.py`)** to rename workouts automatically after upload.  
🚀 **Enhance workout analysis** in the **description**:  
   - **Fastest pace recorded**  
   - **Average pace of reps**  
   - **Comparison with past sessions**  

---

## **📝 7. Committing Your Changes**
After updating the `.env` file and testing the script, commit your code:
```sh
git add .
git commit -m "Added AI-powered workout naming"
git push origin main
```

---

## **💪 8. Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Submit a **pull request**.

---

## **🌟 9. License**
This project is open-source under the **MIT License**.

---

