from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass