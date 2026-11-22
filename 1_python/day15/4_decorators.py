import time
from functools import wraps
from time import perf_counter

def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("[INFO] Starting Function Execution...")
        print("Function Details","\n")
        print("-"*50)

        print(f"Name: {func.__name__}")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")

        start_time = perf_counter()

        try:
            result = func(*args,**kwargs)
            print("[SUCCESS] Function Execution completed successfully!")

            return result

        except Exception as e:
            print(f"[FAILURE] Function Execution Failed due to: {e}!")
            raise
        
        finally:            
            end_time = perf_counter()
            execution_time = end_time - start_time

            print(f"[INFO] Execution completed in {round(execution_time,2)}")
            print("[INFO] Function Execution ended.")


    return wrapper


@my_decorator
def fetch_user(user_id):
    time.sleep(2)
    return {"user_id": user_id, "name": "Kumar"}


@my_decorator
def process_payment(amount, currency="INR"):
    time.sleep(1)

    if amount <= 0:
        raise ValueError("Invalid payment amount")

    return {"amount": amount, "currency": currency}


@my_decorator
def calculate_total(price, quantity):
    time.sleep(0.5)
    return price * quantity


if __name__ == "__main__":

    print("\n--- Test 1: Successful API call ---")
    user = fetch_user(101)
    print("Returned:", user)

    print("\n--- Test 2: Successful payment ---")
    payment = process_payment(5000, currency="INR")
    print("Returned:", payment)

    print("\n--- Test 3: Failed payment ---")
    try:
        process_payment(-100)
    except ValueError as e:
        print("Caller caught:", e)

    print("\n--- Test 4: Different function ---")
    total = calculate_total(250, 4)
    print("Returned:", total)

    print("\n--- Test 5: Metadata ---")
    print("Function name:", fetch_user.__name__)

