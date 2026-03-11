import string

mylist = []
for i in string.ascii_lowercase:
    with open(i+".txt","r") as f:
        letter = f.read()
        mylist.append(letter)

print(mylist)

# import glob

# letters = []
# file_list = glob.glob("letters/*.txt")

# for filename in file_list:
#     with open(filename,"r") as file:
#         letters.append(file.read().strip("\n"))

# print(letters)

# we generate a list with glob.glob (list of path those have this pattern)
# glob() will be looking at the pattern in its paranthes, path pattern for file names.
#  * means everything