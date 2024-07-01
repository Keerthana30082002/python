# Define the logging decorator
def logging_decorator(func):
    def wrapper():
        print("Function executed")
        func()
        print("Function execution complete")
    return wrapper

# Define the function to be decorated
@logging_decorator
def say_hello():
    print("hello")

# Test the decorated function
say_hello()