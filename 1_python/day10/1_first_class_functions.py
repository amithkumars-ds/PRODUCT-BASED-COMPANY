def greet():
    print("Hello there!")

greeting_new = greet
greeting = greeting_new()

def execute_fn(func):
    func()

execute_fn(greeting_new)
