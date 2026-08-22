from RequestHandler import RequestHandler, user, request

from Decorators.AuthenticationDecorator import Authentication
from Decorators.RateLimiterDecorator import RateLimiter
from Decorators.CachingDecorator import Caching
from Decorators.LoggingDecorator import Logging
from Decorators.MetricsDecorator import Metrics


# -------------------------
# Create base objects
# -------------------------

user = user(
    user_id=1,
    username="Alice"
)

request = request(
    token="valid_token",
    user=user
)


# -------------------------
# Create base handler
# -------------------------

handler = RequestHandler()


# -------------------------
# Wrap the handler
# -------------------------

handler = Authentication(handler)

handler = RateLimiter(handler)

handler = Caching(handler)

handler = Metrics(handler)

handler = Logging(handler)


# -------------------------
# Execute
# -------------------------

response = handler.handle_request(request)

print("\nFinal response:")
print(response)