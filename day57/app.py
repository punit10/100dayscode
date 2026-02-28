from enum import verify

from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
year = datetime.datetime.now().year

@app.route("/")
def index():
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, year=year)

@app.route("/guess/<name>")
def guess(name):
    agify_endpoint = "https://api.agify.io"
    agify_params = {"name": name}
    response = requests.get(agify_endpoint, params=agify_params, verify=False)
    response_json = response.json()
    guessed_age = response_json["age"]

    genderize_endpoint = "https://api.genderize.io"
    genderize_params = {"name": name, "country_id": "IN"}
    response = requests.get(genderize_endpoint, params=genderize_params, verify=False)
    guessed_gender = response.json()["gender"]

    return render_template("guess.html",
                           name=name,
                           guessed_age = guessed_age,
                           guessed_gender = guessed_gender,
                           year=year)

if __name__ == "__main__":
    app.run(debug=True)