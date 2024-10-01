from pymongo.errors import PyMongoError
from app.extensions import mongo
from bson.objectid import ObjectId

class UserDAO:
    def __init__(self):
        self.collection = mongo.db.users

    def create_user(self, user_data):
        try:
            return self.collection.insert_one(user_data).inserted_id
        except PyMongoError as e:
            # Handle or log the error appropriately
            return None

    def get_user_by_id(self, user_id):
        try:
            return self.collection.find_one({'_id': ObjectId(user_id)})
        except PyMongoError as e:
            # Handle or log the error
            return None

    def update_user(self, user_id, update_data):
        try:
            return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': update_data})
        except PyMongoError as e:
            # Handle or log the error
            return None

    def delete_user(self, user_id):
        try:
            return self.collection.delete_one({'_id': ObjectId(user_id)})
        except PyMongoError as e:
            # Handle or log the error
            return None
