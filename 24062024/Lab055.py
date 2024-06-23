# Decorators

def my_decorators(func):
    def wrapper():
        print("Starting of the function")
        print("**********")
        func()
        print("*******")
        print("End of function")
    return wrapper()


@my_decorators
def say_hello():
    print("say Hello")



