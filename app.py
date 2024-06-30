from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from models import db, User, Event, Booking
from db_utils import get_user_by_username
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError, NoResultFound
import os


# init flask app
app = Flask(__name__)
app.config.from_object(Config)  # load configuration


# login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate


# Configuration for file uploads
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Define route for home page
@app.route('/')
def welcome_home():
    return render_template('index.html')  # Render the home page template


@app.route('/about-us')
def about_us():
    return render_template('about-us.html')  # Render about-us tpl


@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')  # Render about-us tpl


@app.route('/events')
def events_all():
    return render_template('events/events.html')  # Render all events tpl


@app.route('/events-workshops')
def events_workshops():
    return render_template('events/events-workshops.html')  # Render workshops events tpl


@app.route('/events-outdoor')
def events_outdoor():
    return render_template('events/events-outdoor.html')  # Render outdoor events tpl


@app.route('/events-clubs')
def events_clubs():
    return render_template('events/events-clubs.html')  # Render clubs events tpl


@app.route('/events-adventure')
def events_adventure():
    return render_template('events/events-adventure.html')  # Render adventure events tpl


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')  # Render privacy tpl


@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms-of-service.html')  # Render TOS tpl


@app.route('/support-center')
def support_center():
    return render_template('support-center.html')  # Render the support center template


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


@app.route('/api/get_user_info', methods=['GET'])
def get_user_info():
    user_id = request.args.get('user_id')
    try:
        user = User.query.filter_by(id=user_id).one()
        return jsonify({
            'id': user.id,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'username': user.username,
            'email': user.email,
            'mobile_number': user.mobile_number,
            'address1': user.address1,
            'address2': user.address2,
            'suburb': user.suburb,
            'city': user.city,
            'country': user.country,
            'postal_code': user.postal_code,
        })
    except NoResultFound:
        return jsonify({'error': 'User not found'}), 404


@app.route('/api/update_user_info', methods=['POST'])
def update_user_info():
    data = request.json
    user_id = data.get('id')
    try:
        user = User.query.filter_by(id=user_id).one()

        if User.query.filter(User.email == data['email'], User.id != user_id).first():
            return jsonify({'error': 'Email already exists'}), 400
        if User.query.filter(User.username == data['username'], User.id != user_id).first():
            return jsonify({'error': 'Username already exists'}), 400

        user.firstname = data['firstname']
        user.lastname = data['lastname']
        user.username = data['username']
        user.email = data['email']
        user.mobile_number = data['mobile_number']
        user.address1 = data['address1']
        user.address2 = data['address2']
        user.suburb = data['suburb']
        user.city = data['city']
        user.country = data['country']
        user.postal_code = data['postal_code']

        db.session.commit()
        return jsonify({'success': 'User updated successfully'})
    except NoResultFound:
        return jsonify({'error': 'User not found'}), 404


@app.route('/user/user_update_info')
def user_update_info():
    return render_template('user/user_update_info.html')  # Render admin manage users


@app.route('/user/user_manage_booking')
def user_manage_booking():
    return render_template('user/user_manage_booking.html')  # Render admin manage booking


@app.route('/admin/admin_manage_users')
def admin_manage_users():
    return render_template('admin/admin_manage_users.html')  # Render admin manage users


@app.route('/admin/admin_pending_bookings')
def admin_pending_bookings():
    return render_template('admin/admin_pending_bookings.html')  # Render admin pending bookings


@app.route('/admin/view_all_bookings')
def admin_view_all_bookings():
    return render_template('admin/admin_view_all_bookings.html')  # Render admin all bookings


@app.route('/admin/admin_manage_events')
def admin_manage_events():
    return render_template('admin/admin_manage_events.html')  # Render admin manage events


@app.route('/api/event_count', methods=['GET'])
def get_event_count():
    # Count events in db
    event_count = Event.query.count()
    return jsonify({'count': event_count})


@app.route('/api/active_bookings_count', methods=['GET'])
def get_active_bookings_count():
    count = Booking.query.filter_by(status='Approved').count()
    return jsonify({'count': count})


@app.route('/api/pending_bookings_count', methods=['GET'])
def get_pending_bookings_count():
    count = Booking.query.filter_by(status='Pending').count()
    return jsonify({'count': count})


@app.route('/api/events', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.date.asc()).all()
    return jsonify([event.to_dict() for event in events])


# Define the route for adding or editing an event
@app.route('/api/events', methods=['POST'])
def add_event():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Add event to the database
        data = request.form
        event = Event(
            name=data['name'],
            location=data['location'],
            date=data['date'],
            time=data['time'],
            fee=data['fee'],
            image_path=os.path.join(app.config['UPLOAD_FOLDER'], filename),
            category=data['category']
        )
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'Event added successfully'}), 201
    return jsonify({'error': 'File not allowed'}), 400


