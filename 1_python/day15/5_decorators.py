def repeat(times):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(times):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(times=5)
def greet(name:str):
    print(f"Hello {name}")

if __name__ == "__main__":
    greet("Kumar")
