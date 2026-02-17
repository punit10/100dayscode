import requests
import os

EXERCISE_APP_ID = os.environ.get("EXERCISE_APP_ID")
EXERCISE_API_KEY = os.environ.get("EXERCISE_API_KEY")
AGE = 30
GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 167
headers = {
    "x-app-id": EXERCISE_APP_ID,
    "x-app-key": EXERCISE_API_KEY
}
query = {
    "query": input("What exercise you have done today? "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
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
