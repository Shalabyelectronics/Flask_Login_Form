# Flask_Login_Form
This another Flask practice where we are going to learn about how to use forms-wtf , wtforms and flask-bootstrap

![ezgif com-gif-maker](https://user-images.githubusercontent.com/57592040/158195722-bb30cb85-a41d-4a42-a748-19824fa979b3.gif)
## How I go throgh this practice ?
First of all I spend some time figuring out how Flask framwork actually work?
So After setting up my Flask app by creating my app instance and all routes for each page I start working on login form 
I used flask-wtf , wtfforms and validators lets explain each 
### Flask_wtf ?
WTF stands for WT Forms which is intended to provide the interactive user interface for the user. The WTF is a built-in module of the flask which provides an alternative way of designing forms in the flask web applications.
and you can read more about it from [here](https://www.javatpoint.com/flask-wtf).
and this is the class I created for a login form:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import Length, Email, DataRequired


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(),Email(), Length(min=8, max=30)])
    password = PasswordField(label="Password", validators=[DataRequired(),Length(min=8, max=30)])
    submit = SubmitField(label="Log in")
```
### After creating the login class?
We need now to create our login form from the class that we created so the first step is to edite our html page by using flask-bootstrap to save our time so first we will install it from ```pip install Flask-Bootstrap```
After that we need to add bootstrap to our flask app like this 
```Bootstrap(app)```
Then we go back to our login page to add bootstrap blocks like this:
```html
{% extends "bootstrap/base.html" %}
{% block title %}
Log In
{% endblock %}
	{% block content %}
        <div class="container">
		<h1>Login</h1>
			<form method="post" action="{{ url_for('login') }}" novalidate>
				{{ form.csrf_token }}
				<p>
					{{ form.email.label }}
					<br>
					{{ form.email }}
					{% for err in form.email.errors %}
					<span style="color:red;"> {{ err }}</span>
					{% endfor %}
				</p>
				<p>
					{{ form.password.label }}
					<br>
					{{ form.password }}
					{% for err in form.password.errors %}
					<span style="color:red;"> {{ err }}</span>
					{% endfor %}
				</p>
					{{ form.submit }}
			</form>

        </div>
{% endblock %}
```
For more info about Flask-Bootstrap [here!](https://pythonhosted.org/Flask-Bootstrap/)
Also you can watch this video to understand more about it [here](https://www.youtube.com/watch?v=PE9ZGniSDW8) and [here](https://www.youtube.com/watch?v=S7ZLiUabaEo)
### secure your form !!!
Here we are going to discuss why you need to secure your form ??
and the answer is from bad hackers who can steel it from Cross-site request forgery (CSRF) and to know more about it [here](https://portswigger.net/web-security/csrf)
So we need to create a secret key first then assign it to our app config file like this 
```python
app.config["SECRET_KEY"] = TOKEN
# OR 
app.secret_key = "some secret string"
```
And you need to generate the token as well you have two way to do so 

First by using secrets module and using `token_hex(bytes)`

Second by using os module and using `urandom(bytes).hex()`
Then we need to go back to our form and under form tag directly we need to add 
`{{ form.csrf_token }}` to activate the secure mode and we used csrf_token because we have only one hidden field and it is a password so if I have more than one hidden field I can use `{{ form.hidden_tag() }}`
### Creating our login route method.
We are almost done the final part is a little bit trick where we are going to add some logic to our login route like this 
```python
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
```
I will explain this logic now first I add ` methods=["GET", "POST"]` to let our method to get or post request data after we submit the form and to check that as well we need to import request from flask.
So I will check first if the user already post the data by submit it if yes will check if the form is valid and there are no errors if yes we will check if the user email and password are matched So if yes we will redirect the user to the success page else we will redirect the user to denied page.
## The End :)
