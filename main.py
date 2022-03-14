from flask import Flask, render_template, url_for, redirect, request
from form import LoginForm
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.secret_key = os.environ.get("flask_blog_token")
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    else:
        return render_template("login.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/denied")
def denied():
    return render_template("denied.html")


@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(debug=True)
