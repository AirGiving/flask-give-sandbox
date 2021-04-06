import os,requests



from flask import Flask, g
from flask import request,session
from flask import render_template,flash,redirect,url_for,request

from flask_bootstrap import Bootstrap
from config import Config
#from forms import RegisterForm,LoginForm
#from flask_wtf import LoginForm,RegisterForm
import sqlite3
#from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy

from markupsafe import escape#為測試userID而導入
from datetime import datetime
from flask_bcrypt import Bcrypt
#需要先安裝pip install flask-bcrypt
from flask_login import LoginManager,login_user,current_user,login_required
app = Flask(__name__)
#bootstrap=Bootstrap(app)
#db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)
app.config.from_object(Config)
#login = LoginManager(app)
#login.login_view = 'login'
#login.login_message ='you must login to access this page'
#login.login_message_category ='info'
#from app import app

#from app.forms import RegisterForm,LoginForm
#from app.models import User
#from app import db,login
#from app.routes import *

#app = Flask(__name__)
#app.config['SECRET_KEY']= '123qwe'

app.config['SQLALCHEMY_DATABASES_URI'] = 'sqlite:///giveo2db.db'

#app.config['SQLALCHEMY_BINDS'] = 'mysql+pymysql://root:admin@127.0.0.1:3306/movie'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)