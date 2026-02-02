import requests
import os
from datetime import datetime
USERNAME = "punitsharma"
TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# response.raise_for_status()
# print(response.text)
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Walking graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint,
#                          json=graph_config,
#                          headers=headers,
#                          verify=False
#                         )
# response.raise_for_status()
# print(response.text)
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": "20260202",
    "quantity": "4.0"
}
response = requests.post(
    url=pixel_endpoint,
    json=pixel_config,
    headers=headers,
    verify=False
)
print(response.text)