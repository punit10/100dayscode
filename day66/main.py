from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_cafe = Cafe.query.all()
    return render_template("index.html", all_cafe=all_cafe)

@app.route("/random", methods=["GET"])
def get_random_cafe():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    }
    cafe_dictionary= {"cafe": cafe}
    return jsonify(cafe_dictionary)

# HTTP GET - Read Record
@app.route("/all", methods=["GET"])
def get_all_cafe():
    all_cafes = Cafe.query.all()
    dict_all_cafes = {"cafes": []}
    for cafe in all_cafes:
        new_cafe = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        dict_all_cafes["cafes"].append(new_cafe)
    return jsonify(dict_all_cafes)

# Get Via search
# /search?loc=London
@app.route("/search", methods=["GET"])
def get_cafe_by_search():
    location = request.args.get("loc")
    selected_cafes=Cafe.query.filter(Cafe.location.ilike(f"%{location}%")).all()
    cafe_dictionary = {"cafes": []}
    for cafe in selected_cafes:
        new_cafe={
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
        cafe_dictionary["cafes"].append(new_cafe)
    return jsonify(cafe_dictionary)

# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    name = request.args.get("name")
    map_url = request.args.get("map_url")
    img_url = request.args.get("img_url")
    location = request.args.get("loc")
    seats = request.args.get("seats")
    has_toilet = request.args.get("has_toilet")
    has_wifi = request.args.get("has_wifi")
    has_sockets = request.args.get("has_sockets")
    can_take_calls = request.args.get("can_take_calls")

    return f"{name} {map_url}"
    return jsonify(cafe_dictionary)

# name=angel priya cafe&map_url=google.com
# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
