# Abstraction means defining what an object must do without defining exactly how it does it.

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        return f"{message} sent!"


class SMSNotification(Notification):
    def send(self, message):
        return f"{message} sent!"


class WhatsAppNotification(Notification):
    pass



if __name__ == "__main__":
    notifications = [
        EmailNotification(),
        SMSNotification(),
        WhatsAppNotification()
    ]

    for notification in notifications:
        print(notification.send("Hello! This is a test notification."))


