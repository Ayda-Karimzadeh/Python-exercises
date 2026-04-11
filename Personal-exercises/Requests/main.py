import requests

r = requests.get("https://codeyad.com")

print(r) #<response [200]> successful

print(r.status_code) #200

e = requests.get("https://codeyad.com/afsfhlghhs")

print(e) #<Response [404]> not found

if r.status_code == 200:
    print("Success!")