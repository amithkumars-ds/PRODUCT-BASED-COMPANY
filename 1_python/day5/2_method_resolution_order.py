class Camera:
    def start(self):
        return "Camera Started"

class Phone:
    def start(self):
        return "Phone Started"

class Smartphone(Camera, Phone):
    pass

class Smartphone2(Phone, Camera):
    pass



if __name__ == "__main__":
    phone = Smartphone()
    print(phone.start())
    print(Smartphone.mro())
        
    phone2 = Smartphone2()
    print(phone2.start())
    print(Smartphone2.mro())

