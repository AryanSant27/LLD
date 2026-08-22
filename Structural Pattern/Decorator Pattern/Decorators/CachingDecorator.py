from RequestHandler import RequestHandler
import json

CACHE_FILE = 'cache_file.json'

class Caching():
    def __init__(self, handler):
        self.handler = handler

    def handle_request(self, request):
        cached_response = self.get_cached_response(request)
        if cached_response:
            print("Returning cached response.")
            return cached_response

        response = self.handler.handle_request(request)
        self.cache_response(request, response)
        return response

    def get_cached_response(self, request):
        try:
            with open(CACHE_FILE, 'r') as cache_file:
                cache_data = json.load(cache_file)
                return cache_data.get(request.request_id)
        except FileNotFoundError:
            return None

    def cache_response(self, request, response):
        try:
            with open(CACHE_FILE, 'r') as cache_file:
                cache_data = json.load(cache_file)
        except FileNotFoundError:
            cache_data = {}
        cache_data[request.request_id] = response
        with open(CACHE_FILE, 'w') as cache_file:
            json.dump(cache_data, cache_file, indent=4)
