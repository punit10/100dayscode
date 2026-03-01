from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)
year = datetime.datetime.now().year

@app.route('/')
def home():
    blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_endpoint, verify=False)
    blog_data = response.json()
    return render_template("index.html",
                           blog_data = blog_data,
                           year=year)

if __name__ == "__main__":
    app.run(debug=True)