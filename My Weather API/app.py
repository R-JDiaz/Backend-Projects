import requests
import json
import redis

r = redis.Redis(host="localhost", port=6379, db=0)

def request(location, date1=None, date2=None):
    BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    API_KEY = "UW9WGNEW2SEFDM82H8H48CELF"

    if date1 and date2:
        #DATE FORMAT = format yyyy-MM-ddTHH:mm:ss. For example 2020-10-19T13:00:00.
        url = f"{BASE_URL}/{location}/{date1}/{date2}?key={API_KEY}"
    elif date1:
        url = f"{BASE_URL}/{location}/{date1}?key={API_KEY}"
    else:
        url = f"{BASE_URL}/{location}/?key={API_KEY}"
    
    cache = r.get(url)
    
    if cache is None:
        try:
            response = requests.get(url)    
            response.raise_for_status()

            data = response.json()
            dict = data
            print(f"API RESPONSE: {dict["resolvedAddress"]}")

            r.set(url, json.dumps(data))

            print("api is working")

        except requests.exceptions.HTTPError as httpError:
            print(f"Http Error: {str(httpError)}")
        except Exception as err:
            print(f"Normal Error: {str(err)}")
    else:
        cache_data = json.loads(cache)
        print(cache_data["resolvedAddress"])
        print("cache is working")


if __name__ == "__main__" :
    location = "Bulacan, Philippines"
    request(location)

