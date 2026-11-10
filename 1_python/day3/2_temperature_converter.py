class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = 1.8*celsius+32
        return round(fahrenheit, 2)



if __name__ == "__main__":
    print(TemperatureConverter.celsius_to_fahrenheit(0))
    print(TemperatureConverter.celsius_to_fahrenheit(100))
