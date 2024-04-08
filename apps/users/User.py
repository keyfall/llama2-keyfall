from run import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)#主键
    username = db.Column(db.String, unique=True, nullable=False)#username不重复，不可为空
    password = db.Column(db.String)
    email = db.Column(db.String)