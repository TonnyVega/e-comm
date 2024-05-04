from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired,Length, Email, ValidationError, EqualTo

from models import User

# sign up
class Signup_form(FlaskForm):
  username= StringField('Username', validators=[DataRequired(), Length(min=6, max=21)])  
  email = EmailField('Email', validators=[DataRequired(), Email()])
  Password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
  confirm_password= PasswordField('Confirm_password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
    existing_user = User.query.filter_by(username= username.data).first()
    if existing_user:
      raise ValidationError(f'The username {username.data} is unavailable, please use a different name.')
  def validate_email(self, email):
    existing_email = User.query.filter_by(email= email.data).first()
    if existing_email:
      raise ValidationError(f'This email is already in use.')
      
      

class LoginForm(FlaskForm):
  username = StringField('Username', validators= [DataRequired, Length(min=4, max=20)])
  password = PasswordField('Password', validators= [DataRequired, Length(min=6)])
  SubmitField= SubmitField('Sign In')
  