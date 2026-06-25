# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

def countDog(text):
    text.lower()
    return text.count("dog")

print(countDog('This dog runs faster than the other dog dude!'))