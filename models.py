#models.py
#20210205
from flask_login import UserMixin #login_manager,
from app import app
from app import db
from tp3 import login
#D:\tp3>pip install login
#from apps.user.models import User

@login.user_loader
def load_user(user_number):
	return User.query.filter_by(id=user_number).first()


class User(db.Model,UserMixin):
	 __tablename__ = "users"
	 number = db.Column(db.Integer,Primary_Key=True)
	 username = db.Column(db.String(20),unique=True,nullable = False)
	 phone = db.Column(db.String(20),nullable = False)
	 password = db.Column(db.String(20),nullable = False)
	 email = db.Column(db.String(120),unique=True,nullable = False)
	 def __repr__(self):
		 return '<User % r >' % self.username