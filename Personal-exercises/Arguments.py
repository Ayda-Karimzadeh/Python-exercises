# Why do you get an error, and how would you fix it?

# def foo(a=2, b):
#     return a + b

def foo(b, a=2):
    return a + b
# Always put non-default parameters first, followed by default ones.
