from app.dao.nutrition_dao import NutritionDAO

class NutritionController:
    def __init__(self):
        self.nutrition_dao = NutritionDAO()

    def add_nutritional_info(self, nutrition_data):
        """ Add new nutritional information """
        return self.nutrition_dao.create_nutrition_info(nutrition_data)

    def get_nutritional_info(self, nutrition_id):
        """ Retrieve nutritional information by ID """
        return self.nutrition_dao.get_nutrition_info_by_id(nutrition_id)

    def update_nutritional_info(self, nutrition_id, update_data):
        """ Update existing nutritional information """
        return self.nutrition_dao.update_nutrition_info(nutrition_id, update_data)

    def delete_nutritional_info(self, nutrition_id):
        """ Delete nutritional information """
        return self.nutrition_dao.delete_nutrition_info(nutrition_id)
