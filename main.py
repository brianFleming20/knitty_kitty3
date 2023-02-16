from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField, widgets, SelectMultipleField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
# from forms import CreatePostForm


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knitty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




# class KnittyItem(db.Model):
#     __tablename__ = "kitty_posts"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     subtitle = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)


# class User(UserMixin, db.Model):
#     __tablename__ = "Users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False)
#     password = db.Column(db.String(250), nullable=False)
#     email = db.Column(db.String(250), unique=True, nullable=False)
# db.create_all()


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class Order(FlaskForm):
    string_of_files = ["I am not robot"]
    files = [(x, x) for x in string_of_files]
    example = MultiCheckboxField(' ', choices=files)
    name = StringField('Name', validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    request = CKEditorField("Request", validators=[DataRequired()])
    submit = SubmitField("Send")


@app.route("/")
def home():
    x = datetime.now()

    date = x.strftime("%A %d %B %Y")
    form = Order()
    return render_template("index.html", date=date, form=form)


@app.route("/ordering")
def ordering():
    x = datetime.now()
    date = x.strftime("%A %d %B %Y")
    return render_template("ordering.html", date=date)


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
