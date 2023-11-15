from app.models import MongoDb

class UserModel:
    model_db_instance = MongoDb()
    mongo_db = model_db_instance.mongo_db()
    collection = mongo_db.users

    @classmethod
    def create_user(cls, data):
        return cls.collection.insert_one(data)

    @classmethod
    def get_users(cls):
        return cls.collection.find()
