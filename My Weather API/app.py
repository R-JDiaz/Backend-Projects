from request_data import request_data
from config import Config
from flask import Flask, jsonify, request
from ratelimit import limits

app = Flask(__name__)
HOUR = 3600



@app.route("/weather", methods=["GET"])
def run():
    location = request.args.get("location", Config.location)
    response = request_data(location)
    return jsonify(response)

if  __name__ == "__main__":
    app.run(debug=True)
