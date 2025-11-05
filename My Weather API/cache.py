from redis import Redis
from config import Config
r = Redis(Config.redis_host, Config.redis_port, Config.redis_db)

def get_cache(url):
    return r.get(url)

def set_cache(url, data, exp=None):
    if exp is None:
        r.set(url, data)
        return 'succesfully saved in cache'
    elif isinstance(exp, int):
        r.set(url, data, ex=exp)
        return 'succesfully saved in cache w/ exp'
    else:
        return("Unable to process Non-numeric data for expiration")
    