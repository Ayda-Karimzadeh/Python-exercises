while True:

    password = input("enter your password: ")

    if len(password)<8 :
        print("your password must be at least 8 char!")
    elif password.isnumeric() :
        print("your password should contain at least a letter!")
    elif password.isalpha():
        print("your password should contain at least a number!")
    else:
        print("your password is great!")