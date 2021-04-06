# -*- coding: utf-8 -*-
#tp3 python tp3.py
#https://pythonhosted.org/Flask-Bootstrap/
#創於2021/01/25衍生自tp/python mangetp.py
import os,requests


from flask import Flask, g
from flask import request,session
from flask import render_template,flash,redirect,url_for,request
from wtforms import form
from flask_bootstrap import Bootstrap
from config import Config
#import forms
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired



#from forms import LoginForm
import sqlite3
#from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapper

#from flask.ext.sqlalchemy import SQLAlchemy
#from flask_wtf import LoginForm
#from LoginForm import *
from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField,BooleanField,SubmitField #,RecaptchaField

#from flask_wtf import CSRFProtect


from markupsafe import escape#為測試userID而導入
from datetime import datetime
from flask_bcrypt import Bcrypt
#需要先安裝pip install flask-bcrypt
#from wtforms import RegisterForm,LoginForm
#from form import RegisterForm,LoginForm
from flask_login import LoginManager,login_user,current_user,login_required
from flask_login import UserMixin
#from models import User
#from app import app
app = Flask(__name__)
bootstrap=Bootstrap(app)

#db = sqlite3.connect('give02db.db')
#db = SQLALCHEMY_DATABASE_URL=os.environ.get('give02db.db')
#app.config['SQLALCHEMY_DATABASES_URI'] ='sqlite:///giveo2db.db'
SQLALCHEMY_DATABASE_URL='sqlite:///giveo2db.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
#SECRET_KEY ='6b90c3136c634fddb597289d392571e6'

#若用有app.config的會報錯找不到users table
#app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///giveo2db.db'
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#app.config["SECRET_KEY"] = '6b90c3136c634fddb597289d392571e6'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
#app.config.from_object(Config)
#app.config.from_object(‘config‘)
#app.config.from_object(config)
login = LoginManager(app)
login.login_view = 'login'
login.login_message ='you must login to access this page'
login.login_message_category ='info'

#from models import User
from app import app
#from forms import LoginForm
#from app.routes import *
#from app.forms import RegisterForm,LoginForm
#from app.models import User
#from app import db,login

class Users(db.Model,UserMixin):
#class User(UserMixin):
	__tablename__ = "users"
	
	#class User(db.Model,UserMixin):
	number = db.Column(db.Integer,Primary_Key=True)
	__mapper_args__ = {
         'primary_key':[number]
     }
	username = db.Column(db.String(20),unique=True,nullable = False)
	phone = db.Column(db.String(20),nullable = False)
	password = db.Column(db.String(20),nullable = False)
	email = db.Column(db.String(120),unique=True,nullable = False)
	def __repr__(self):
		return '<Users % r >' % self.username



class RegisterForm(FlaskForm):
    #檢核功能尚未正常發揮20210206
    #validators.username()
    username = StringField('UserName', validators=[DataRequired()])
       
    email = StringField('email', validators=[DataRequired()])    
    
    password = PasswordField('PassWord', validators=[DataRequired()])
        
    Confirm = PasswordField('Confirm PassWord', validators=[DataRequired()])
    #class FormWithCaptcha(form.Form):
    #recaptcha = RecaptchaField()

    validate_on_Submit = SubmitField('Register New Account')








class LoginForm(FlaskForm):
    #檢核功能尚未正常發揮20210206
    #validators.username()
    username = StringField('UserName', validators=[DataRequired()])
       
    password = PasswordField('PassWord', validators=[DataRequired()])
        
    remember = BooleanField('Remember')

    validate_on_Submit = SubmitField('sign in')








#app = Flask(__name__)
# @app.route('/')
# def hello_world():
     # return "Hello World!2021/01/25"
@app.route('/')#裝飾器告訴你怎樣的url可以call怎樣的function
def index():#這是一個function的名稱 上方的裝飾器會call他
     #return 'Index Page'
     
     return render_template('index.html')

#引導到註冊頁面
@app.route('/registercarvin',methods=["POST","GET"])
def registercarvin():
    return render_template('registercarvin.html')


