from RequestHandler import RequestHandler

class Logging():
    def __init__(self, handler):
        self.handler = handler

    def handle_request(self, request):
        # Logging the request is non-critical: if it fails, keep going.
        try:
            self.log_request(request)
        except Exception as e:
            print(f"Error occurred while logging request: {e}")

        # Handling the request IS critical: log the error, then re-raise
        # so the caller isn't handed a silent None.
        try:
            response = self.handler.handle_request(request)
        except Exception as e:
            print(f"Error occurred while handling request: {e}")
            raise

        # Logging the response is non-critical too.
        try:
            self.log_response(response)
        except Exception as e:
            print(f"Error occurred while logging response: {e}")

        return response

    def log_request(self, request):
        # Log the incoming request details
        print(f"Logging Request: {request}")
    def log_response(self, response):
        # Log the outgoing response details
        print(f"Logging Response: {response}")
