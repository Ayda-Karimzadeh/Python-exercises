# Why is there an error in the code, and how would you fix it?
# def foo(a=1, b=2):
#     return a + b

# x = foo - 1

def foo(a=1, b=2):
    return a + b

x = foo() - 1

#the function call is an integer but the function itself (the function blueprint) is a function object
print(type(foo))
print(type(foo()))