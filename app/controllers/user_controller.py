from app.services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def add_user(self, user_data):
        """
        Add a new user by passing the data to the service.
        """
        return self.user_service.add_user(user_data)

    def get_user(self, user_id):
        """
        Get user details by ID.
        """
        return self.user_service.get_user_by_id(user_id)

    def update_user(self, user_id, update_data):
        """
        Update user details.
        """
        return self.user_service.update_user(user_id, update_data)

    def delete_user(self, user_id):
        """
        Delete a user by ID.
        """
        return self.user_service.delete_user(user_id)

    def list_users(self):
        """
        List all users by passing through the service layer.
        """
        return self.user_service.get_all_users()
