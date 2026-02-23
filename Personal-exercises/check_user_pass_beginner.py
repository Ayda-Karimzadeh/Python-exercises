users = {
    "amir": "1234",
    "reza": "4567",
    "farid": "6789"
}

entered_username = input('enter your username: ')
entered_password = input('enter your password: ')

while entered_username not in users or users[entered_username] != entered_password :
    print("your username or password is wrong!")
    entered_username = input("enter your username again: ")
    entered_password = input("enter your password again: ")

print('you loged in successfully!')