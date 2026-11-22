from functools import wraps

def retry(times:int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            last_error = None
            for attempt in range(times):
                try:
                    result = func(*args,**kwargs)
                    print(f"Connection successful!")
                    return result

                except Exception as e:
                    last_error = e
                    print(f"Attempt {attempt+1} failed: {e}")
            raise last_error
        return wrapper
    return decorator



attempt_counter = 0


@retry(times=3)
def fetch_data():
    global attempt_counter
    attempt_counter += 1

    print(f"Fetching data... Attempt {attempt_counter}")

    if attempt_counter < 3:
        raise ConnectionError("API connection failed")

    return {"status": "success", "data": [10, 20, 30]}


@retry(times=3)
def permanent_failure():
    print("Connecting to API...")
    raise ConnectionError("Server unavailable")


if __name__ == "__main__":

    print("\n--- Test 1: Eventually succeeds ---")
    result = fetch_data()
    print("Result:", result)

    print("\n--- Test 2: All attempts fail ---")
    try:
        permanent_failure()
    except ConnectionError as e:
        print("Final exception:", e)

    
