def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Starting function...")
        try:
            func(*args,**kwargs)
            print("Function completed!")
        except Exception as e:
            print(f"Function failed: {e}")
            raise
        finally:
            print("Function execution ended.")
        print("\n")
    return wrapper


@my_decorator
def divide(a,b):
    print(a/b)



if __name__ == "__main__":
    divide(10,2)
    divide(10,0)
