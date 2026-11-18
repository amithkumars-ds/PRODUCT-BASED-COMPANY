from functools import wraps

def log_execution(func):
    @wraps(func)
    def execute(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")
        
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Execution Failed: {e}")
            raise
        
        print("Execution Successful!")

        return result
    return execute


@log_execution
def create_user(name, email):
    return f"User {name} created with email {email}"


@log_execution
def calculate_salary(basic, bonus=0):
    return basic + bonus


@log_execution
def process_payment(amount, currency="INR"):
    return f"Payment of {currency} {amount} processed"

@log_execution
def divide(a, b):
    return a / b



if __name__ == "__main__":
    user = create_user("Kumar", "kumar@example.com")
    print("Result:", user)

    print("---")

    salary = calculate_salary(50000, bonus=10000)
    print("Result:", salary)

    print("---")

    payment = process_payment(5000)
    print("Result:", payment)

    print(divide(10, 2))
    print(divide(10, 0))
