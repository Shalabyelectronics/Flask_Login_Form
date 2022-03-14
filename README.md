# Flask_Login_Form
This another Flask practice where we are going to learn about how to use forms-wtf , wtforms and flask-bootstrap

![ezgif com-gif-maker](https://user-images.githubusercontent.com/57592040/158195722-bb30cb85-a41d-4a42-a748-19824fa979b3.gif)
## How I go throgh this practice ?
First of all I spend some time figuring out how Flask framwork actually work?
So After setting up my Flask app by creating my app instance and all routes for each page I start working on login form 
I used flask-wtf , wtfforms and wtfforms. validators lets explain each 
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
