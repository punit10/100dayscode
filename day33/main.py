import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# print(data)
# lat = data["iss_position"]["latitude"]
# long = data["iss_position"]["longitude"]
# print(lat, long)

LAT = 8.537981
LONG = -80.782127
parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
sunrise_data = response.json()
sunrise = sunrise_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sunrise_data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)
