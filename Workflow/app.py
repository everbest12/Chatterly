from dotenv import load_dotenv
from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI
import requests
import os

# Load environment variables
load_dotenv()

# Constants from .env
PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")

# === Facebook Graph API Tools ===

def post_to_facebook(text: str):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    params = {"message": text, "access_token": ACCESS_TOKEN}
    r = requests.post(url, params=params)
    if r.status_code == 200:
        return f"✅ Post successful! ID: {r.json().get('id')}"
    else:
        return f"❌ Failed to post: {r.json()}"

def get_latest_post_id():
    url = f"https://graph.facebook.com/{PAGE_ID}/posts"
    params = {"access_token": ACCESS_TOKEN}
    r = requests.get(url, params=params)
    if r.status_code == 200 and r.json()["data"]:
        return r.json()["data"][0]["id"]
    return None

def get_comments(post_id: str):
    url = f"https://graph.facebook.com/{post_id}/comments"
    params = {"access_token": ACCESS_TOKEN}
    r = requests.get(url, params=params)
    if r.status_code == 200:
        comments = r.json().get("data", [])
        return "\n".join([f"- {c['from']['name']}: {c['message']}" for c in comments])
    return f"❌ Failed to fetch comments: {r.json()}"

def reply_to_latest_comment(reply_text: str):
    post_id = get_latest_post_id()
    if not post_id:
        return "❌ No recent posts found."
    url = f"https://graph.facebook.com/{post_id}/comments"
    params = {"access_token": ACCESS_TOKEN}
    r = requests.get(url, params=params)
    data = r.json().get("data", [])
    if not data:
        return "❌ No comments to reply to."
    latest_comment_id = data[0]["id"]
    return reply_to_comment(latest_comment_id, reply_text)

def reply_to_comment(comment_id: str, reply_text: str):
    url = f"https://graph.facebook.com/{comment_id}/comments"
    params = {"message": reply_text, "access_token": ACCESS_TOKEN}
    r = requests.post(url, params=params)
    if r.status_code == 200:
        return f"✅ Replied to comment ID: {comment_id}"
    else:
        return f"❌ Failed to reply: {r.json()}"

# === LangChain Integration ===

llm = OpenAI(temperature=0.7)

tools = [
    Tool(
        name="PostToFacebook",
        func=post_to_facebook,
        description="Use this to post content to the Facebook page. Input should be the text message."
    ),
    Tool(
        name="ReplyToLatestComment",
        func=reply_to_latest_comment,
        description="Use this to reply to the most recent comment on the latest post. Input should be the reply message."
    ),
    Tool(
        name="GetComments",
        func=lambda _: get_comments(get_latest_post_id()),
        description="Use this to get comments from the most recent Facebook post."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# === Test It ===
if __name__ == "__main__":
    print("🤖 LangChain Facebook Bot Ready!")

    # Example command
    user_input = "Post to Facebook: 🚀 WITH AI YOU CAN ACHIEVE ALOT!"
    response = agent.run(user_input)
    print("\nAgent Response:", response)
