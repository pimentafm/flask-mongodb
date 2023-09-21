from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://root:root@localhost:27017/information"

mongo = PyMongo(app)

@app.route('/create_user', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        id = mongo.db.users.insert_one({
            'name': _name,
            'email': _email,
            'password': _hashed_password  # Store the hashed password
        }).inserted_id

        response = jsonify("User added successfully")
        response.status_code = 200

        return response
    else:
        return not_found()
    
@app.errorhandler(404)
def not_found(error = None):
    message = {
        'status': 404,
        'message': 'Not found!'
    }

    response = jsonify(message)
    response.status_code = 404

    return response


if __name__ == "__main__":
    app.run(debug = True)


