from flask import Flask, render_template, request
import smtplib
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

@app.route("/contact", methods=('GET', 'POST'))
def contact():
    page_title = "Contact Us"
    if request.method == "POST":
        form_data = request.form
        send_email(name=form_data.get("name"),
                   email=form_data.get("email"),
                   phone=form_data.get("phone"),
                   message=form_data.get("message")
                   )
        return render_template("contact.html",
                               is_email_sent=True)
    return render_template("contact.html",
                           year=datetime.now().year,
                           is_email_sent=False,
                           page_title=page_title)

def send_email(name, email, phone, message):
    my_email = ""
    my_password = "XXXXXXXXXXXXX"
    email_body = (f"Subject:New Message - Peak Performance from {name} \n\n"
                  f"Name: {name}\n"
                  f"Email: {email}\n"
                  f"Phone: {phone}\n"
                  f"Message:{message}")
    # print(email_body)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, my_email, email_body)


if __name__ == "__main__":
    app.run(debug=True)