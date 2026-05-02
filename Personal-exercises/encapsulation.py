class Person:
    def __init__(self):
        self.a = 7 #public
        self._b = 15 #protected
        self.__c = 19 #private
    
    def test(self):
        print(self.__c)

p1 = Person()

# print(p1.a)


# p1.a=18
# print(p1.a)

class Child(Person):
    def __init__(self):
        super().__init__()
        self._b = 9

P1 = Person()

# print(p1._b)

p1.__c = 20
print(p1.__c)

# in dota baham farq daran

p1.test()

# private baray ine ke az taqir tasadofi moteqayer jologiri konim va be tor mostaqim behesh dastresi nadarim
