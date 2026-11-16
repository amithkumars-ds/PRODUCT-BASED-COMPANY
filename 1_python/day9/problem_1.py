from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Message: {message} sent!")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS: {message} sent!")



if __name__ == "__main__":

    # Test EmailNotification
    email = EmailNotification()
    email.send("Your order has been shipped!")

    # Test SMSNotification
    sms = SMSNotification()
    sms.send("Your OTP is 123456")

    # Test abstract class instantiation
    try:
        notification = Notification()
    except TypeError as e:
        print("Abstract Class Error:", e)

    # Test incomplete child class
    class PushNotification(Notification):
        pass

    try:
        push = PushNotification()
    except TypeError as e:
        print("Incomplete Implementation Error:", e)
