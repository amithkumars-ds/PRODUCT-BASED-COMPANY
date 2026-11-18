# Function approach
def create_tax_calculator(rate):
    if rate <= 0:
        raise ValueError("Invalid ROI!")
    def calculate_tax(amount):
        return rate*amount

    return calculate_tax


# OOP approach
class TaxCalculator:
    def __init__(self, rate):
        if rate <= 0:
            raise ValueError("Invalid ROI!")
        self.rate = rate

    def calculate_tax(self, amount):
        tax = self.rate * amount
        return tax

if __name__ == "__main__":
    # function approach
    india_tax_calculator = create_tax_calculator(0.18)
    india_tax = india_tax_calculator(10000)
    us_tax_calculator  = create_tax_calculator(0.08)
    us_tax = us_tax_calculator(10000)


    print(f"Tax to pay in India: {india_tax}")
    print(f"Tax to pay in US: {us_tax}")


    # OOP approach
    india_tax_calculator = TaxCalculator(0.18)
    india_tax = india_tax_calculator.calculate_tax(10000)
    us_tax_calculator  = TaxCalculator(0.08)
    us_tax = us_tax_calculator.calculate_tax(10000)


    print(f"Tax to pay in India: {india_tax}")
    print(f"Tax to pay in US: {us_tax}")

