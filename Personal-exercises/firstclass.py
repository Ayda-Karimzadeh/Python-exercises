# # first class functions in python
# a = "Ayda"
# print(a)
#
# b=a
# print(b)
#
# def test(text):
#     print(text)
#
# test(a)
#................................................................
# def test(text):
#     print(text)
#
# b = test
#
# b("Ayda")
# .....................................................................

def test(func):
    return func

def test2(number):
    print(number+5)

# a = test(test2)
# a(5)

mylist = [test2]
print(mylist)
