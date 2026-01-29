import requests
import os
USERNAME = "punitsharma"
TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
response.raise_for_status()
print(response.json())
print(response.text)