from request_data import request_data
from config import Config
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
HOUR = 3600

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

@app.route("/weather", methods=["GET"])
def run():
    location = request.args.get("location", Config.location)
    response = request_data(location)
    return jsonify(response)

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="Too many requests, try again later"), 429

if  __name__ == "__main__":
    app.run(debug=True)
