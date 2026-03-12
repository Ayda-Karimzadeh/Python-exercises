import glob

letters = []
file_list = glob.glob("*.txt")

for filename in file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
    if letter in "python":
        letters.append(letter)


print(letters)