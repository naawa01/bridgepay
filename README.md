# BridgePay

**Shop global. Pay with MoMo.**

BridgePay converts Mobile Money into a secure virtual card you can use for any online payment — subscriptions, e-commerce, AI tools, hosting, gaming, freelance platforms. No bank account. No PayPal. Just MoMo.

---

## The Problem

Millions of people across West Africa have Mobile Money wallets and real purchasing power. But most online platforms require a bank card or PayPal — neither of which is accessible to the majority of MoMo users. The result: people are locked out of global digital commerce not because they lack money, but because the infrastructure doesn't connect.

## The Solution

BridgePay sits between Mobile Money and the global card payment network. A user loads funds via MoMo, and BridgePay instantly generates a virtual Visa card they can use anywhere online.

---

## What Makes BridgePay Different

Existing virtual card solutions leave real gaps. BridgePay is built around exactly those gaps:

**1. Security-First Design**
Most virtual cards behave like normal debit cards — always active, no controls. BridgePay gives users:
- Burn-after-use mode — card self-destructs after first transaction
- Lock/unlock — deactivate and reactivate anytime
- Auto-expiry — card lives for 1 hour, 24 hours, 7 days, or 30 days
- Spending limits — set a maximum the card can be charged

**2. Radical Simplicity**
No crypto. No loans. No savings products. No investing. One job: turn your MoMo into a card you can use anywhere online.

**3. Built for West Africa**
Designed around Ghanaian MoMo habits, local trust concerns, and the real frustrations of paying online from Africa. The UI reflects that — warm, grounded, familiar.

**4. User-Controlled Risk**
You decide when your card works, how long it lives, how much it can spend, and when it dies. No surprises. No unauthorized charges.

---

## How It Works

1. User enters their MoMo number and amount to load
2. A MoMo payment prompt is sent to their phone
3. Once confirmed, BridgePay generates a funded virtual Visa card
4. User copies the card details and pays anywhere online
5. User can lock, unlock, or destroy the card at any time
6. If a card is destroyed with remaining balance, user can instantly create a new one

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Database | SQLite via Flask-SQLAlchemy |
| MoMo Collection | Africa's Talking Payments API |
| Virtual Card Issuance | Flutterwave Virtual Cards API |
| Environment | python-dotenv |

---

## Project Structure
bridgepay/
├── frontend/
│   ├── index.html          # Landing page
│   ├── dashboard.html      # Main app interface
│   ├── favicon.svg         # Brand identity
│   └── styles.css          # Legacy styles
├── backend/
│   ├── app.py              # Flask app entry point
│   ├── config.py           # Environment configuration
│   ├── models.py           # SQLite database models
│   ├── routes/
│   │   ├── auth.py         # Authentication routes
│   │   └── payments.py     # Payment and card routes
│   └── services/
│       ├── momo.py         # Africa's Talking MoMo integration
│       └── cards.py        # Virtual card generation
├── .env                    # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
---

## Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/naawa01/bridgepay.git
cd bridgepay
```

**2. Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install flask flask-sqlalchemy python-dotenv requests africastalking
```

**4. Set up environment variables**

Create a `.env` file in the root folder:
FLW_CLIENT_ID=your_flutterwave_client_id
FLW_SECRET_KEY=your_flutterwave_secret_key
FLW_ENCRYPTION_KEY=your_flutterwave_encryption_key
AT_API_KEY=your_africastalking_api_key
AT_USERNAME=sandbox
FLASK_SECRET_KEY=any_random_string
DEBUG=True
**5. Run the app**
```bash
cd backend
FLASK_APP=app.py flask run
```

Open `http://127.0.0.1:5000` in your browser.

---

## Current Status

This is a hackathon MVP built for Next Byte Hacks V2 (June 2026). The core flow is fully functional with sandbox integrations.

**What works:**
- Full MoMo payment request flow
- Virtual card generation with security controls
- Lock, unlock, and destroy card
- Balance recovery after card destruction
- SQLite persistence across sessions

**Production roadmap:**
- Live Flutterwave virtual card issuance (pending business registration)
- Ghana Card API integration for KYC verification
- User authentication and multi-card management
- Transaction history and spending analytics
- Mobile app (React Native)

---

## Built By

**Adam** — self-taught developer and entrepreneur from Prang, Ghana. Building from Weija, Accra.

> *"Existing virtual card solutions still leave gaps in security, user control, simplicity, and localized accessibility. BridgePay is built around those gaps."*

---

## License

MIT