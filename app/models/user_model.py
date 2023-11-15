from app.models import MongoDb

class UserModel:
    model_db_instance = MongoDb.mongo_db()
    collection = model_db_instance.users

    @classmethod
    def create_user(cls, data):
        return cls.collection.insert_one(data)

    @classmethod
    def get_users(cls):
        return cls.collection.find()
