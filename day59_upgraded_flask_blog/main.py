from flask import Flask, render_template
from datetime import datetime
import requests
app = Flask(__name__)

blog_api_endpoint = "https://api.npoint.io/01954ce68f9f44591edc"
response = requests.get(blog_api_endpoint, verify=False)
blog_data = response.json()

@app.route("/")
def get_all_posts():
    page_title = "Do More, Be More Productive"
    return render_template("index.html",
                           blog_data=blog_data,
                           year=datetime.now().year,
                           page_title=page_title)


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    requested_post = None
    page_title = "Read Post"
    for blog_post in blog_data:
        if blog_post['id'] == post_id:
            requested_post = blog_post
    return render_template("post.html",
                   post=requested_post,
                   year=datetime.now().year,
                   page_title=page_title)

@app.route("/about")
def about():
    page_title = "About Me"
    return render_template("about.html", year=datetime.now().year,
                           page_title=page_title)

@app.route("/contact")
def contact():
    page_title = "Contact"
    return render_template("contact.html", year=datetime.now().year,
                           page_title=page_title)

if __name__ == "__main__":
    app.run(debug=True)