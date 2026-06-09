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
@auth_bp.route('/stats', methods=['GET'])
@login_required
def stats():
    from models import Card
    
    cards = Card.query.filter_by(user_id=current_user.id).all()
    
    total_cards = len(cards)
    active_cards = sum(1 for c in cards if c.status == 'active')
    locked_cards = sum(1 for c in cards if c.locked)
    burned_cards = sum(1 for c in cards if c.status == 'burned')
    total_loaded_ghs = sum(c.amount * 14.5 for c in cards)  # approx GHS conversion
    total_loaded_usd = sum(c.amount for c in cards)
    total_remaining_usd = sum(c.remaining_balance for c in cards if c.status == 'active')

    # member for X days
    try:
        joined = datetime.fromisoformat(current_user.created_at)
        days_member = (datetime.now() - joined).days
    except:
        days_member = 0

    return jsonify({
        "success": True,
        "stats": {
            "total_cards": total_cards,
            "active_cards": active_cards,
            "locked_cards": locked_cards,
            "burned_cards": burned_cards,
            "total_loaded_usd": round(total_loaded_usd, 2),
            "total_loaded_ghs": round(total_loaded_ghs, 2),
            "total_remaining_usd": round(total_remaining_usd, 2),
            "days_member": days_member
        }
    })