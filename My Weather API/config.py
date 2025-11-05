import os
from dotenv import load_dotenv

load_dotenv()
class Config():
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    API_BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    redis_host = "localhost"
    redis_port = 6379
    redis_db = 0
