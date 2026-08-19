from PaymentInterface import PaymentInterface

class CreditCardPayment(PaymentInterface):
    def pay(self, amount, saved_card_info):
        print(f"Processing credit card payment of ${amount} with saved card info: {saved_card_info}")
    
    def refund(self, amount, saved_card_info):
        print(f"Processing credit card refund of ${amount} to saved card info: {saved_card_info}")