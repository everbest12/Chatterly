from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
import requests
import os

# Load secrets
PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")

# Define tools
def post_to_facebook(text: str):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    params = {"message": text, "access_token": ACCESS_TOKEN}
    r = requests.post(url, params=params)
    return r.json()

def get_latest_post_id():
    url = f"https://graph.facebook.com/{PAGE_ID}/posts"
    params = {"access_token": ACCESS_TOKEN}
    r = requests.get(url, params=params)
    return r.json()["data"][0]["id"]

def get_comments(post_id: str):
    url = f"https://graph.facebook.com/{post_id}/comments"
    params = {"access_token": ACCESS_TOKEN}
    r = requests.get(url, params=params)
    return r.json()["data"]

def reply_to_comment(comment_id: str, reply_text: str):
    url = f"https://graph.facebook.com/{comment_id}/comments"
    params = {"message": reply_text, "access_token": ACCESS_TOKEN}
    r = requests.post(url, params=params)
    return r.json()

# LangChain LLM
llm = OpenAI(temperature=0.7)

# Define tools
tools = [
    Tool(name="PostToFacebook",
    func=post_to_facebook, 
    description="Post content to Facebook."),

    Tool(name="ReplyToComment", 
    func=reply_to_comment, 
    description="Reply to a comment on a post."),
]

# Create agent
agent = initialize_agent(
    tools,
    llm, 
    agent="zero-shot-react-description", 
    verbose=True)
