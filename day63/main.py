from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask import Markup

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

all_books = []
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


@app.route('/')
def home():
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddBookForm()
    if form.validate_on_submit():
        book_title = form.book_title.data
        author = form.author.data
        rating = form.rating.data
        all_books.append({
            'title': book_title,
            'author': author,
            'rating': rating
        })
        return render_template('index.html', all_books=all_books)
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

