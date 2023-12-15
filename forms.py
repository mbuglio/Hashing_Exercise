from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class UserRegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=30)])
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=55)])
    email = StringField('Email', validators=[InputRequired(), Length(max=50)])

class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired(), Length(min=1, max=20)])
    password = PasswordField('Password', [InputRequired(), Length(min=6, max=55)])

class FeedbackForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    content = StringField('Content', validators=[InputRequired()])

class DeleteForm(FlaskForm):
    """left blank on purpose"""
