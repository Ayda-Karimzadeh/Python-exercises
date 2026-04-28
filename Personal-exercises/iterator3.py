class MyIter:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a < self.number:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

o1 = MyIter(8)

for n in o1:
    print(n)