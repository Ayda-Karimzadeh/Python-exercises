import requests

url = 'https://example.com/api/data'
payload = {'key1': 'value1', 'key2': 'value2'}
auth = ('username', 'password')
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, auth=auth, headers=headers)

if response.status_code == 200:
    print('Data sent successfully')
else:
    print('Error sending data:', response.text)