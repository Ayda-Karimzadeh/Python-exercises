import requests

response = requests.get('https://codeyad.com/')

print(response)
print(response.status_code)
print(type(response))
print(type(response.status_code))

print(response.text)