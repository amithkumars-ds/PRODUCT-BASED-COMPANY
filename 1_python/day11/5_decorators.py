from functools import wraps

def wrapper(func):
    @wraps(func)
    def execute(*args, **kwargs):
        print("Starting operation...")
        result = func(*args, **kwargs)
        print("Operation completed...")

        return result

    return execute


@wrapper
def add(a, b):
    print(f"Sum: {a + b}")


@wrapper
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


@wrapper
def process_payment(amount, currency="INR"):
    print(f"Processing {currency} {amount}")


if __name__ == "__main__":
    add(10, 20)
    print("---")
    greet("Kumar")
    print("---")
    greet("Kumar", greeting="Welcome")
    print("---")
    process_payment(5000, currency="INR")


    print("\nMetadata Details")
    print("-"*50)
    print(add.__name__)
    print(greet.__name__)
    print(process_payment.__name__)
