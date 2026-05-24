const API_BASE = "http://127.0.0.1:5000/api";

async function initiatePayment() {
    const phone = document.getElementById('phone').value;
    const amount = document.getElementById('amount').value;
    const statusMsg = document.getElementById('status-msg');
    const generateBtn = document.getElementById('generateBtn');

    if (!phone || !amount) {
        statusMsg.textContent = "Please enter your phone number and amount.";
        statusMsg.style.color = "#ff5252";
        return;
    }

    statusMsg.style.color = "#00e676";
    statusMsg.textContent = "Sending MoMo prompt to your phone...";

    try {
        const response = await fetch(`${API_BASE}/pay`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ phone_number: phone, amount: parseFloat(amount) })
        });

        const data = await response.json();

        if (data.success) {
            statusMsg.textContent = "MoMo prompt sent! Approve it on your phone, then click below.";
            generateBtn.style.display = "block";
            generateBtn.dataset.userId = phone;
            generateBtn.dataset.amount = amount;
        } else {
            statusMsg.style.color = "#ff5252";
            statusMsg.textContent = "Payment request failed. Try again.";
        }
    } catch (err) {
        statusMsg.style.color = "#ff5252";
        statusMsg.textContent = "Could not reach server. Is Flask running?";
    }
}

async function generateCard() {
    const generateBtn = document.getElementById('generateBtn');
    const statusMsg = document.getElementById('status-msg');
    const userId = generateBtn.dataset.userId;
    const amount = generateBtn.dataset.amount;

    statusMsg.style.color = "#00e676";
    statusMsg.textContent = "Generating your virtual card...";

    try {
        const response = await fetch(`${API_BASE}/card/create`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: userId, amount: parseFloat(amount) })
        });

        const data = await response.json();

        if (data.success) {
            // Format card number with spaces
            const num = data.card_number;
            const formatted = `${num.slice(0,4)} ${num.slice(4,8)} ${num.slice(8,12)} ${num.slice(12,16)}`;

            document.getElementById('cardNumber').textContent = formatted;
            document.getElementById('cardExpiry').textContent = data.expiry;
            document.getElementById('cardCvv').textContent = data.cvv;
            document.getElementById('cardHolder').textContent = "BRIDGEPAY USER";

            statusMsg.textContent = "Your virtual card is ready!";
            generateBtn.style.display = "none";
        } else {
            statusMsg.style.color = "#ff5252";
            statusMsg.textContent = "Card generation failed. Try again.";
        }
    } catch (err) {
        statusMsg.style.color = "#ff5252";
        statusMsg.textContent = "Could not reach server. Is Flask running?";
    }
}