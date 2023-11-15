from app.models.user_model import UserModel

class UserService:
    @classmethod
    def create_user(cls, data):
        return UserModel.create_user(data)

    @classmethod
    def get_users(cls):
        return UserModel.get_users()
