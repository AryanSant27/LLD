from gateway import EmailGateway, SMSGateway
from notifications.EmailNotification import EmailNotification
from notifications.SMSNotification import SMSNotification


class NotificationService:
    def __init__(self, notification_strategy):
        self.notification_strategy = notification_strategy

    def send_notification(self, message):
        self.notification_strategy.send(message)
    

send_email_notification = NotificationService(EmailNotification(EmailGateway(), "SMTP"))
send_sms_notification = NotificationService(SMSNotification(SMSGateway()))




