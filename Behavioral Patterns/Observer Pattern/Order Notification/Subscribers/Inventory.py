from Subscriber import Subscriber
class Inventory(Subscriber):
    def __init__(self, order_id):
        self.order_id = order_id

    def update(self, order):
        if order.status == "PLACED":
            print(f"Inventory updated for Order ID: {order.order_id}. Items are being prepared for shipment.")
        if order.status == "CANCELLED":
            print(f"Inventory updated for Order ID: {order.order_id}. Items are being restocked.")