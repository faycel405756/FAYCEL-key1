from flask import Flask, jsonify
import requests
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

@app.route("/get-key")
def get_key():
    url = "https://sieuthidora.io.vn/br1/hma.php?step=1"
    r = requests.get(url, allow_redirects=True, timeout=10)

    params = parse_qs(urlparse(r.url).query)

    if "key" not in params:
        return jsonify({"error": "key not found"}), 400

    key_value = params["key"][0]

    return jsonify({
        "key": key_value
    })

if __name__ == "__main__":
    app.run()
