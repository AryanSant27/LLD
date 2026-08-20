from abc import ABC, abstractmethod

class Publisher(ABC):
    @abstractmethod
    def __init__(self, symbol, price):
        self.subscribers = []
    @abstractmethod
    def notify_subscribers(self, old_price, new_price):
        for subscriber in self.subscribers:
            subscriber.update(self, old_price, new_price)
    @abstractmethod       
    def set_price(self, price):
        old_price = self.price
        self.price = price
        self.notify_subscribers(old_price, self.price)
    @abstractmethod    
    def add_subscriber(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
    @abstractmethod
    def remove_subscriber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)