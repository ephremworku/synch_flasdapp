from adapters.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    fav_prog_language = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(100), nullable=False, unique=False)
