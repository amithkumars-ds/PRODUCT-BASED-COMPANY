def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Starting function...")
        func(*args,**kwargs)
        print("Function completed!")
    return wrapper


@my_decorator
def greet():
    print("Hello!")

@my_decorator
def calculate(a,b):
    print(f"{a}+{b}={a+b}")


if __name__ == "__main__":
    greet()

    print("\n")

    calculate(10,20)
