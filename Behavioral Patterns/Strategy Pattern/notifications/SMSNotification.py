from gateway.SMSGateway import SMSGateway
from notification_strategy import NotificationStrategy


class SMSNotification(NotificationStrategy):
    def __init__(self, sms_gateway: SMSGateway):
        self.sms_gateway = sms_gateway

    def send(self, message):
        self.sms_gateway.send_sms(message)