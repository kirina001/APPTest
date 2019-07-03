# -*- coding: UTF-8 -*-
import requests, json

# 创建session对象，模拟浏览器的cookie管理
session = requests.session()
jsonres = {}


# 使用session请求接口
result = session.post('http://112.74.191.10:8081/inter/HTTP/auth')
jsonres = json.loads(result.text)
if jsonres['status'] == 200 and not (jsonres['token'] is None):
    print('pass')

# 添加头
session.headers['token'] = ''
result = session.post('http://112.74.191.10:8081/inter/HTTP/auth')
jsonres = json.loads(result.text)
if jsonres['status'] == 200:
    print('pass')

# 一位长度
session.headers['token'] = 'a'
result = session.post('http://112.74.191.10:8081/inter/HTTP/auth')
jsonres = json.loads(result.text)
if jsonres['status'] == 200:
    print('pass')
# 过长
session.headers['token'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
result = session.post('http://112.74.191.10:8081/inter/HTTP/auth')
jsonres = json.loads(result.text)
if jsonres['status'] == 200:
    print('pass')
# 未授权
session.headers['token'] = '109f1a34bdcf4785b6c70a9917d7a49d'
result = session.post('http://112.74.191.10:8081/inter/HTTP/auth')
jsonres = json.loads(result.text)
if jsonres['status'] == 200:
    print('pass')
# 保存token
token = json.loads(result.text)['token']
print(token)
# token已经授权
session.headers['token'] = token
result = session.post('http://112.74.191.10:8081/inter/HTTP/auth')
jsonres = json.loads(result.text)
if jsonres['status'] == 200:
    print('pass')
# 登录
result = session.post('http://112.74.191.10:8081/inter/HTTP/login', data={'username': 'Tester', 'password': '123456'})
jsonres = json.loads(result.text)
if jsonres['status'] == 200:
    print('pass')
# token已经登录
result = session.post('http://112.74.191.10:8081/inter/HTTP/auth')
jsonres = json.loads(result.text)
if jsonres['status'] == 201:
    print('pass')


# 注销
result = session.post('http://112.74.191.10:8081/inter/HTTP/logout')
jsonres = json.loads(result.text)
if jsonres['status'] == 202:
    print('pass')
