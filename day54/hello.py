from flask import Flask

# Create the application instance
app = Flask(__name__)

def make_bold(function):
    def bold(*args, **kwargs):
        return f"<b>{function(*args, **kwargs)}</b>"
    return bold

def make_underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function(*args, **kwargs)}</u>"
    return wrapper

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
@make_underline
def greet(name):
    return f"Hello, {name}!"

@app.route("/user/<name>/<int:age>")
def user(name, age):
    return f"Hello, {name}! You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True)