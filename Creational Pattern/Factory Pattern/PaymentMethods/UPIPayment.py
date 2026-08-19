from PaymentInterface import PaymentInterface

class UPIPayment(PaymentInterface):
    def pay(self, amount, upi_id):
        print(f"Processing UPI payment of ${amount} with UPI ID: {upi_id}")
    def refund(self, amount, upi_id):
        print(f"Processing UPI refund of ${amount} to UPI ID: {upi_id}")