class Order:
    def __init__(self, order_id, customer_id, status):
        self.order_id = order_id
        self.customer_id = customer_id
        self.status = status
        self.subscribers = []
        self.notify()
    def change_status(self, new_status):
        self.status = new_status
        self.notify()
    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self)
    def add_subscriber(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)