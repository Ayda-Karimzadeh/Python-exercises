# ** Given the variables:**

# planet = "Earth"
# diameter = 12742
# ** Use .format() to print the following string: **

# The diameter of Earth is 12742 kilometers.

planet = "Earth"
diameter = 12742

print("The diameter of {} is {} kilometers.".format(planet,diameter))

# but i prefer f-strings:
# print(f"The diameter of {planet} is {diameter} kilometers.")