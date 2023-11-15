import pymongo
from config import Config


class ModelDB:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(Config.MONGO_URI)
            self.client.server_info()  # Check if the server is available
            self.db = self.client.hmvc
            print(" * DB connection established...")

        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(" * Failed to connect to the database:", err)
            
    def mongodb(self):
        return self.db
