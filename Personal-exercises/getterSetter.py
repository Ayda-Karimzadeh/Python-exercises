class Person:
    def __init__(self):
        self.a = 7 #public
        self._b = 15 #protected
        self.__age = 20
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self, value):
#         self.__age = value

# p1 = Person()

# a = p1.get_age()

# print(a)

# p1.set_age(38)
# a = p1.get_age()

# print(a)

#     def get_age(self):
#         return self.__age
    
#     def set_age(self, value):
#         self.__age = value
    
#     def del_age(self):
#         del self.__age

#     age = property(get_age, set_age, del_age)

# p1 = Person()
# print(p1.age)

# p1.age = 15

# del p1.age
# print(p1.age)
# .......................................................

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value > 50:
            raise ValueError('sorry')
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age

p1 = Person()

print(p1.age)

p1.age = 16

print(p1.age)

p1.age = 51