import requests
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into os.environ

webhook_url = os.getenv("SLACK_WEBHOOK_URL")

def send_to_slack(message: str, webhook_url: str = None):
    webhook_url = webhook_url or os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        raise ValueError("Slack webhook URL not provided.")

    payload = {
        "text": message
    }

    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        raise Exception(f"Slack notification failed: {response.text}")
