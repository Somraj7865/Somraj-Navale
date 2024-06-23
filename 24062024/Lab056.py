def decorator1(func):
    def wrapper():
        print("Decorator1")
        func()

    return wrapper


def decorator2(func):
    def wrapper():
        print("Decorator2")
        func()

    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello")


say_hello()

# *******************
# def decorator1(func):
#     def wrapper():
#         print("Decorator1")
#         func()
#     return wrapper
#
# def decorator2(func):
#     def wrapper():
#         print("Decorator2")
#         func()
#     return wrapper
#
# @decorator1
# @decorator2
# def say_hello():
#     print("Hello")
#
# say_hello()
