from decimal import Decimal
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Credit card payment successful!")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print("UPI payment successful!")

class PaymentProcessor:
    def __init__(self, payment_obj:Payment):
        self.__payment = payment_obj

    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError(f"Invalid amount: {amount}")

    def process(self, amount):
        self._validate_amount(amount)
        self.__payment.process_payment(amount)







if __name__ == "__main__":

    # Test Credit Card Payment
    credit_card = CreditCardPayment()
    processor1 = PaymentProcessor(credit_card)

    print("Testing Credit Card Payment:")
    processor1.process(Decimal("1500.00"))

    print("\n" + "-" * 40 + "\n")

    # Test UPI Payment
    upi = UPIPayment()
    processor2 = PaymentProcessor(upi)

    print("Testing UPI Payment:")
    processor2.process(Decimal("2500.00"))

    print("\n" + "-" * 40 + "\n")

    # Test polymorphism
    payment_methods = [
        CreditCardPayment(),
        UPIPayment()
    ]

    for payment in payment_methods:
        processor = PaymentProcessor(payment)
        processor.process(Decimal("500.00"))
