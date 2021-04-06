#forms.py說明：建立Form_設置使用者註冊所需要的表單

import wtforms
from flask_wtf import FlaskForm
#from flask_wtf import Form,RecaptchaField,LoginForm

from wtforms.fields import *
from wtforms import widgets, Form as _Form
#from captcha.fields import ReCaptchaField

from wtforms import StringField, SubmitField, validators, PasswordField ,BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo#,Phone
#from app.models import User
from models import User
from app import app

class RegisterForm(FlaskForm):
    #檢核功能尚未正常發揮20210206
    #validators.username()
    username = StringField('UserName', validators=[DataRequired(),Length(min=6,max=20)])
       
    email = StringField('email', validators=[DataRequired()])    
    
    password = PasswordField('PassWord', validators=[DataRequired(),Length(min=8,max=20)])
        
    Confirm = PasswordField('Confirm PassWord', validators=[DataRequired(),EqualTo('password')])
    #class FormWithCaptcha(form.Form):
    recaptcha = RecaptchaField()

    validate_on_Submit = SubmitField('Register New Account')


class LoginForm(FlaskForm):
    #檢核功能尚未正常發揮20210206
    #validators.username()
    username = StringField('UserName', validators=[DataRequired(),Length(min=6,max=20)])
       
    password = PasswordField('PassWord', validators=[DataRequired(),Length(min=8,max=20)])
        
    remember = BooleanField('Remember')

    validate_on_Submit = SubmitField('sign in')




    