from bson.objectid import ObjectId

class UserRepository:
    def __init__(self, db):
        self.db = db

    def add(self, user):
        return self.db.users.insert_one(user.__dict__).inserted_id

    def get_all(self):
        return self.db.users.find()

    def get_by_id(self, id):
        return self.db.users.find_one({'_id': ObjectId(id)})

    def delete(self, id):
        return self.db.users.delete_one({'_id': ObjectId(id)})

    def update(self, id, user):
        return self.db.users.update_one({'_id': ObjectId(id)}, {'$set': user.__dict__})