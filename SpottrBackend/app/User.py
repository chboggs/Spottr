# from flask import Flask, request, jsonify
# from flask.ext.sqlalchemy import SQLAlchemy
# from passlib.apps import custom_app_context as password_context

# db = SQLAlchemy()

# class User(db.Model):
# 	## DB stuff right here
# 	__tablename__ = 'users'
# 	username = db.Column(db.String, primary_key=True)
# 	password_hash = db.Column(db.String)
# 	email = db.Column(db.String)
# 	first_name = db.Column(db.String)
# 	age = db.Column(db.Int)
# 	authenticated = db.Column(db.Boolean, default=False)

# 	@property
#    	def is_authenticated(self):
#     	return True

# 	@property
#     def is_active(self):
#        	return True

#     @property
#     def is_anonymous(self):
#         return False

#     def get_id(self):
#         return str(self.username)

#     def __repr__(self):
#         return '<User %r>' % (self.nickname)

# 	def hash_pass(self, password):
# 		self.password_hash = password_context.encrypt(password)

# 	def verify_pass(self, password):
# 		return password_context.verify(password, self.password_hash)

# 	def post(self):
# 		# JSON validation
# 		user_info = requests.get_json()
# 		username = user_info['username']
# 		password = user_info['password']
# 		## check for existing user/email

# 		user = User(username=username, email=user_info['email'], first_name=user_info['first_name'], age=user_info['age'])
# 		user.hash_pass(password)

# 		