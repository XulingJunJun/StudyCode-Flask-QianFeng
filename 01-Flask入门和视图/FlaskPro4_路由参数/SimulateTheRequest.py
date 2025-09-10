import requests

res = requests.get('http://127.0.0.1:5000/method/')
print(res.text)

res = requests.post('http://127.0.0.1:5000/method/')
print(res.text)
