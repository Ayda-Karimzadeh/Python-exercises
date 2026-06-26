# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

def countDog(text):
    text.lower()
    return text.count("dog")

print(countDog('This dog runs faster than the other dog dude!'))

# def countDog(st):
#     count = 0
#     for word in st.lower().split():
#         if word == 'dog':
#             count += 1
#     return count