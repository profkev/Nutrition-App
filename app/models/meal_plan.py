from bson.objectid import ObjectId

class MealPlan:
    def __init__(self, user_id, date, meals, meal_plan_id=None):
        self.meal_plan_id = meal_plan_id or ObjectId()
        self.user_id = user_id
        self.date = date
        self.meals = meals

    def to_dict(self):
        return {
            "_id": self.meal_plan_id,
            "user_id": self.user_id,
            "date": self.date,
            "meals": self.meals
        }
