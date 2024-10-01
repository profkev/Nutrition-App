from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.controllers.recipe_controller import RecipeController
from bson.objectid import ObjectId

# Create the blueprint for recipe-related routes
recipe_api = Blueprint('recipe_api', __name__)

# Initialize the controller
recipe_controller = RecipeController()

# Route to list all recipes and render the 'recipes.html' template
@recipe_api.route('/recipes', methods=['GET'])
def list_recipes():
    """
    Fetch all recipes and render the 'recipes.html' page.
    """
    recipes = recipe_controller.get_all_recipes()
    # Render the 'recipes.html' template and pass the recipes to it
    return render_template('recipes.html', recipes=recipes)

# Route for creating a new recipe via form submission or API
@recipe_api.route('/recipes', methods=['POST'])
def create_recipe():
    """
    Create a new recipe from form data (or API JSON) and redirect to the list of recipes.
    """
    # For API calls, accept JSON data
    if request.is_json:
        recipe_data = request.get_json()
    else:
        # If it's a form submission, use form data
        recipe_data = {
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'ingredients': request.form.get('ingredients')
        }

    new_recipe = recipe_controller.create_recipe(recipe_data)
    return redirect(url_for('recipe_api.list_recipes'))

# Route for getting a specific recipe (API)
@recipe_api.route('/recipes/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """
    Fetch a specific recipe by ID.
    """
    recipe = recipe_controller.get_recipe(ObjectId(recipe_id))
    return jsonify(recipe)

# Route for editing a recipe via form submission
@recipe_api.route('/recipes/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    """
    Update a recipe based on form or API submission.
    """
    if request.is_json:
        recipe_data = request.get_json()
    else:
        # If it's a form submission, use form data
        recipe_data = {
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'ingredients': request.form.get('ingredients')
        }
    
    updated_recipe = recipe_controller.update_recipe(ObjectId(recipe_id), recipe_data)
    return redirect(url_for('recipe_api.list_recipes'))

# Route for deleting a recipe
@recipe_api.route('/recipes/<recipe_id>', methods=['DELETE', 'POST'])
def delete_recipe(recipe_id):
    """
    Delete a specific recipe by ID, either through API or form submission.
    """
    recipe_controller.delete_recipe(ObjectId(recipe_id))
    return redirect(url_for('recipe_api.list_recipes'))

# Route to serve the page for creating a new recipe (form-based)
@recipe_api.route('/recipes/new', methods=['GET'])
def new_recipe_page():
    """
    Render the page to create a new recipe via a form.
    """
    return render_template('new_recipe.html')
