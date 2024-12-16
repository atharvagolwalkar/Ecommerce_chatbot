from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for efficiency
db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app

# Database Models (defining tables in the database)
class Product(db.Model):
    """Model for storing product information."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Product name
    description = db.Column(db.Text)  # Product description
    price = db.Column(db.Float, nullable=False)  # Product price
    category = db.Column(db.String(50))  # Product category (e.g., Electronics, Books)
    stock = db.Column(db.Integer, default=0)  # Product stock

class ChatMessage(db.Model):
    """Model for storing chat messages."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))  # User ID who sent the message
    content = db.Column(db.Text, nullable=False)  # Message content
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of message
    message_type = db.Column(db.String(10))  # Message type ('user' or 'bot')

class User(db.Model):
    """Model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
    password = db.Column(db.String(120), nullable=False)  # User password (to be hashed in production)

# API Routes (handling the HTTP requests)

@app.route('/api/products', methods=['GET'])
def get_products():
    """API route to get products, optionally filtered by category or search term."""
    category = request.args.get('category')  # Get category filter from query params
    search = request.args.get('search')  # Get search term from query params
    
    query = Product.query  # Start with the base query for all products
    
    # Apply filters if provided
    if category:
        query = query.filter_by(category=category)
    if search:
        query = query.filter(Product.name.ilike(f'%{search}%'))  # Case-insensitive search
    
    products = query.all()  # Get all matching products from the database
    # Return the products as a JSON response
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': p.price,
        'category': p.category,
        'stock': p.stock
    } for p in products])

@app.route('/api/auth/register', methods=['POST'])
def register():
    """API route for registering a new user."""
    data = request.json  # Get the registration data from the request body
    
    # Check if the username already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({
            'success': False,
            'message': 'Username already exists'
        }), 400  # Return an error if username is taken
    
    # Create a new user instance
    new_user = User(
        username=data['username'],
        password=data['password']  # Password should be hashed in production
    )
    
    try:
        db.session.add(new_user)  # Add the new user to the database
        db.session.commit()  # Commit the changes
        return jsonify({
            'success': True,
            'user_id': new_user.id,
            'message': 'Registration successful'
        })
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({
            'success': False,
            'message': 'Registration failed'
        }), 500  # Return error if registration fails

@app.route('/api/auth/login', methods=['POST'])
def login():
    """API route for logging in a user."""
    data = request.json  # Get login data from the request body
    print("Login attempt:", data)  # Debug print
    
    # Check if the user exists by username
    user = User.query.filter_by(username=data['username']).first()
    print("Found user:", user)  # Debug print
    
    # If user exists and the password matches, return success
    if user and user.password == data['password']:
        return jsonify({'success': True, 'user_id': user.id})
    
    # Specific error messages
    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 401
    return jsonify({'success': False, 'message': 'Invalid password'}), 401

@app.route('/api/check-users', methods=['GET'])
def check_users():
    """API route to get a list of all users."""
    users = User.query.all()  # Fetch all users from the database
    # Return user information as a JSON response
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

@app.route('/api/chat/history', methods=['GET'])
def get_chat_history():
    """API route to get the chat history for a specific user."""
    user_id = request.args.get('user_id')  # Get user ID from query params
    messages = ChatMessage.query.filter_by(user_id=user_id).order_by(ChatMessage.timestamp).all()  # Get all messages for the user
    # Return the chat messages as a JSON response
    return jsonify([{
        'content': msg.content,
        'timestamp': msg.timestamp.isoformat(),  # Convert timestamp to ISO format
        'type': msg.message_type
    } for msg in messages])

@app.route('/api/chat/message', methods=['POST'])
def save_message():
    """API route to save a new chat message."""
    data = request.json  # Get message data from the request body
    message = ChatMessage(
        user_id=data['user_id'],
        content=data['content'],
        message_type=data['type']
    )
    db.session.add(message)  # Add the new message to the database
    db.session.commit()  # Commit the changes
    return jsonify({'success': True})  # Return success response

# Function to initialize the database and add sample data if not already present
def init_db():
    """Initialize the database and add sample data if needed."""
    with app.app_context():
        db.create_all()  # Create all database tables
        
        # Add sample products if no products exist
        if not Product.query.first():
            electronics = [
                {"name": "4K Smart TV", "price": 699.99, "category": "Electronics", "description": "55-inch 4K Ultra HD Smart LED TV", "stock": 50},
                # More electronics products can be added here...
            ]
            # Create product objects from sample data
            products = [Product(**product_data) for product_data in electronics]
            db.session.bulk_save_objects(products)  # Bulk save products for efficiency
        
        # Add a sample user if none exists
        if not User.query.first():
            test_user = User(username='test', password='test123')  # Sample test user
            db.session.add(test_user)
            db.session.commit()

# Run the application
if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(debug=True)  # Start the Flask app in debug mode
