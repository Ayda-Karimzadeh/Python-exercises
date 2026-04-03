d = dict(weather = "clima", earth = "terra", rain = "chuva")

def myfunc():
    a = input("Enter word: ")
    for i in d.keys():
        if i == a:
            print(d[i])
myfunc()

# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# def vocabulary(word):
#     return d[word]

# word = input("Enter word: ")
# print(vocabulary(word))