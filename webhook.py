import requests, sys, json, os
from dotenv import load_dotenv

# Get arguments from command line
if len(sys.argv) < 2:
    print("Please provide message as arguments.")
    sys.exit(1)
message = sys.argv[1]

# Define the message payload
payload = {"text": f"{message}"}


# Load environment variables from .env file
load_dotenv()

# Define the webhook URL
url = os.getenv('SLACK_WEBHOOK_URL')

# Send the request
response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

# Check if the request was successful
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Error sending message: {response.text}")
