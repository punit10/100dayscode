from flask import Flask

# Create the application instance
app = Flask(__name__)
class User():
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
        return wrapper

def make_bold(function):
    def bold(*args, **kwargs):
        return f"<b>{function(*args, **kwargs)}</b>"
    return bold

def make_underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function(*args, **kwargs)}</u>"
    return wrapper

def make_italic(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function(*args, **kwargs)}</u>"
    return wrapper()

# Define a route for the default page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/greet")
@make_bold
@make_underline
def greeting():
    return "Welcome!"

@app.route("/user/<name>")
@is_authenticated_decorator
@make_underline
def greet(name):
    return f"Hello, {name}!"

@app.route("/user/<name>/<int:age>")
def user(name, age):
    return f"Hello, {name}! You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True)