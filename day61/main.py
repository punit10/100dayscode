from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

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

class LoginForm(FlaskForm):
    email = StringField(label='Email')
    # For best practice "label" property argument can be specified, without it also work
    #email = StringField('Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Login')

app.secret_key = "some-secret-key"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
