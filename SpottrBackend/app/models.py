from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	age = db.Column(db.Integer, unique=False)
	first_name = db.Column(db.String(64), unique=False)
	bio = db.Column(db.Text, unique=False)

	def __repr__(self):
		return '<User %r' % (self.username)