from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_URL = "https://ocg8ffld8exwb.com/ResultService/mobile/api/v2/games"

@app.route("/api/predict", methods=["GET"])
def proxy_api():
    params = {
        "country": "96",
        "Gr": "1357",
        "Lng": "fr_FR",
        "Ref": "1",
        "ChampIds": "2627439",
        "DateFrom": "1759881600",
        "DateTo": "1759967999",
        "CyberType": "1"
    }
    try:
        r = requests.get(API_URL, params=params, timeout=10)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return {"status": "Proxy API FC24 Penalty online"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
