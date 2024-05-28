from entities.user import User as UserEntity
from repositories.user_repository import UserRepository
from adapters.orm import User as UserORM

class UserService:
    @staticmethod
    def create_user(name: str, email: str, fav_prog_language: str, sex: str):
        if UserRepository.get_user_by_email(email):
            raise ValueError("User already exists")
        user_entity = UserEntity(name, email, fav_prog_language, sex)
        user_orm = UserORM(name=user_entity.name, email=user_entity.email, fav_prog_language=fav_prog_language, sex=sex)
        UserRepository.add_user(user_orm)
