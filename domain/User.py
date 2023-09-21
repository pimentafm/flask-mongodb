from werkzeug.security import generate_password_hash

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)