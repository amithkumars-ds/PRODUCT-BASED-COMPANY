def repeat(times):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                print("Before execution")
                func(*args, **kwargs)
                print("After execution")

        return wrapper
    return my_decorator


@repeat(times=3)
def greet(name):
    print(f"Hello {name}!")


greet("Kumar")
