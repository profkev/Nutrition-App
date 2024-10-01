# /app/dao/meal_dao.py
from app.extensions import mongo
from bson.objectid import ObjectId

class MealDAO:
    def __init__(self):
        self.collection = mongo.db.meals

    def create_meal(self, meal_data):
        return self.collection.insert_one(meal_data).inserted_id

    def get_meal_by_id(self, meal_id):
        return self.collection.find_one({'_id': ObjectId(meal_id)})

    def update_meal(self, meal_id, meal_data):
        return self.collection.update_one({'_id': ObjectId(meal_id)}, {'$set': meal_data})

    def delete_meal(self, meal_id):
        return self.collection.delete_one({'_id': ObjectId(meal_id)})
