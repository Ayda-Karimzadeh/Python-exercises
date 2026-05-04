# def gnrtor():
#     yield 1
#     yield 2
#     yield 3

# # for value in gnrtor():
# #     print(value)

# x = gnrtor() #iterator
# print(type(x))

# # for value in x:
# #     print(value)

# print(next(x))
# print(next(x))
# # print(next(x))
# print(x.__next__())

def fib(limit):
    # a, b = 0, 1
    a = 0
    b = 1
    while a < limit:
        yield a
        a, b = b, a+b

x = fib(5)

for value in x:
    print(value)

# masraf kamtar ram ba generator, chizi ke yeild shode zakhire nemishe