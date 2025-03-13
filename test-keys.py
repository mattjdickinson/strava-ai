import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve API keys
STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Print for verification
print(f"STRAVA_CLIENT_ID: {STRAVA_CLIENT_ID}")
print(f"STRAVA_CLIENT_SECRET: {STRAVA_CLIENT_SECRET[:5]}... (hidden)")
print(f"ANTHROPIC_API_KEY: {ANTHROPIC_API_KEY[:5]}... (hidden)")

# Check if any keys are missing
if not STRAVA_CLIENT_ID or not STRAVA_CLIENT_SECRET or not ANTHROPIC_API_KEY:
    print("⚠️ ERROR: One or more API keys are missing. Check your .env file.")
