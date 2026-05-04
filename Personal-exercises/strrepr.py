# import datetime

# s = "Hello, Ayda."
# print(str(s))
# print(repr(s))

# a = "12"
# print(str(a))
# print(repr(a))

# today = datetime.datetime.now()

# print(str(today))
# print(repr(today))

class Teacher:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "Ayda str"

    def __repr__(self):
        return "Ayda repr"

t = Teacher("amir")

print(t)

print(repr(t))