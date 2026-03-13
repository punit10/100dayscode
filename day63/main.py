from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

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
bootstrap = Bootstrap5(app)
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(3, 'Harry Potter 2', 'J. K. Rowling', '9.3')")
# db.commit()

all_books = []

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

with app.app_context():
    db.create_all()

# with app.app_context():
#     new_book = Books(title="Maths", author="R. D sharma", rating=8.3)
#     db.session.add(new_book)
#     db.session.commit()

class AddBookForm(FlaskForm):
    book_title = StringField('Book', validators=[DataRequired()])
    author = StringField('Author',
                               validators=[
                                   DataRequired(),
                               ])
    rating = SelectField('Rating',
                              validators=[DataRequired()],
                              choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    submit = SubmitField('Submit')

class EditBookRatingForm(FlaskForm):
    rating = SelectField('Select New Rating',
                              validators=[DataRequired()],
                              choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    books = db.session.execute(db.select(Books).order_by(Books.id)).scalars()
    return render_template('index.html', all_books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddBookForm()
    if form.validate_on_submit():
        book_title = form.book_title.data
        author = form.author.data
        rating = form.rating.data
        #dict for all book which is not used now!
        all_books.append({
            'title': book_title,
            'author': author,
            'rating': rating
        })
        new_book = Books(
            title=book_title,
            author=author,
            rating=rating
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
# @app.route("/edit", methods=["GET", "POST"])
def edit(book_id):
    form = EditBookRatingForm()
    if form.validate_on_submit():
        #UPDATE RECORD
        print(book_id)
        book_to_update = db.get_or_404(Books, book_id)
        book_to_update.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for('home'))
    book_selected = db.get_or_404(Books, book_id)
    return render_template("edit_rating.html",
                           form=form,
                           book_selected=book_selected)

@app.route("/delete/<int:book_id>", methods=['GET', 'POST'])
def delete(book_id):
    book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

