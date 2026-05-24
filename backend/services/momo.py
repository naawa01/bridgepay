def request_momo_payment(phone_number, amount, currency="GHS"):
    """
    Mock MoMo payment request.
    In production this sends a real prompt via Africa's Talking.
    """
    try:
        return {
            "success": True,
            "data": {
                "status": "PendingConfirmation",
                "description": f"MoMo prompt sent to {phone_number}",
                "transactionId": f"BP-{phone_number[-4:]}-{int(amount)}",
                "phone": phone_number,
                "amount": amount,
                "currency": currency
            }
        }
    except Exception as e:
        return {"success": False, "error": str(e)}