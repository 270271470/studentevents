from werkzeug.security import generate_password_hash
from models import db, User


# Method to hash and set the user's password
def set_password(self, password):
    self.password_hash = generate_password_hash(password)


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()
