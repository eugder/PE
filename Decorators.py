import Decorators_lib

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
@Decorators_lib.test_decorator
def say_something():
    print("Ok")
    return ("Returned msg")

# say_whee = my_decorator(say_whee)

print(say_something())