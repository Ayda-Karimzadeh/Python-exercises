filepath = "D:/Python developer/Python-exercises/Personal-exercises/UsernameAndPasswordChecker/users.txt"
while True:
    usr = input("Enter username: ")

    with open(filepath,"r") as f:
       users = f.readlines()
       users = [i.strip() for i in users]
    if usr in users:
        print("username exists.")
        continue
    else:
        print("username is fine")
        break

while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following : ")
        for note in notes:
            print(note)