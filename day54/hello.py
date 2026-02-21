from flask import Flask

# Create the application instance
app = Flask(__name__)
# Define a route for the default page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/greet")
def greeting():
    return "Welcome!"

@app.route("/user/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/user/<name>/<int:age>")
def user(name, age):
    return f"Hello, {name}! You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True)