from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"[INFO] Starting to execute function: {func.__name__}")

        try:
            print(f"[INFO] Arguments: {args}")
            print(f"[INFO] Keyword Arguments: {kwargs}")

            result = func(*args,**kwargs)

            print(f"[INFO] Function executed successfully!")

            return result

        except Exception as e:
            print(f"[ERROR] Function execution failed due to: {e}")
            raise

        finally:
            print("[INFO] Function execution ended.")

    return wrapper



@my_decorator
def create_user(name, role="user"):
    print(f"Creating {name} as {role}")


@my_decorator
def calculate_salary(basic, bonus):
    return basic + bonus


@my_decorator
def divide(a, b):
    return a / b


if __name__ == "__main__":

    print("\n--- Test 1: Positional and keyword arguments ---")
    create_user("Kumar", role="admin")

    print("\n--- Test 2: Positional arguments ---")
    salary = calculate_salary(50000, 10000)
    print(f"Salary: {salary}")

    print("\n--- Test 3: Function failure ---")
    try:
        divide(10, 0)
    except ZeroDivisionError:
        print("Exception caught by caller.")

    print("\n--- Test 4: Metadata Integrity ---")
    print(calculate_salary.__name__)
    print(calculate_salary.__doc__)
    print(calculate_salary.__wrapped__)
