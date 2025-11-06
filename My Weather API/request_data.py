import requests
from config import Config
import cache
from format import format_data
import json
import logging 

logger = logging.getLogger(__name__)

def request_data(location, date1=None, date2=None):
    url=f"{Config.API_BASE_URL}/{location}"
    params = {"key" : Config.WEATHER_API_KEY}
    if date1 and date2:
        params["date1"] = date1
        params["date2"] = date2
    elif date1:
        params["date1"] = date1
    
    req = requests.Request('GET', url, params=params)
    prepared = req.prepare()
    full_url = prepared.url

    cached_data = cache.get_cache(full_url)
    if cached_data is None:
        try:
            response1 = requests.get(full_url, timeout=5)
            response1.raise_for_status()
            response = format_data(response1.json())
            logger.info(str(cache.set_cache(full_url, json.dumps(response))))
            return response
        
        except requests.exceptions.Timeout as e:
            logger.error(f"API takes too long {e}")
            raise
        except requests.exceptions.HTTPError as httpError:
            logger.error(f"HTTP ERROR: {httpError}")
            raise
        except Exception as error:
            logger.error(f"Other Error: {error}", exc_info=True)
            raise
    else:
        if isinstance(cached_data, bytes):
            cached_data = cached_data.decode("utf-8")
        logger.info(f"data from cache")
        return json.loads(cached_data)

if __name__ == "__main__":
    location = "Pandi, Philippines"
    request_data(location)
