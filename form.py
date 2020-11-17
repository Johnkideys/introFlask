from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class registerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=23)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=23)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=2,max=23)])
    submit = SubmitField('Sign in')