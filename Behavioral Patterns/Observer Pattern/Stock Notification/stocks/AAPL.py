from Publisher import Publisher

class AAPL(Publisher):
    def __init__(self):
        super().__init__()
        self.price = 200