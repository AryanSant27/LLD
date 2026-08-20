from Subscriber import Subscriber

class MobileApp(Subscriber):
    def __init__(self, user_id):
        self.user_id = user_id
    
    def update(self, stock, old_price, new_price):
        print(f"MobileApp received update from {stock.__class__.__name__}: Price changed from {old_price} to {new_price}")