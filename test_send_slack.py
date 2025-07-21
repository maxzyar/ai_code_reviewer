import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the Slack webhook URL
slack_url = os.getenv("SLACK_WEBHOOK_URL")

# Message payload
payload = {
    "text": "✅ *Slack integration test successful!* This message confirms your webhook is working."
}

# Send POST request
response = requests.post(slack_url, json=payload)

# Check response
if response.status_code == 200:
    print("Slack message sent successfully ✅")
else:
    print(f"Failed to send message ❌ Status: {response.status_code}, Response: {response.text}")
