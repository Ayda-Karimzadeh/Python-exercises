p = input("enter your password: ")

has_num = any(i.isdigit() for i in p)
has_upper = any(i.isupper() for i in p)

if has_num:
    pass
else:
    print("at least 1 num")

if has_upper:
    pass
else:
    print("at least 1 upper case")

if len(p)>= 5:
    pass
else:
    print("5 or more characters")

# p = input("enter your password: ")

# if not any(i.isdigit() for i in p):
#     print("Password must contain at least 1 number")

# if not any(i.isupper() for i in p):
#     print("Password must contain at least 1 uppercase letter")

# if len(p) < 5:
#     print("Password must be at least 5 characters long")
