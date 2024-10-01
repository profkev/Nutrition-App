print("Loading meal_controller.py")

from app.dao.meal_dao import MealDAO

print("Successfully imported MealDAO in meal_controller.py")

class MealController:
    def __init__(self):
        self.meal_dao = MealDAO()

    def create_meal(self, meal_data):
        return self.meal_dao.create_meal(meal_data)



# /app/controllers/meal_controller.py
from app.dao.meal_dao import MealDAO

class MealController:
    def __init__(self):
        self.meal_dao = MealDAO()

    def create_meal(self, meal_data):
        return self.meal_dao.create_meal(meal_data)

    def get_meal(self, meal_id):
        return self.meal_dao.get_meal_by_id(meal_id)

    def update_meal(self, meal_id, meal_data):
        return self.meal_dao.update_meal(meal_id, meal_data)

    def delete_meal(self, meal_id):
        return self.meal_dao.delete_meal(meal_id)
