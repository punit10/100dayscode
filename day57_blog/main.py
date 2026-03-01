from flask import Flask, render_template
import requests
import datetime
import post

app = Flask(__name__)
year = datetime.datetime.now().year
blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_endpoint, verify=False)
blog_data = response.json()

@app.route('/')
def home():
    return render_template("index.html",
                           blog_data = blog_data,
                           year=year)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    return render_template("post.html",
                           blog_data = blog_data,
                           year=year,
                           post_id=post_id)
if __name__ == "__main__":
    app.run(debug=True)