from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.String(10), primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
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