# ** Split this string:**

# s = "Hi there Sam!"
# **into a list. **
# .................................................................

s = "Hi there Sam!"
# a = [i for i in s.split()]
# print(a)

a = s.split()
print(a)

# We don't need a list comprehension because the split() method already returns a list