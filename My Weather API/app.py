from flask import Flask
from request_data import request_data
app = Flask(__name__)

@app.route("/weather")
def run(location):
    location = "Manila, Philippines"
    return request_data(location)

if __name__ == "__main__" :
    app.run(debug=True)

 