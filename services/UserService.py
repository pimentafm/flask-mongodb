from domain.User import User


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def authenticate(self, email, password):
        user = self.repository.get_by_email(email)
        if user and user.verify_password(password):
            return {"status": "success", "message": "Authenticated", "user": user.to_dict()}
        return {"status": "error", "message": "Authentication failed"}

    def create_user(self, name, email, password):
        user = User(name, email, password)
        return self.repository.add(user)

    def get_users(self):
        users_cursor = self.repository.get_all()
        users = list(users_cursor)

        for user in users:
            del user['password']
        return users

    def get_user_by_id(self, id):
        user = self.repository.get_by_id(id)

        if user:
            user_dict = user.to_dict()
            del user_dict['password']
            return user_dict
        return None

    def delete_user(self, id):
        return self.repository.delete(id)

    def update_user(self, id, name, email, password):
        user = User(name, email, password)
        return self.repository.update(id, user)
