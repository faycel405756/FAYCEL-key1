from flask import Flask, Response
import requests
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

@app.route("/get-key")
def get_key():
    url = "https://sieuthidora.io.vn/br1/hma.php?step=1"
    r = requests.get(url, allow_redirects=True)
    params = parse_qs(urlparse(r.url).query)
    return Response(params["key"][0], mimetype="text/plain")

if __name__ == "__main__":
    app.run()
