from app.services.recipe_service import RecipeService

class RecipeController:
    def __init__(self):
        self.recipe_service = RecipeService()

    def create_recipe(self, recipe_data):
        return self.recipe_service.add_recipe(recipe_data)

    def get_recipe(self, recipe_id):
        return self.recipe_service.get_recipe_by_id(recipe_id)

    def update_recipe(self, recipe_id, update_data):
        return self.recipe_service.update_recipe(recipe_id, update_data)

    def delete_recipe(self, recipe_id):
        return self.recipe_service.delete_recipe(recipe_id)

    def get_all_recipes(self):
        return self.recipe_service.get_all_recipes()
