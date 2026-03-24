from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'
Bootstrap5(app)

# CREATE DB
all_movies = []

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-movies-collection.db"
# initialize the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    year: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[float] = mapped_column(String(250), nullable=True)
    img_url: Mapped[float] = mapped_column(String(250), nullable=False)


    def __init__(self,
                 title,
                 year,
                 description,
                 rating,
                 ranking,
                 review,
                 img_url
                 ):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url

with app.app_context():
    db.create_all()

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

class AddMovieForm(FlaskForm):
    title = StringField('Title',
                        validators=[InputRequired()])
    year = StringField('Year',
                       validators=[InputRequired()])
    description = TextAreaField('Description',
                              validators=[InputRequired(),
                                          Length(min=4, max=1000)])
    rating = FloatField('Rating',
                        validators=[InputRequired()])
    ranking =FloatField('Ranking',
                        validators=[InputRequired()])
    review = StringField('Review')
    img_url = StringField('Image URL',
                          validators=[InputRequired()])
    submit = SubmitField('Add Movie')

class EditMovieRatingForm(FlaskForm):
    rating = FloatField('Rating',
                        validators=[InputRequired()])
    review = StringField('Review',
                         validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.id)).scalars()
    return render_template("index.html", all_movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        new_movie_details = Movie(
            title=form.title.data,
            year=form.year.data,
            description=form.description.data,
            rating=form.rating.data,
            ranking=form.ranking.data,
            review=form.review.data,
            img_url=form.img_url.data,
        )
        db.session.add(new_movie_details)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditMovieRatingForm()
    selected_movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data
        # get movie obj and update it with new fields
        selected_movie.rating = float(rating)
        selected_movie.review = review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",
                           form=form,
                           selected_movie=selected_movie)

@app.route("/delete/<int:movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    selected_movie = db.get_or_404(Movie, movie_id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
