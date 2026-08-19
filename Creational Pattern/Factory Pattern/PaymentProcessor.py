from PaymentMethods.CreditCardPayment import CreditCardPayment
from PaymentMethods.UPIPayment import UPIPayment
from PaymentMethods.PayPalPayment import PayPalPayment

class PaymentProcessor:
    def create(self, payment_method):
        if payment_method == "CreditCard":
            return CreditCardPayment()
        elif payment_method == "UPI":
            return UPIPayment()
        elif payment_method == "PayPal":
            return PayPalPayment()
        else:
            raise ValueError("Invalid payment method")