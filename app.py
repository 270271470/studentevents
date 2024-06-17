from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from forms import RegistrationForm
from models import db, User
from config import Config
from werkzeug.security import generate_password_hash
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from Config object


# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate


# Define route for home page
@app.route('/')
def welcome_home():
    return render_template('index.html')  # Render the home page template


# Define the route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from request
        if not data:
            return jsonify({"error": "Invalid input"}), 400  # Return an error if there is no data

        try:
            # Create new User object with the data from the request
            user = User(
                firstname=data.get('firstName'),
                lastname=data.get('lastName'),
                email=data.get('email'),
                mobile_number=data.get('mobile_number', ''),
                address1=data.get('streetAddress'),
                address2=data.get('address2', ''),
                suburb=data.get('suburb', ''),
                city=data.get('city'),
                country=data.get('country'),
                postal_code=data.get('postalCode'),
                role='user'
            )
            user.password_hash = generate_password_hash(data.get('password'))  # Hash the password
            db.session.add(user)  # Add user to session
            db.session.commit()  # Commit the session to save user to database
            return jsonify({"message": "Registration successful"}), 201
        except IntegrityError:
            db.session.rollback()  # Rollback the session in case of error
            return jsonify({"error": "Email already registered"}), 400  # Return error if email is already registered
        except Exception as e:
            return jsonify({"error": str(e)}), 400  # Return error for any other exception

    return render_template('user/register.html')  # Render registration form template for GET request


# Run the Flask application
if __name__ == '__main__':
    app.run()
