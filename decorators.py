# decorators: extending the behavior of functions and classes without modifying the underlying. 

import functools

# example of function decorator
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        res = func(*args, **kwargs)
        print("End")
    return wrapper

# uses the above function to extend the below function
@start_end_decorator
def print_name():
    print("Ben")

print_name()

# Decorators with arguments

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet("Ben")

# Class decorator: often used to maintain and track state across function calls

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This has executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("HI!")

say_hi()
say_hi()
say_hi()
