class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * (9/5)) + 32
        return round(fahrenheit, 2) 

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32)*(5/9)
        return round(celsius, 2)



if __name__ == "__main__":
    print(TemperatureConverter.celsius_to_fahrenheit(0))
    print(TemperatureConverter.fahrenheit_to_celsius(32))

