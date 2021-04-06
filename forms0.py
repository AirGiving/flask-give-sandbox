#forms.py說明：建立Form_設置使用者註冊所需要的表單
from flask_wtf import FlaskForm
from flask_wtf import Form

from wtforms.fields import *
from wtforms import widgets, Form as _Form


from wtforms import StringField, SubmitField, validators, PasswordField #,PhoneField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo#,Phone
class RegisterForm(FlaskForm):
    #依照Model來建置相對應的Form
    
    #password2: 用來確認兩次的密碼輸入相同
    #
    #validators.username()
    username = StringField('UserName', validators=[DataRequired(),Length(min=6,max=20)])
       
    email = StringField('email', validators=[DataRequired()])    
    
    password = PasswordField('PassWord', validators=[DataRequired(),Length(min=8,max=20)])
        
    Confirm = PasswordField('Confirm PassWord', validators=[DataRequired(),EqualTo('password')])
    
    validate_on_Submit = SubmitField('Register New Account')


    class RegisterForm_R(FlaskForm):
    #"""依照Model來建置相對應的Form
    
    #password2: 用來確認兩次的密碼輸入相同
    #"""
    	username = StringField('UserName', validators=[
        validators.DataRequired(),
        validators.Length(10, 30)
        #validators.username()
    	])
    	email = EmailField('Email', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    	])
    #phone = PhoneField('Phone', validators=[
        #validators.DataRequired(),
        #validators.Length(1, 20),
        #validators.Phone()
    #])
    	password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    	])
    	password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    	])
    validate_on_Submit = SubmitField('Register New Account')
