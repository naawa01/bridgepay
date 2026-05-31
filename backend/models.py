from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(256), nullable=False)
    full_name = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.String(30))
    cards = db.relationship('Card', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "email": self.email,
            "full_name": self.full_name,
            "created_at": self.created_at
        }


class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.String(10), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_number = db.Column(db.String(20), nullable=False)
    cvv = db.Column(db.String(3), nullable=False)
    expiry = db.Column(db.String(10), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    remaining_balance = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(5), default='USD')
    billing_name = db.Column(db.String(100))
    status = db.Column(db.String(20), default='active')
    locked = db.Column(db.Boolean, default=False)
    burn_after_use = db.Column(db.Boolean, default=False)
    spending_limit = db.Column(db.Float)
    expiry_window = db.Column(db.String(5), default='24h')
    created_at = db.Column(db.String(30))

    def to_dict(self):
        return {
            "success": True,
            "card_id": self.id,
            "card_number": self.card_number,
            "cvv": self.cvv,
            "expiry": self.expiry,
            "amount": self.amount,
            "remaining_balance": self.remaining_balance,
            "currency": self.currency,
            "billing_name": self.billing_name,
            "status": self.status,
            "locked": self.locked,
            "burn_after_use": self.burn_after_use,
            "spending_limit": self.spending_limit,
            "expiry_window": self.expiry_window,
            "created_at": self.created_at
        }