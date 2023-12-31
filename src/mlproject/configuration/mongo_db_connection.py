import pymongo
from src.mlproject.constant.database import DATABASE_NAME # Because DATABASE_NAME we have alredy defined in constant database.py file
import certifi # This library provide the certificate if you have sent the HTTP request to the server he provide ssl on layer.
from src.mlproject.constant.env_variable import MONGODB_URL_KEY
import os
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                mongo_db_url = os.getenv('MONGO_DB_URL')
                print(mongo_db_url)
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e

