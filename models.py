from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# Initialize SQLAlchemy for db interactions
db = SQLAlchemy()

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    address1 = db.Column(db.String(100), nullable=False)
    address2 = db.Column(db.String(100))
    suburb = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Increased length to 255
    role = db.Column(db.String(10), default='user')


# Method to hash and set the user's password
def set_password(self, password):
    self.password_hash = generate_password_hash(password)
