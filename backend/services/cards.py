import random
import string
from datetime import datetime, timedelta
from models import db, Card

EXPIRY_OPTIONS = {
    "1h": 1/24,
    "24h": 1,
    "7d": 7,
    "30d": 30
}

def generate_card_number():
    return f"4{''.join(random.choices(string.digits, k=15))}"

def generate_cvv():
    return ''.join(random.choices(string.digits, k=3))

def generate_expiry(days):
    expiry = datetime.now() + timedelta(days=days)
    return expiry.strftime("%m/%Y")

def create_virtual_card(user_id, amount, currency="USD", spending_limit=None, expiry_window="24h", burn_after_use=False):
    try:
        days = EXPIRY_OPTIONS.get(expiry_window, 1)
        card_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        card = Card(
            id=card_id,
            user_id=user_id,
            card_number=generate_card_number(),
            cvv=generate_cvv(),
            expiry=generate_expiry(days),
            amount=amount,
            remaining_balance=amount,
            currency=currency,
            billing_name=f"BridgePay User {user_id}",
            status="active",
            locked=False,
            burn_after_use=burn_after_use,
            spending_limit=spending_limit if spending_limit else amount,
            expiry_window=expiry_window,
            created_at=datetime.now().isoformat()
        )

        db.session.add(card)
        db.session.commit()
        return card.to_dict()

    except Exception as e:
        db.session.rollback()
        return {"success": False, "error": str(e)}


def lock_card(card_id):
    card = Card.query.get(card_id)
    if not card:
        return {"success": False, "error": "Card not found"}
    card.locked = True
    card.status = "locked"
    db.session.commit()
    return {"success": True, "card_id": card_id, "status": "locked"}


def unlock_card(card_id):
    card = Card.query.get(card_id)
    if not card:
        return {"success": False, "error": "Card not found"}
    card.locked = False
    card.status = "active"
    db.session.commit()
    return {"success": True, "card_id": card_id, "status": "active"}


def burn_card(card_id):
    card = Card.query.get(card_id)
    if not card:
        return {"success": False, "error": "Card not found"}
    card.status = "burned"
    card.locked = True
    db.session.commit()
    return {"success": True, "card_id": card_id, "status": "burned", "remaining_balance": card.remaining_balance}


def get_card(card_id):
    card = Card.query.get(card_id)
    if not card:
        return {"success": False, "error": "Card not found"}
    return {"success": True, "data": card.to_dict()}


def get_user_cards(user_id):
    cards = Card.query.filter_by(user_id=user_id).order_by(Card.created_at.desc()).all()
    return {"success": True, "cards": [c.to_dict() for c in cards]}