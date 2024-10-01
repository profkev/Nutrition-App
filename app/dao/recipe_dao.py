from app.extensions import mongo

class RecipeDAO:
    def create_recipe(self, recipe_data):
        """
        Insert a new recipe into the database.
        """
        return mongo.db.recipes.insert_one(recipe_data)

    def get_recipe_by_id(self, recipe_id):
        """
        Retrieve a recipe by its ID.
        """
        return mongo.db.recipes.find_one({'_id': recipe_id})

    def update_recipe(self, recipe_id, update_data):
        """
        Update an existing recipe with new data.
        """
        return mongo.db.recipes.update_one({'_id': recipe_id}, {'$set': update_data})

    def delete_recipe(self, recipe_id):
        """
        Delete a recipe from the database by its ID.
        """
        return mongo.db.recipes.delete_one({'_id': recipe_id})

    def get_all_recipes(self):
        """
        Retrieve all recipes from the database.
        """
        return list(mongo.db.recipes.find())
