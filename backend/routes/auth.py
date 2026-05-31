from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    full_name = data.get('full_name')
    phone = data.get('phone')
    email = data.get('email')
    password = data.get('password')

    if not phone or not password:
        return jsonify({"success": False, "error": "Phone and password are required"}), 400

    if User.query.filter_by(phone=phone).first():
        return jsonify({"success": False, "error": "Phone number already registered"}), 400

    user = User(
        phone=phone,
        email=email,
        full_name=full_name,
        created_at=datetime.now().isoformat()
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    login_user(user)
    return jsonify({"success": True, "user": user.to_dict()})


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')

    user = User.query.filter_by(phone=phone).first()

    if not user or not user.check_password(password):
        return jsonify({"success": False, "error": "Invalid phone number or password"}), 401

    login_user(user)
    return jsonify({"success": True, "user": user.to_dict()})


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"success": True})


@auth_bp.route('/me', methods=['GET'])
@login_required
def me():
    return jsonify({"success": True, "user": current_user.to_dict()})