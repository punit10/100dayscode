import requests
import os
my_lat = 8.537981
my_long = -80.782127

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API = os.environ.get("OWM_API")
print(OWM_API)

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "cnt": 4, #optional count paramater
    "appid": OWM_API
}
response = requests.get(OWM_ENDPOINT,
                        params=parameters,
                        verify=False
    )

response.raise_for_status()
weather_data = response.json()
print(weather_data)
will_rain = False
weather = ""
for hourly_data in weather_data["list"]:
    # print(hourly_data["weather"][0]["id"], hourly_data["weather"][0]["description"])
    condition_code = hourly_data["weather"][0]["id"]
    weather += f"{hourly_data["weather"][0]["main"]}: {hourly_data["weather"][0]["description"]}, "
    if int(condition_code) < 700:
        will_rain = True
print(weather)
if will_rain:
    print("Bring An umbrella!")
    # Get the logic to send the text/whatsapp message to alert