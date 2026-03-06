import os

def count_words():
    strng_list = []
    if os.path.exists("text.txt"):
        with open("text.txt","r") as myfile:
            strng = myfile.read()
            strng_list = strng.split()
        return len(strng_list)

print(count_words())

# def count_words():
#     strng_list = []
#     if os.path.exists("text.txt"):
#         myfile =open("text.txt", "r")
#         strng = myfile.read()
#         strng_list = strng.split()
#         return len(strng_list)

# print(count_words())

# it's important which folder is open in terminal