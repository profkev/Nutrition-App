from flask import Blueprint, request, jsonify
from app.controllers.user_controller import UserController

# Define the blueprint for user-related routes
user_routes = Blueprint('user_routes', __name__)

# Initialize the controller
user_controller = UserController()

# Route for listing all users
@user_routes.route('/users', methods=['GET'])
def list_users():
    users = user_controller.list_users()
    return jsonify(users)

# Route for adding a new user
@user_routes.route('/users', methods=['POST'])
def add_user():
    user_data = request.get_json()
    new_user = user_controller.add_user(user_data)
    return jsonify(new_user), 201

# Route for getting a specific user by ID
@user_routes.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_controller.get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

# Route for updating a user
@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    update_data = request.get_json()
    updated_user = user_controller.update_user(user_id, update_data)
    return jsonify(updated_user)

# Route for deleting a user
@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_controller.delete_user(user_id)
    return '', 204
