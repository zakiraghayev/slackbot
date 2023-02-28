import os
import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Get arguments from command line
if len(sys.argv) < 3:
    print("Please provide channel name and message as arguments.")
    sys.exit(1)
channel_name = sys.argv[1]
message = sys.argv[2]

# Set up Slack client
client = WebClient(token=os.environ["SLACK_API_TOKEN"])

# Find channel ID by name
try:
    response = client.conversations_list()
    channels = response["channels"]
    channel_id = next((c["id"] for c in channels if c["name"] == channel_name), None)
    if channel_id is None:
        raise ValueError(f"No channel found with name '{channel_name}'.")
except SlackApiError as e:
    print("Error: {}".format(e))
    sys.exit(1)

# Send message to channel
try:
    response = client.chat_postMessage(channel=channel_id, text=message)
    print("Message sent: ", response["ts"])
except SlackApiError as e:
    print("Error: {}".format(e))
    sys.exit(1)
