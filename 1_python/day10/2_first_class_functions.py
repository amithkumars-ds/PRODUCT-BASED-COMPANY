def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def calculate(func, a, b):
    return func(a,b)



if __name__ == "__main__":
    print(calculate(add, 2, 3))
    print(calculate(multiply, 2, 3))
