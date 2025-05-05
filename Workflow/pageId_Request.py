import requests

# Replace this with your actual User Access Token (from Graph API Explorer)
USER_ACCESS_TOKEN="EAA52VSuca7QBOwkvQIDYFdQUh62SUZAxJAY5YYhzUTfHSOEgUGhEeZBI5o9u4s0ZBMjhYWIgw0stoLaB00JFj9ZAkrJmsWa3ZBvI81E4ZCvv86n0T9G0qZCyJHQEtJGvt17PGxKazK0xJMzG5dbDgwju4rEuXTE1kwdGFfSNxfmyN6cZAn8vY7ZCiTgglREDEkJJLGZCN3X1LnoCFX7OZBeEuZBdZAhgZCNeZBsEHEZD"

def get_pages(token):
    url = "https://graph.facebook.com/v22.0/me/accounts"
    params = {
        "access_token": token
    }

    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print("Error:", response.status_code)
        print("Details:", response.json())
        return
    
    data = response.json()
    
    if "data" not in data or len(data["data"]) == 0:
        print("❌ No pages found. Make sure your token has the right permissions.")
        return

    print("\n✅ Pages Found:")
    for page in data["data"]:
        print(f"Page Name      : {page['name']}")
        print(f"Page ID        : {page['id']}")
        print(f"Page Token     : {page['access_token']}")
        print("-" * 40)

get_pages(USER_ACCESS_TOKEN)
