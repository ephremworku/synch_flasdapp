from adapters.orm import User
from adapters.database import db

class UserRepository:
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
