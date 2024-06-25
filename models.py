from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy for db interactions
db = SQLAlchemy()


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)  # New field
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
    about = db.Column(db.Text)  # New field
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), default='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'mobile_number': self.mobile_number,
            'address1': self.address1,
            'address2': self.address2,
            'suburb': self.suburb,
            'city': self.city,
            'country': self.country,
            'postal_code': self.postal_code,
            'role': self.role
        }
      