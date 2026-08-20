from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, stock, old_price, new_price):
        pass         