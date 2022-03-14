from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import Length, Email, DataRequired


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(),Email(), Length(min=8, max=30)])
    password = PasswordField(label="Password", validators=[DataRequired(),Length(min=8, max=30)])
    submit = SubmitField(label="Log in")

