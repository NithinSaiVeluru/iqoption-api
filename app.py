from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "Trading API is running"})

@app.route("/trade", methods=["POST"])
def trade():
    data = request.get_json()
    if not data or "signal" not in data:
        return jsonify({"error": "Missing 'signal'"}), 400
    
    signal = data["signal"].lower()
    print(f"🚀 Received trade signal: {signal}")

    return jsonify({
        "status": "success",
        "received_signal": signal,
        "message": f"Executed {signal} trade (simulation for now)"
    })
