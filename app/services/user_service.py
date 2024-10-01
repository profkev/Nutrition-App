from app.dao.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def add_user(self, user_data):
        return self.user_dao.create_user(user_data)

    def get_user_by_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)

    def update_user(self, user_id, update_data):
        return self.user_dao.update_user(user_id, update_data)

    def delete_user(self, user_id):
        return self.user_dao.delete_user(user_id)

    def get_all_users(self):
        return self.user_dao.get_all_users()
