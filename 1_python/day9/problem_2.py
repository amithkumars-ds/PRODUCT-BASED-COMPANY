class Camera:
    def take_photo(self):
        print("Photo captured")

class Phone:
    def make_call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    def use_device(self):
        super().take_photo()
        super().make_call()


if __name__ == "__main__":

    phone = Smartphone()

    # Test inherited methods
    phone.take_photo()
    phone.make_call()

    # Test combined method
    phone.use_device()

    # Test MRO
    print("MRO:", Smartphone.mro())

    # Test show_mro method
    print("Show MRO:", phone.show_mro())
