from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")






if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)