import os
import requests
from dotenv import load_dotenv

# Load Facebook credentials
load_dotenv()
access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
page_id = os.getenv("FACEBOOK_PAGE_ID")

def post_to_facebook(message):
    if not access_token or not page_id:
        raise ValueError("Missing Facebook credentials in .env")

    url = f"https://graph.facebook.com/{page_id}/feed"
    payload = {
        "message": message,
        "access_token": access_token
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Post published to Facebook successfully!")
    else:
        print("Failed to post to Facebook.")
        print("Status:", response.status_code)
        print("Response:", response.json())
