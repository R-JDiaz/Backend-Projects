from request_data import request_data
from config import Config
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from logger import setup_logger
from urllib.parse import quote
import requests

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
    try:
        location = request.args.get("location", Config.location)
        date1 = request.args.get("date1", None)
        date2 = request.args.get("date2", None)
        response = request_data(location,date1,date2)
        return jsonify(response)
    except requests.exceptions.Timeout as e:
        return jsonify({"error": "Request timed out"}), 504
    except requests.exceptions.HTTPError as httpError:
        return jsonify({"error": f"HTTP error {e.response.status_code}"}), 400
    except Exception as error:
        return jsonify({"error": "Unexpected error"}), 500


@app.errorhandler(429)
def ratelimit_handler(e):
    logger.warning(f"LIMIT REACHED: {e}")
    return f"error = {str(e)}", 429

if  __name__ == "__main__":
    app.run(debug=True)
