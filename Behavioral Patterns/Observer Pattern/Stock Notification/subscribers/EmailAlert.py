from Subscriber import Subscriber   

class EmailAlert(Subscriber):
    def __init__(self, email):
        self.email = email
    def update(self, stock, old_price, new_price):
        print(f"EmailAlert received update from {stock.__class__.__name__}: Price changed from {old_price} to {new_price}")