# Why is there an error in the code, and how would you fix it?

# def foo(a, b):
#     print(a + b)

# x = foo(2, 3) * 10

# def foo(a, b):
#     print((a + b)*10)

# x = foo(2, 3)

# Line 4 throws a TypeError because Python cannot multiply a None type object with an integer. The function output is what produces a None object because the function definition is not returning anything. Fix it by using return  instead of print :

def foo(a, b):
    return a + b

x = foo(2, 3) * 10