from RequestHandler import RequestHandler
from datetime import datetime
class Metrics():
    def __init__(self, handler):
        self.handler = handler
        self.last_duration = None
    def handle_request(self, request):

        start_time = datetime.now()

        try:
            return self.handler.handle_request(request)

        finally:
            end_time = datetime.now()

            self.last_duration = (
                end_time - start_time
            ).total_seconds()

            print(f"Request Duration: {self.last_duration} seconds")
    def log_metrics(self):
        # Report the duration measured on the most recent request.
        if self.last_duration is not None:
            print(f"Request Duration: {self.last_duration} seconds")
        else:
            print("Request Duration: Not available (request not completed)")
