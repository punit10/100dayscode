from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=year)


if __name__ == "__main__":
    app.run(debug=True)