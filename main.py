import requests
import os
from dotenv import load_dotenv

load_dotenv()
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

# Post message on Discord
requests.post(
    webhook_url,
    json={"content": "It's 11:11, make a wish!"}
)
print("Successfully posted to discord")

