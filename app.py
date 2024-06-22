from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from models import db, User
from db_utils import get_user_by_username
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
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
                username=data.get('username'),
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
                about=data.get('about'),
                role='user'
            )
            user.password_hash = generate_password_hash(data.get('password'))  # Hash the password
            db.session.add(user)  # Add user to session
            db.session.commit()  # Commit the session to save user to database
            return jsonify({"message": "Registration successful"}), 201
        except IntegrityError:
            db.session.rollback()  # Rollback the session in case of error
            return jsonify({"error": "Email or Username already registered"}), 400  # Return error if email or username is already registered
        except Exception as e:
            return jsonify({"error": str(e)}), 400  # Return error for any other exception

    return render_template('user/register.html')  # Render registration form template for GET request


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = get_user_by_username(username)

        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['user_role'] = user.role
            if user.role == 'admin':
                return jsonify({"redirect": url_for('admin_dashboard')})
            else:
                return jsonify({"redirect": url_for('user_dashboard')})
        return jsonify({"error": "Invalid credentials"}), 401

    return render_template('login.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    if 'user_role' in session and session['user_role'] == 'admin':
        return render_template('admin/dashboard.html')
    else:
        return redirect(url_for('login'))


@app.route('/user/dashboard')
def user_dashboard():
    if 'user_role' in session and session['user_role'] == 'user':
        return render_template('user/dashboard.html')
    else:
        return redirect(url_for('login'))


@app.route('/admin/admin_manage_users')
def admin_manage_users():
    return render_template('admin/admin_manage_users.html')  # Render admin manage users


@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.firstname = data.get('firstname', user.firstname)
    user.lastname = data.get('lastname', user.lastname)
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.mobile_number = data.get('mobile_number', user.mobile_number)
    user.address1 = data.get('address1', user.address1)
    user.address2 = data.get('address2', user.address2)
    user.suburb = data.get('suburb', user.suburb)
    user.city = data.get('city', user.city)
    user.country = data.get('country', user.country)
    user.postal_code = data.get('postal_code', user.postal_code)
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify(user.to_dict())


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})


@app.route('/api/current_user')
def get_current_user():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return jsonify({'name': user.firstname}), 200
    return jsonify({'error': 'Unauthorized'}), 401


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/api/user_count', methods=['GET'])
def get_user_count():
    # Count users in db
    user_count = User.query.count()
    return jsonify({'count': user_count})


# Run the Flask application
if __name__ == '__main__':
    app.run()
