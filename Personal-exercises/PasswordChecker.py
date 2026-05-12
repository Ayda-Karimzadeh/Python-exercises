password = input("Enter new password:")

numal = password.isalnum()
has_upper = any(i.isupper() for i in password)

if numal and has_upper and 5<=len(password):
    print("fine")

else:
    print("password is not fine")

# while True:
#     psw = input("Enter new password: ")
#     if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
#         print("Password is fine")
#         break
#     else:
#         print("Password is not fine")