# from abc import ABC, abstractmethod, abstractproperty

# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass
    
#     @abstractproperty
#     def legs(self):
#         pass

# class Lion(Animal):
#     def move(self):
#         print("lion is moving")
    
#     @property
#     def legs(self):
#         return 4

# class Dog(Animal):
#     def move(self):
#         print("dog is moving")
    
#     @property
#     def legs(self):
#         return 2

# l1 = Lion()
# d1 = Dog()
# l1.move()
# d1.move()

# print(l1.legs)
# print(d1.legs)
# ....................................

# in python 3.14 you should do this:

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

    @property
    @abstractmethod
    def legs(self):
        pass


class Lion(Animal):
    def move(self):
        print("lion is moving")

    @property
    def legs(self):
        return 4


class Dog(Animal):
    def move(self):
        print("dog is moving")

    @property
    def legs(self):
        return 2


l1 = Lion()
d1 = Dog()

l1.move()
d1.move()

print(l1.legs)
print(d1.legs)