@app.route('/api/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'error': 'Event not found'}), 404

    data = request.form
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            event.image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    event.name = data['name']
    event.location = data['location']
    event.date = data['date']
    event.time = data['time']
    event.fee = data['fee']
    event.category = data['category']
    db.session.commit()
    return jsonify({'message': 'Event updated successfully'}), 200


@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted'})


# Booking route
@app.route('/api/bookings', methods=['POST'])
def book_event():
    try:
        data = request.json
        print('Booking request data:', data)  # Log the booking request data

        user_id = data.get('user_id')
        event_id = data.get('event_id')
        fullname = data.get('fullname')
        location = data.get('location')
        date = data.get('date')
        time = data.get('time')
        quantity = data.get('quantity')
        total_fee = data.get('total_fee')

        if not user_id or not event_id:
            return jsonify({'error': 'Missing user_id or event_id'}), 400

        # Ensure user and event exist in the database
        user = User.query.get(user_id)
        event = Event.query.get(event_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        if not event:
            return jsonify({'error': 'Event not found'}), 404

        booking = Booking(
            user_id=user_id,
            event_id=event_id,
            fullname=fullname,
            location=location,
            date=date,
            time=time,
            quantity=quantity,
            total_fee=total_fee
        )

        db.session.add(booking)
        db.session.commit()
        return jsonify({'message': 'Booking confirmed!'}), 201
    except IntegrityError as e:
        db.session.rollback()
        print('IntegrityError:', str(e))
        return jsonify({'error': 'IntegrityError: ' + str(e)}), 500
    except Exception as e:
        db.session.rollback()
        print('Error booking event:', str(e))
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500


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


# Define the User Loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for getting current user details
@app.route('/api/current_user', methods=['GET'])
def get_current_user():
    user_id = session.get('user_id')  # Get user_id from session
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    user = User.query.get(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'username': user.username,
            'email': user.email,
            'mobile_number': user.mobile_number,
            'address1': user.address1,
            'address2': user.address2,
            'suburb': user.suburb,
            'city': user.city,
            'country': user.country,
            'postal_code': user.postal_code,
        })
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/api/user_count', methods=['GET'])
def get_user_count():
    # Count users in db
    user_count = User.query.count()
    return jsonify({'count': user_count})


@app.route('/api/user/bookings', methods=['GET'])
def get_user_bookings():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    bookings = Booking.query.filter_by(user_id=user_id).all()
    bookings_data = []
    for booking in bookings:
        event = Event.query.get(booking.event_id)
        # Ensure the path starts from the root
        image_path = '/' + event.image_path.replace('\\', '/')
        bookings_data.append({
            'id': booking.id,
            'event': {
                'name': event.name,
                'location': event.location,
                'date': event.date,
                'time': event.time,
                'image_path': image_path
            },
            'total_fee': booking.total_fee,
            'status': booking.status
        })

    return jsonify(bookings_data)


@app.route('/api/bookings/<int:booking_id>', methods=['PATCH'])
def cancel_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    if booking.status != 'Pending':
        return jsonify({'error': 'Only pending bookings can be cancelled'}), 400

    booking.status = 'Cancelled'
    db.session.commit()
    return jsonify({'message': 'Booking cancelled successfully!'})


@app.route('/api/bookings/pending', methods=['GET'])
def get_pending_bookings():
    pending_bookings = Booking.query.filter_by(status='Pending').all()
    bookings_data = []
    for booking in pending_bookings:
        event = Event.query.get(booking.event_id)
        image_path = '/' + event.image_path.replace('\\', '/')
        user = User.query.get(booking.user_id)
        bookings_data.append({
            'id': booking.id,
            'user': {
                'fullname': f"{user.firstname} {user.lastname}"
            },
            'event': {
                'name': event.name,
                'location': event.location,
                'date': event.date,
                'time': event.time,
                'image_path': image_path
            },
            'total_fee': booking.total_fee,
            'status': booking.status
        })

    return jsonify(bookings_data)


# Route to get all bookings
@app.route('/api/bookings/all', methods=['GET'])
def get_all_bookings():
    bookings = Booking.query.all()
    bookings_data = []
    for booking in bookings:
        user = User.query.get(booking.user_id)
        event = Event.query.get(booking.event_id)
        image_path = '/' + event.image_path.replace('\\', '/')
        bookings_data.append({
            'id': booking.id,
            'user': {
                'fullname': f'{user.firstname} {user.lastname}'
            },
            'event': {
                'name': event.name,
                'location': event.location,
                'date': event.date,
                'time': event.time,
                'image_path': image_path
            },
            'total_fee': booking.total_fee,
            'status': booking.status
        })
    return jsonify(bookings_data)


@app.route('/api/bookings/<int:booking_id>/approve', methods=['POST'])
def approve_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    if booking.status != 'Pending':
        return jsonify({'error': 'Only pending bookings can be approved'}), 400

    booking.status = 'Approved'
    db.session.commit()
    return jsonify({'message': 'Booking approved successfully!'})


# Run the Flask application
if __name__ == '__main__':
    app.run()
