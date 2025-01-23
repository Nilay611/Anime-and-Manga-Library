from functools import wraps
from flask import jsonify
from . import redis_client
import json

def cache_response(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        cache_key = f.__name__
        cached_data = redis_client.get(cache_key)
        
        if cached_data:
            return jsonify(json.loads(cached_data))
        
        response = f(*args, **kwargs)
        redis_client.setex(cache_key, 300, json.dumps(response.get_json()))  # Cache for 5 minutes
        return response
        
    return wrapper
