name = "Ayda Karimzadeh" #iterable

# myiterator  = iter(name)
#
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))

# for n in name :
#     print(n)

# sakht yek class ke object hay iterable darad ke mishe az roy anha iterator sakht
# class MyIter:
#     # def __init__(self):
#     #     pass
#
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
# o1 = MyIter()
# myiterator = iter(o1)
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))

# class MyIter:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a < 6:
#             x = self.a
#             self.a += 1
#             return x
#
# o1 = MyIter()
# myiterator = iter(o1)
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))

class MyIter:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a < 6:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

o1 = MyIter()
# myiterator = iter(o1)
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))

for n in o1:
    print(n)