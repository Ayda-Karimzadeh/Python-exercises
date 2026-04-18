def my_decorator(func):
    def wraper():
        print("Hello")
        func()
        print("Goodbye")
    return wraper

@my_decorator
def say_myname():
    print("I'm Ayda")

say_myname()