from bson.objectid import ObjectId
from domain.User import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def add(self, user):
        return self.db.users.insert_one(user.to_dict()).inserted_id

    def get_all(self):
        return self.db.users.find()

    def get_by_id(self, id):
        doc = self.db.users.find_one({'_id': ObjectId(id)})
        return User.from_dict(doc) if doc else None

    def get_by_email(self, email):
        doc = self.db.users.find_one({'email': email})
        return User.from_dict(doc) if doc else None

    def delete(self, id):
        return self.db.users.delete_one({'_id': ObjectId(id)})

    def update(self, id, user):
        return self.db.users.update_one({'_id': ObjectId(id)}, {'$set': user.to_dict()})
