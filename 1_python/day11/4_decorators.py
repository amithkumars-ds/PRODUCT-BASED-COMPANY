def wrapper(func):
    def execute():
        print("Starting operation...")
        func()
        print("Operation completed.")
    return execute

@wrapper
def process_payment():
    print("Processing payment...")


if __name__ == "__main__":
    process_payment() 
