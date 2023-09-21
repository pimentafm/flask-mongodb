from domain.User import User

class UserService:
    def __init__(self, repository):
        self.repository = repository

    def create_user(self, name, email, password):
        user = User(name, email, password)
        return self.repository.add(user)

    def get_users(self):
        return self.repository.get_all()

    def get_user_by_id(self, id):
        return self.repository.get_by_id(id)

    def delete_user(self, id):
        return self.repository.delete(id)

    def update_user(self, id, name, email, password):
        user = User(name, email, password)
        return self.repository.update(id, user)