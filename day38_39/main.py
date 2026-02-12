from enum import verify

import requests

headers = {
    "x-app-id": "app_edbed308d1914248b5e01566",
    "x-app-key": "nix_live_YDZ3WSmPfaHNLVw5dvJQ0Xf9fytyHC7D"
}
query = {
    "query": input("What exercise you have done today? "),
    "weight_kg": 70,
    "height_cm": 175,
    "age": 30,
    "gender": "male"
}

BASE_ENDPOINT = "https://app.100daysofpython.dev"
exercise_endpoint = f"{BASE_ENDPOINT}/v1/nutrition/natural/exercise"
response = requests.post(exercise_endpoint,
                         json=query,
                         headers=headers,
                         verify=False
)
response.raise_for_status()
print(response.json()["exercises"][0])
