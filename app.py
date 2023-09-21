from flask import Flask
from flask_pymongo import PyMongo
from services.UserService import UserService
from repository.UserRepository import UserRepository
import routes
import os

app = Flask(__name__)

# Use environment variables for sensitive information
app.secret_key = os.environ.get("SECRET_KEY", "default_secret_key")
app.config['MONGO_URI'] = os.environ.get(
    "MONGO_URI", "mongodb://root:root@localhost:27017/information")

mongo = PyMongo(app)

user_repository = UserRepository(mongo.db)
user_service = UserService(user_repository)

routes.init_app(app, user_service)

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", True))


# from flask import Flask
# from flask_pymongo import PyMongo
# from services.UserService import UserService
# from repository.UserRepository import UserRepository
# import routes
# import os

# app = Flask(__name__)

# # Use environment variables for sensitive information
# app.secret_key = os.environ.get("SECRET_KEY", "default_secret_key")
# app.config['MONGO_URI'] = os.environ.get("MONGO_URI", "mongodb://root:root@localhost:27017/information")

# mongo = PyMongo(app)

# user_repository = UserRepository(mongo.db)
# user_service = UserService(user_repository)

# routes.init_app(app, user_service)

# if __name__ == "__main__":
#     app.run(debug=os.environ.get("FLASK_DEBUG", True))
