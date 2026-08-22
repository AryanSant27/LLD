from RequestHandler import RequestHandler

class RateLimiter():
    def __init__(self, handler, max_requests=5):
        self.handler = handler
        self.max_requests = max_requests

    def handle_request(self, request):
        try:
            self.check_rate_limit(request)
        except Exception as e:
            print(f"Rate limit exceeded: {e}")
            raise
        return self.handler.handle_request(request)

    def check_rate_limit(self, request):
        # Placeholder for rate limiting logic
        if request.request_count >= self.max_requests:
            raise Exception("Rate limit exceeded. Please try again later.")
        request.request_count += 1