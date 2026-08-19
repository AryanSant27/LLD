from PaymentInterface import PaymentInterface

class PayPalPayment(PaymentInterface):
    def pay(self, amount, PayPal_id):
        print(f"Processing PayPal payment of ${amount} with PayPal ID: {PayPal_id}")
    def refund(self, amount, PayPal_id):
        print(f"Processing PayPal refund of ${amount} to PayPal ID: {PayPal_id}")