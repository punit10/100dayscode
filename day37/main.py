import requests
import os
from datetime import datetime
USERNAME = "punitsharma"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
user_params = {
    "token": PIXELA_TOKEN,
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
    "X-USER-TOKEN": PIXELA_TOKEN,
}

# response = requests.post(url=graph_endpoint,
#                          json=graph_config,
#                          headers=headers,
#                          verify=False
#                         )
# response.raise_for_status()
# print(response.text)
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
# today = datetime(year=2026, month=1, day=30)
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Kms did you walk today? "),
}
response = requests.post(
    url=pixel_endpoint,
    json=pixel_config,
    headers=headers,
    verify=False
)
print(response.text)

# post_multiple_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/pixels"
# post_data = [{
#     "date": datetime(year=2026, month=1, day=30).strftime("%Y%m%d"),
#     "quantity": "6.0"
# },
# {
#     "date": datetime(year=2026, month=1, day=29).strftime("%Y%m%d"),
#     "quantity": "4.0"
# },
# {
#     "date": datetime(year=2026, month=1, day=28).strftime("%Y%m%d"),
#     "quantity": "2.0"
# },
# ]
#
# post_data_config = {"-": post_data}
# response = requests.post(
#     url=post_multiple_endpoint,
#     json= post_data_config,
#     headers=headers,
#     verify=False
# )
# print(response.text)


date_to_update = datetime(year=2026, month=1, day=30).strftime("%Y%m%d")
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"
update_config = {
    "quantity": "2.0"
}
# response = requests.put(
#     url=update_endpoint,
#     json=update_config,
#     headers=headers,
#     verify=False
# )
# print(response.text)


delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"
# response = requests.delete(
#     url=delete_endpoint,
#     headers=headers,
# )
print(response.text)