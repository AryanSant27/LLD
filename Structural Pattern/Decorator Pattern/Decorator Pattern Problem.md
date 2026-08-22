# Decorator Pattern — Interview Problem

# API Request Processing Pipeline

## Problem Statement

You are building a backend API gateway.

Every incoming API request must pass through a configurable set of behaviors such as:

- Authentication
- Rate Limiting
- Caching
- Logging
- Metrics

The system should be designed using the **Decorator Pattern**.

The objective is to dynamically compose these behaviors around a base request handler without modifying the original handler.

---

# Base Interface

Create a common request handler abstraction:

```python
class RequestHandler:

    def handle_request(self, request):
        pass