
# def hello(name):
#     def hello_name():
#         print(f"Hello {name}")
#     return hello_name

# new = hello("mobina")

# new()
#........................................................................

#decorator
# def hello_decorator(func):
#     #wrapper
#     def inner():
#         print("Hello before function execution")
#         func() # Hi user
#         print("this is after function execution")
#     return inner

# # شیوه استاندارد
# @hello_decorator
# def hello():
#     print("Hi user")
# hello()

# new = hello_decorator(hello)
# new()
#میتونی از همون اسم هلو استفاده کنی بجای نیو
# hello = hello_decorator(hello) # @hello_decorator
# hello()



#..........................................................................
# def my_decorator(func):
#     def wraper():
#         print("Hello")
#         func()
#         print("Goodbye")
#     return wraper

# @my_decorator
# def say_myname():
#     print("I'm Ayda")
# say_myname()

#...........................................................................

def hello_decorator(func):
    #wrapper
    def inner(*args, **kwargs):
        print("Hello before function execution")
        func(*args, **kwargs) # Hi user
        print("this is after function execution")
    return inner

# شیوه استاندارد
@hello_decorator
def hello(name):
    print(f"Hi {name}")
hello("Ayda")