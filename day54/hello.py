from flask import Flask

# Create the application instance
app = Flask(__name__)
# Define a route for the default page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()