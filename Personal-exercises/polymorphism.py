class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    
    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.D is the capital of USA.")
    
    def language(self):
        print("English is the most widely spoken language of USA.")
    
    def type(self):
        print("USA is a developing country.")

# obj_ind = India()
# obj_usa = USA()

# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()

class Bird():
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some can't.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches can not fly.")

obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()