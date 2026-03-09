f = open("myfile.txt","w")
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alphabets:
    f.write(f"{i}\n")
f.close()

# import string

# with open("letters.txt", "w") as file:
#     for letter in string.ascii_lowercase:
#         file.write(letter + "\n")