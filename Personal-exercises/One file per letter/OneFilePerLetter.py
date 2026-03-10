import string

for i in string.ascii_lowercase:
    with open(f"{i}.txt","w") as f:
        f.write(i)

# import string,os
# if not os.path.exists("letters"):
#   os.makedirs("letters")
# for letter in string.ascii_lowercase:
#   with open("letters/" + letter + ".txt" + "w" ) as file:
#       file.write(letter)