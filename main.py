from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    x = datetime.now()

    date = x.strftime("%A %d %B %Y")
    return render_template("index.html", date=date)


@app.route("/ordering")
def ordering():
    return render_template("ordering.html")


@app.route("/about")
def about():
    return render_template("elements.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
