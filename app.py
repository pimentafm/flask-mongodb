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
            'password': _hashed_password
        }).inserted_id

        response = jsonify("User added successfully")
        response.status_code = 200

        return response
    else:
        return not_found()
    
@app.route('/users')
def users():
    users = mongo.db.users.find()
    response = dumps(users)
    return response

@app.route('/user/<id>')
def user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    response = dumps(user)
    return response

@app.route('/delete/<id>', methods = ['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify("User deleted successifully!")
    return response
    
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


