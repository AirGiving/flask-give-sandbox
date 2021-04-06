#tp3/config.py
#20210205
import os
import sqlite3
#CSRF_ENABLED = True
#SECRET_KEY = '123qwe'



basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
	#SECRET_KEY
	#SECRET_KEY = os.environ.get('SECRET_KEY') or '839ba4d4f8bd47deb5f21d77449e97d6'
	#CSRF_ENABLED = True

	#CSRF_ENABLED = True
	#SECRET_KEY ='123qwe'
	SQLALCHEMY_DATABASE_URL='sqlite:///giveo2db.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	#SECRET_KEY ='6b90c3136c634fddb597289d392571e6'
	

	RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'A-RECAPTCHA_PUBLIC_KEY'
	RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'A-RECAPTCHA_PRIVATE_KEY'
	#SECRET_KEY = '839ba4d4f8bd47deb5f21d77449e97d6'

	"""database configuration"""
	#db = sqlite3.connect('give02db.db')
	#db = SQLALCHEMY_DATABASE_URL=os.environ.get('give02db.db')
	#SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL') or 'sqlite:///'give02db.db'+ os.path.join(basedir,'app')'
	#SQLALCHEMY_DATABASE_URL='sqlite:///giveo2db.db'
	#SQLALCHEMY_TRACK_MODIFICATIONS=True

	#app.config['SQLALCHEMY_DATABASES_URI'] = 'sqlite:///giveo2db.db'
	#app.config['SQLALCHEMY_BINDS'] = 'mysql+pymysql://root:admin@127.0.0.1:3306/movie'
	#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	#db = SQLAlchemy(app)

	#RuntimeError: A secret key is required to use CSRF.