@app.route('/register',methods=["POST","GET"])
def register():#20210205新增正測試中
	#db = sqlite3.connect('give02db.db')
	#if current_user.is_authenticated:
		#return redirect(url_for('index')) 
	form = RegisterForm()
	#validators=[DataRequired()]
	#password = form.password.data
	#password = {}
	if form.validate_on_Submit():
		username = form.username.data
		email = form.email.data
		#password = form.password.data

		password = (bcrypt.generate_password_hash(form.password.data)) 
		#ValueError: Password must be non-empty.尚待克服20210206
		#print(username,email,password)
		#以下處理寫入的工作

		#def writeuserindb():#寫入users  基本資料
		#db = sqlite3.connect('give02db.db') 
				#if request.method =="POST":
		#username = request.form["username"]
		#email = request.form["email"] 
		phone = "none phone"
		date = datetime.now()#抓取系統時間要先導入from datetime import datetime
		#password = request.form["password"]
		#print(username,email,phone,date,password)
		#db = sqlite3.connect('give02db.db') 
		with db:#一定要用with db要不然無法寫入資料庫
			curs = db.cursor()
			#data = cursor.fetchone()#沒作用但暫不刪
			ins = 'INSERT INTO users(username,email,phone,date,password) VALUES(?,?,?,?,?)'
			#ins = 'INSERT INTO users(username,email,phone,date,password) VALUES(www,we@gmail.com,0932345565,20210206)'
			curs.execute(ins,(username,email,phone,date,password))
			#db.session.commit()
			#curs.commit()
			print(username,email,phone,date,password)
			#db.close() 
			#return #"完成輸入"
			#return render_template("login.html")
			#return render_template('register.html', form = form)
			#return render_template('register.html')
		return render_template('register.html', form = form)
	else:
		return redirect(url_for("register.html"))

@app.route('/login',methods=["POST","GET"])
def login():
	#SECRET_KEY ='6b90c3136c634fddb597289d392571e6'
	db = sqlite3.connect('give02db.db')
	
	form = LoginForm()
	if form.validate_on_Submit():
	#if form.Submit():
		username = form.username.data
		password = form.password.data
		remember = form.remember.data
		#check if password is match
		#User = ()
		user = Users.query.filter_by(username=username).first()
		if user and bcrypt.check_password_hash(user.password,password):
		#user exists and password matched
			login_user(user,remember=remember)
			flash('login success',category='info')
			if request.args.get('next'):
				next_page = request.args.get('next')
					#return redirect(url_for(next_page))
			return redirect(next_page)
		return redirect(url_for('index'))
		#flash('user not exists or password not match', category='danger')
	return render_template('login.html',form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('iogin'))


@app.route('/things',methods=["POST","GET"])
def things():
    return render_template('things_form.html')
    #return "分享物品資料登錄頁面(施工中)"

@app.route('/thingsplay',methods=["POST","GET"])
def thingsplay():
    return render_template('thingsplay_form.html')
    #return "分享物品目錄瀏覽頁面'thingsplay_form.html'(施工中)"
@app.route('/show_one',methods=["POST","GET"])
#('/show_one',methods=["POST","GET"])
#def show_one(request):還沒成功20210129
#讀取一筆資料：cname =張三
    #try:
        # item = student.objects.get(cname='張三')
        # except Exception as e:
        # errormsg = '讀取資料出現錯誤：' + e
        # return render(request,'show_one.html',locals())




@app.route('/iwantdb',methods=["POST","GET"])
def iwantdb():
    return render_template('iwant_form.html')

#writeindb將users資料寫入資料庫
@app.route('/writeindb',methods=["POST","GET"])
def writeindb():#寫入users  基本資料
   db = sqlite3.connect('give02db.db') 
      #number = None #因為是由系統自動產生
      #取得頁面上input輸入欄位裡面輸入的欄位資料:
   if request.method =="POST":
        username = request.form["username"]
        email = request.form["email"] 
        phone = request.form["phone"]
        date = datetime.now()#抓取系統時間要先導入from datetime import datetime
        #password = request.form["password"]
        password = (bcrypt.generate_password_hash(request.form["password"])) 
        with db:
            #db.executemany#沒作用但暫不刪
            curs = db.cursor()
            #data = cursor.fetchone()#沒作用但暫不刪
            ins = 'INSERT INTO users(username,email,phone,date,password) VALUES(?,?,?,?,?)'
            #ins = 'INSERT INTO users(new_name,new_email,new_phone,date,password) VALUES(new_name,new_email,new_phone,new_date)'
            curs.execute(ins,(username,email,phone,date,password))
            #return "完成輸入"
            return render_template("registercarvin.html")
   else:
        return redirect(url_for("registercarvin.html"))
            
            
