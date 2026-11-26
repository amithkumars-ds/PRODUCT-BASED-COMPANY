import time

def retry(times:int):
    def my_decorator(func):
        def wrapper(*args,**kwargs):
            last_error = None
            for t in range(times):
                try:
                    result = func(*args,**kwargs)
                    return result
                except Exception as e:
                    print("Connection failed")
                    last_error = e
                if t < times - 1:
                    time.sleep(2**t)
            raise last_error

        return wrapper
    return my_decorator

@retry(times=4)
def api_call():
    print("Calling api")



attempt_counter = 0

@retry(times=4)
def api_success():
    global attempt_counter
    attempt_counter += 1

    print(f"API attempt {attempt_counter}")

    if attempt_counter < 3:
        raise ConnectionError("Temporary API failure")

    return {"status": "success", "data": [10, 20, 30]}


@retry(times=4)
def api_failure():
    print("Calling unavailable API...")
    raise ConnectionError("Server unavailable")


if __name__ == "__main__":

    print("\n--- TEST 1: Eventually succeeds ---")
    result = api_success()
    print("Final result:", result)

    print("\n--- TEST 2: All attempts fail ---")
    try:
        api_failure()
    except ConnectionError as e:
        print("Final exception:", e)

