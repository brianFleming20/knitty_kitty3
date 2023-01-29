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






if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)