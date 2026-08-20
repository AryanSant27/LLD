from Subscriber import Subscriber

class Customer(Subscriber):
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
    def update(self, order):
        print(f"Customer {self.name} (ID: {self.customer_id}) notified about Order ID: {order.order_id} status change to '{order.status}'")
        self.email_notification(order)
        self.sms_notification(order)
        self.push_notification(order)
        
    def email_notification(self, order):
        print(f"Email sent to Customer {self.name} (ID: {self.customer_id}) regarding Order ID: {order.order_id} status change to '{order.status}'")
    def sms_notification(self, order):
        print(f"SMS sent to Customer {self.name} (ID: {self.customer_id}) regarding Order ID: {order.order_id} status change to '{order.status}'")
    def push_notification(self, order):
        print(f"Push notification sent to Customer {self.name} (ID: {self.customer_id}) regarding Order ID: {order.order_id} status change to '{order.status}'")