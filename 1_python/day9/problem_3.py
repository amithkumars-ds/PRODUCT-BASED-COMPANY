class Engine:
    def start(self):
        print("Engine started")

class Car():
    def __init__(self, engine_obj:Engine=None):
        self.engine = engine_obj if engine_obj is not None else Engine()

    def start_car(self):
        self.engine.start()




if __name__ == "__main__":

    # Test default engine creation
    car1 = Car()
    print("Testing default engine:")
    car1.start_car()

    print("-" * 40)

    # Test dependency injection
    engine = Engine()
    car2 = Car(engine)
    print("Testing injected engine:")
    car2.start_car()

    print("-" * 40)

    # Test different engine implementation
    class ElectricEngine:
        def start(self):
            print("Electric engine started silently!")

    electric_engine = ElectricEngine()
    car3 = Car(electric_engine)

    print("Testing electric engine:")
    car3.start_car()
