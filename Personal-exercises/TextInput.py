# Question: The code produces an error. Please understand the error and try to fix it

# age = input("What's your age? ")
# age_last_year = age - 1
# print("Last year you were %s." % age_last_year)

age = int(input("What's your age? "))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)

# Or:
# age = input("What's your age? ")
# age_last_year = int(age) - 1
# print("Last year you were %s." % age_last_year)


# In this alternative solution, we applied the int  function in the line where the math operation occurs. This could be useful if you intend to use the user input value as a string in other parts of your script, so you don't want to convert it to an integer directly.