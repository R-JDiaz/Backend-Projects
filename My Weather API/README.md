#WEATHER API 

Overview:
 This is a Flask-based program that fetches data from Visual Cross, caches the response using redis, limits the api request using rate limiting, and ensure that the url being passed are correct using urllib encode. The API handles the error gracefully and logs requests safely without exposing sensitive information like api keys.

Features:
- Fetch Data(formatted to get only some datas) by location and optional date ranges
- Caching of API response for faster repeat request and avoid duplicate api requests
- Rate Limiting per IP address using Flask-limiter
- Error handling with JSON responses for time-outs, HTTP errors and unexpected errors
- Logging of request and errors with the api key hidden

Requirements:
Python 3.10+
Flask
requests
Flask-Limiter
Redis (running locally or remote)

Install dependencies:

bash: pip install -r requirements.txt

Getting Started

1. Clone the repository
git clone https://github.com/yourusername/weather-api.git
cd weather-api

2. Set up configuration

Create a .env file:

    WEATHER_API_KEY = "YOUR_API_KEY"
    FLASK_ENV="development"
    LOCATION="YOUR LOCATION"

3. Run Redis

Make sure Redis is running locally on localhost:6379:

redis-server

4. Run the Flask server
python app.py

By default, Flask runs on http://localhost:5000.

Example request:

http://localhost:5000/weather?location=Moscow&date1=2024-10-10&date2=2024-10-15
