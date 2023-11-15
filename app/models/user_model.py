from app.models import ModelDB

class UserModel:
    model_db_instance = ModelDB()
    collection = model_db_instance.mongodb()

    @classmethod
    def create_user(cls, data):
        return cls.collection.insert_one(data)

    @classmethod
    def get_users(cls):
        return cls.collection.find()
