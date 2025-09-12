import requests

res = requests.get('http://127.0.0.1:5000/request/?name=zhangsan&age=33&name=lisi',cookies={'name': 'i am cookies'})
print(res.text)

# res = requests.post('http://127.0.0.1:5000/request', data={'name': '王五', 'name': 'lisi','age': 33})
# res = requests.post('http://127.0.0.1:5000/request', data={'name': '王五', 'age': 33})
# print(res.text)text
