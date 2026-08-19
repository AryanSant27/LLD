from PaymentProcessor import PaymentProcessor

if __name__ == "__main__":
    payment = PaymentProcessor().create("CreditCard")
    payment.pay(100, "1234-5678-9012-3456")
    