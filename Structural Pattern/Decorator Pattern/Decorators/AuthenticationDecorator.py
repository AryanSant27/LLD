from RequestHandler import RequestHandler

class Authentication():
    def __init__(self, handler, valid_token="valid_token"):
        self.handler = handler
        self.valid_token = valid_token

    def handle_request(self, request):
        try:
            self.authenticate(request)
        except Exception as e:
            print(f"Authentication failed: {e}")
            raise
        return self.handler.handle_request(request)
    def authenticate(self, request):
        # Placeholder for authentication logic
        if request.token != self.valid_token:
            raise Exception("Invalid token. Authentication failed.")
        request.authenticated = True