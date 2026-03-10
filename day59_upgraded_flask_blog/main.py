from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def get_all_posts():
    page_title = "Do More, Be More Productive"
    return render_template("index.html", year=datetime.now().year,
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