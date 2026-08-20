from Subscriber import Subscriber
class Analytics(Subscriber):
    def __init__(self, order_id):
        self.order_id = order_id

    def update(self, order):
        print(f"Analytics updated for Order ID: {order.order_id}. Current status: '{order.status}'")