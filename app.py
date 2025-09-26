from flask import Flask, request, jsonify
from iqoptionapi.stable_api import IQ_Option
import time

app = Flask(__name__)

# Demo credentials
EMAIL = "vkonda1972@gmail.com"
PASSWORD = ""

@app.route("/trade", methods=["POST"])
def trade():
    data = request.get_json()
    if not data or "signal" not in data or "pair" not in data:
        return jsonify({"error": "Missing 'signal' or 'pair'"}), 400

    signal = data["signal"].lower()
    pair = data["pair"].upper()
    print(f"🚀 Received trade signal: {signal} for {pair}")

    I_want_money = IQ_Option(EMAIL, PASSWORD)
    I_want_money.connect()
    I_want_money.change_balance("PRACTICE")  # demo account

    amount = 1  # $1 demo trade
    duration = 1  # 1-minute option

    success = False
    order_id = None

    if signal == "buy":
        success, order_id = I_want_money.buy(amount, pair, duration, "call")
    elif signal == "sell":
        success, order_id = I_want_money.buy(amount, pair, duration, "put")
    else:
        return jsonify({"error": "Signal must be 'buy' or 'sell'"}), 400

    message = f"Executed {signal} trade on {pair}, order id: {order_id}" if success else "Trade failed"
    return jsonify({"status": "success" if success else "fail", "message": message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