#將things資料寫入資料庫
@app.route('/thingsinto_db',methods=["POST","GET"])
def thingsinto_db():#thingsinto_db
   db = sqlite3.connect('give02db.db') 
      #thingid = None #因為是由系統自動產生
      #取得頁面上input輸入欄位裡面輸入的欄位資料:
   if request.method =="POST":
        giver_number = request.form["giver_number"]
        thingname = request.form["thingname"] 
        groupn = request.form["groupn"]
        vols = request.form["vols"]
        coment = request.form["coment"]
        date = datetime.now() #抓取系統時間要先導入from datetime import datetime       
        status = request.form["status"]        
        #potoaddress = request.form["potoaddress"]#照片上傳另行處理
        with db:
            #db.executemany#沒作用但暫不刪
            curs = db.cursor()
            #data = cursor.fetchone()#沒作用但暫不刪
            ins = 'INSERT INTO things(giver_number,thingname,groupn,vols,coment,date,status) VALUES(?,?,?,?,?,?,?)'
            #ins = 'INSERT INTO things(new_name,new_email,new_phone,date) VALUES(new_name,new_email,new_phone,new_date)'
            curs.execute(ins,(giver_number,thingname,groupn,vols,coment,date,status))
            #return "完成輸入"
            return render_template("things_form.html")
   else:
        return redirect(url_for("things_form.html"))


#將things_histories資料寫入資料庫things_histories_db
@app.route('/things_histories_db',methods=["POST","GET"])
def things_histories_db():#things_histories_db
   db = sqlite3.connect('give02db.db') 
      #thingid = None #因為是由系統自動產生
      #取得頁面上input輸入欄位裡面輸入的欄位資料:
   if request.method =="POST":
        #sirenumber = request.form["sirenumber"]#系統自動產生
        thingid = request.form["thingid"] 
        coment = request.form["coment"]
        status = request.form["status"]
        dostausmen_number = request.form["dostausmen_number"]
        time = datetime.now() #抓取系統時間要先導入from datetime import datetime       
        #status = request.form["status"]        
        #potoaddress = request.form["potoaddress"]#照片上傳另行處理
        with db:
            #db.executemany#沒作用但暫不刪
            curs = db.cursor()
            #data = cursor.fetchone()#沒作用但暫不刪
            ins = 'INSERT INTO things_histories(thingid,coment,status,dostausmen_number,time) VALUES(?,?,?,?,?)'
            #ins = 'INSERT INTO things(new_name,new_email,new_phone,date) VALUES(new_name,new_email,new_phone,new_date)'
            curs.execute(ins,(thingid,coment,status,dostausmen_number,time))
            #return "完成輸入"
            return render_template("things_histories_form.html")
   else:
        return render_template("things_histories_form.html")
  
    


@app.route('/login', methods=['POST'])
def result():
     if request.method == 'POST':
         user = request.values['user']
         return render_template('result.html', name=user)
@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())




@app.route('/testget', methods=['GET'])
def testget():
     name = request.args.get('name')
     return 'My name is {}'.format(name)

@app.route('/member_form')
def member_form():
     return render_template('member_form.html')

@app.route('/<int:userID>')
def hello(userID):
     return 'The user ID is: {}'.format(escape(userID))
@app.route('/loaddb',methods=['POST','GET'])
def loaddb():# 顯示全部分享物品目錄 20210130會議中3人共同克服無法在html顯示的問題
    conn = sqlite3.connect('give02db.db')
    cursor = conn.cursor()
    conn.commit()
    things={}
    things=cursor.execute("SELECT * FROM things;")
    row = things.fetchall()
    print("This is data in my sqlite3.....by carvin")
    print(f"{row[0]}")
    return render_template('thingsplay_form.html', things=row)
####

if __name__ == '__main__':

     app.run(debug=True)