from gateway.EmailGateway import EmailGateway
from notification_strategy import NotificationStrategy


class EmailNotification(NotificationStrategy):
    def __init__(self, email_gateway: EmailGateway, email_provider):
        self.email_gateway = email_gateway
        self.email_provider = email_provider

    def send(self, message):
        self.email_gateway.send_email(message, self.email_provider)