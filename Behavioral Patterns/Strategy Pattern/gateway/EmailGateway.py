class EmailGateway:
    def send_email(self, message, email_provider):
        print(f"sending email: {message} using {email_provider} provider")