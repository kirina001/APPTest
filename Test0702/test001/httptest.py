# -*- coding: UTF-8 -*-
import requests, json
from test001.httpkeys import HTTP

http = HTTP()  # 创建http实例对象
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status','200')
