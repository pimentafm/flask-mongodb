from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, d):
        # Create a new instance without calling __init__
        user = cls.__new__(cls)
        user.name = d['name']
        user.email = d['email']
        user.password = d['password']  # Directly set the hashed password
        return user
