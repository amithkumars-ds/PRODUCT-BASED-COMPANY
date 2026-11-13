class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine_obj:Engine=None):        
        if engine_obj:
            self.engine = engine_obj
        else:
            self.engine = Engine()

    def start_car(self):
        return self.engine.start()


if __name__ == "__main__":
    # Basic composition test
    car = Car()
    print(car.start_car())

    # Bonus: inject an existing Engine object
    engine = Engine()
    car2 = Car(engine)
    print(car2.start_car())

    # Verify both cars use the same engine instance
    print(car2.engine is engine)
