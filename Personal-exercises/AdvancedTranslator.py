d = dict(weather = "clima", earth = "terra", rain = "chuva") 

def myfunc():
    a = input("Enter word: ")
    for i in d.keys():
        if i == a:
            print(d[i])
        else:
            print("That word doesn't exist!")
            break
myfunc()

# def vocabulary(word):
#     try:
#         return d[word]
#     except KeyError:
#         return "That word doesn't exist."

# word = input("Enter word: ")
# print(vocabulary(word))