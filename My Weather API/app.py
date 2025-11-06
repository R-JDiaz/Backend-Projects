from request_data import request_data
from config import Config
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from logger import setup_logger
app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="redis://localhost:6379"
)

logger = setup_logger(Config.log_file, Config.log_type)

@app.route("/weather")
@limiter.limit("3 per minute")
def run():
    location = request.args.get("location", Config.location)
    response = request_data(location)
    return jsonify(response)

@app.errorhandler(429)
def ratelimit_handler(e):
    logger.warning(f"LIMIT REACHED: {jsonify(error={e})}")
    return jsonify(error={e}), 429

if  __name__ == "__main__":
    app.run(debug=True)
