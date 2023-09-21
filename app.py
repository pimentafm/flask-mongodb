from flask import Flask
from flask_pymongo import PyMongo
from services.UserService import UserService
from repository.UserRepository import UserRepository
import routes

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://root:root@localhost:27017/information"
mongo = PyMongo(app)

user_repository = UserRepository(mongo.db)
user_service = UserService(user_repository)

routes.init_app(app, user_service)

if __name__ == "__main__":
    app.run(debug=True)


