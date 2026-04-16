# Question: Count the number of "a" characters in this text file:http://www.pythonhow.com/data/universe.txt

import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt",headers ={'user-agent' : 'customAgentUser'})

text = response.text

i=0

for char in text:
    if char == "a":
        i =+ 1
print(i)

# import requests

# response = requests.get("http://www.pythonhow.com/data/universe.txt")
# text = response.text
# count_a = text.count("a")
# print(count_a)