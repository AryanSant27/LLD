from NotificationService import NotificationService, send_email_notification, send_sms_notification


class OrderService:
    def __init__(self, order_repository=None):
        self.order_repository = order_repository

    def send_notification(self, order_id):
        send_email_notification.send_notification(f"Order {order_id} has been placed successfully!")
        send_sms_notification.send_notification(f"Order {order_id} has been placed successfully!")


order = OrderService()
order.send_notification("12345")
    