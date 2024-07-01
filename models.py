from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy for db interactions
db = SQLAlchemy()


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
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

    # Relationship with Booking
    bookings = db.relationship('Booking', backref='user', lazy=True)

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


# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(120), nullable=False)
    fee = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'time': self.time,
            'fee': self.fee,
            'image_path': self.image_path,
            'category': self.category
        }


# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_fee = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='Pending', nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'event_id': self.event_id,
            'fullname': self.fullname,
            'location': self.location,
            'date': self.date.isoformat(),
            'time': self.time.isoformat(),
            'quantity': self.quantity,
            'total_fee': self.total_fee,
            'status': self.status
        }
