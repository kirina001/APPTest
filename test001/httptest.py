# -*- coding: UTF-8 -*-
import requests, json
from test001.httpkeys import HTTP

http = HTTP()  # 创建http实例对象
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token为''
http.addheader('token', '')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token为'a'
http.addheader('token', 'a')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# token为'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
http.addheader('token', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '200')

# 保存token
http.savejson('t', 'token')
http.addheader('token', '{t}')
print(http.session.headers)
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status', '201')

# {'username':'Test000001','password':'Test000001'}
# 登录并查看用户信息
# http.post('http://112.74.191.10:8081/inter/HTTP/login', {'username': 'Test000001', 'password': 'Test000001'})
http.post('http://112.74.191.10:8081/inter/HTTP/login', 'username=Test000001&password=Test000001')

http.assertequals('status', '200')
http.savejson('id','userid')
# http.post('http://112.74.191.10:8081/inter/HTTP/getUserInfo', {'id':'{id}'})
http.post('http://112.74.191.10:8081/inter/HTTP/getUserInfo','id={id}')
http.assertequals('status', '200')
http.post('http://112.74.191.10/inter/HTTP/logout')
http.assertequals('status', '200')
