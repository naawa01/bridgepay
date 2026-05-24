from flask import Blueprint, request, jsonify
from services.momo import request_momo_payment
from services.cards import create_virtual_card, lock_card, unlock_card, burn_card, get_card

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/pay', methods=['POST'])
def initiate_payment():
    data = request.get_json()
    phone_number = data.get('phone_number')
    amount = data.get('amount')

    if not phone_number or not amount:
        return jsonify({"success": False, "error": "Phone number and amount are required"}), 400

    result = request_momo_payment(phone_number, amount)
    return jsonify(result)


@payments_bp.route('/card/create', methods=['POST'])
def generate_card():
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    spending_limit = data.get('spending_limit')
    expiry_window = data.get('expiry_window', '24h')
    burn_after_use = data.get('burn_after_use', False)

    if not user_id or not amount:
        return jsonify({"success": False, "error": "user_id and amount are required"}), 400

    result = create_virtual_card(
        user_id=user_id,
        amount=amount,
        spending_limit=spending_limit,
        expiry_window=expiry_window,
        burn_after_use=burn_after_use
    )
    return jsonify(result)


@payments_bp.route('/card/<card_id>/lock', methods=['POST'])
def lock(card_id):
    return jsonify(lock_card(card_id))


@payments_bp.route('/card/<card_id>/unlock', methods=['POST'])
def unlock(card_id):
    return jsonify(unlock_card(card_id))


@payments_bp.route('/card/<card_id>/burn', methods=['POST'])
def burn(card_id):
    return jsonify(burn_card(card_id))


@payments_bp.route('/card/<card_id>', methods=['GET'])
def get(card_id):
    return jsonify(get_card(card_id))

@payments_bp.route('/cards/<user_id>', methods=['GET'])
def get_user_cards(user_id):
    from services.cards import get_user_cards
    return jsonify(get_user_cards(user_id))