import pymongo
from config import Config


class MongoDb:
    @staticmethod
    def mongo_db():
        try:
            client = pymongo.MongoClient(Config.MONGO_URI)
            client.server_info()
            db = client.hmvc
            print(" * DB connection established...")

        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(" * Failed to connect DB", err)
            # You might want to add additional exception handling here

        return db
     
     