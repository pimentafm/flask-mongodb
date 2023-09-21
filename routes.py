from flask import jsonify, request, session
from flask_login import login_required
from bson.json_util import dumps


def init_app(app, user_service):
    @app.route('/login', methods=['POST'])
    def login():
        _json = request.json
        _email = _json.get('email')
        _password = _json.get('password')

        # Authenticate the user
        result = user_service.authenticate(_email, _password)

        if result['status'] == 'success':
            session['logged_in'] = True
            session['user'] = result['user']
            return jsonify(result), 200
        else:
            return jsonify(result), 401

    @app.route('/logout', methods=['GET'])
    def logout():
        session.pop('user', None)
        return jsonify({'status': 'success', 'message': 'Logged out'}), 200

    @login_required
    @app.route('/create_user', methods=['POST'])
    def add_user():
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _password = _json['password']

        if _name and _email and _password and request.method == 'POST':
            id = user_service.create_user(_name, _email, _password)
            return jsonify("User added successfully"), 200
        else:
            return jsonify({'status': 404, 'message': 'Not found!'}), 404

    @login_required
    @app.route('/user/<id>', methods=['GET'])
    def get_user(id):
        user = user_service.get_user_by_id(id)

        if user:
            return dumps(user), 200
        else:
            return jsonify({'status': 404, 'message': 'User not found!'}), 404

    @login_required
    @app.route('/users', methods=['GET'])
    def get_users():
        users = user_service.get_users()
        return dumps(users), 200

    @login_required
    @app.route('/update/<id>', methods=['PUT'])
    def update_user(id):
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _password = _json['password']

        if _name and _email and _password and request.method == 'PUT':
            user_service.update_user(id, _name, _email, _password)
            return jsonify("User updated successfully"), 200
        else:
            return jsonify({'status': 404, 'message': 'Not found!'}), 404

    @login_required
    @app.route('/delete/<id>', methods=['DELETE'])
    def delete_user(id):
        user_service.delete_user(id)
        return jsonify("User deleted successfully"), 200
