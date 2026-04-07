d = dict(weather = "clima", earth = "terra", rain = "chuva") 

def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "That word doesn't exist."

word = input("Enter word: ").lower() 
# As you see, we are converting all the string characters to lowercase as soon as we receive the user's input. Then we pass the lowercase version of the string to the dictionary.

print(vocabulary(word))