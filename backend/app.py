from flask import Flask, send_from_directory
from flask_login import LoginManager
from flask_login import current_user
from flask import redirect, url_for
from config import Config
from models import db, User
import os

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bridgepay.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login_page'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from routes.payments import payments_bp
from routes.auth import auth_bp

app.register_blueprint(payments_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')

@app.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated:
        return redirect('/login')
    return send_from_directory(FRONTEND_DIR, 'dashboard.html')

@app.route('/login')
def login_page():
    return send_from_directory(FRONTEND_DIR, 'login.html')

@app.route('/signup')
def signup_page():
    return send_from_directory(FRONTEND_DIR, 'signup.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

with app.app_context():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])