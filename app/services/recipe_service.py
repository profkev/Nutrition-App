from app.dao.recipe_dao import RecipeDAO

class RecipeService:
    def __init__(self):
        self.recipe_dao = RecipeDAO()

    def add_recipe(self, recipe_data):
        return self.recipe_dao.create_recipe(recipe_data)

    def get_recipe_by_id(self, recipe_id):
        return self.recipe_dao.get_recipe_by_id(recipe_id)

    def update_recipe(self, recipe_id, update_data):
        return self.recipe_dao.update_recipe(recipe_id, update_data)

    def delete_recipe(self, recipe_id):
        return self.recipe_dao.delete_recipe(recipe_id)

    def get_all_recipes(self):
        return self.recipe_dao.get_all_recipes()
