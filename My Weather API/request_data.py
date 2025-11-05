import requests
from config import Config
import cache
from format import format_data
import json
import traceback

def request_data(location, date1=None, date2=None):
    if date1 and date2:
        url = f"{Config.API_BASE_URL}/{location}/{date1}/{date2}?key={Config.WEATHER_API_KEY}"
    elif date1:
        url = f"{Config.API_BASE_URL}/{location}/{date1}?key={Config.WEATHER_API_KEY}"
    else:
        url = f"{Config.API_BASE_URL}/{location}?key={Config.WEATHER_API_KEY}"
        print(url)

    
    cached_data = cache.get_cache(url)
    print("cached: " , cached_data)
    if cached_data is None:
        try:
            response = format_data(requests.get(url).json())
            print(cache.set_cache(url, json.dumps(response)))
            print(url)
            print(response)
            print("DATA FROM API SERVER")
        except requests.exceptions.HTTPError as httpError:
            print(f"HTTP ERROR: {httpError}")
        except Exception as error:
            print(f"Error: {error}")
            traceback.print_exc()
    else:
        print("DATA FROM CACHE")
        print(cached_data)

if __name__ == "__main__":
    location = "Pandi, Philippines"
    request_data(location)
