class Camera:
    @staticmethod
    def take_photo():
        return f"Photo captured!"

class Phone:
    @staticmethod
    def make_call(number):
        return f"Calling {number}"

class Smartphone(Camera, Phone):
    @staticmethod
    def browse_internet():
        return f"Browsing internet"



if __name__ == "__main__":
    phone = Smartphone()

    print(phone.take_photo())
    print(phone.make_call("9876543210"))
    print(phone.browse_internet())
