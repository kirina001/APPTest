# -*- coding:utf-8 -*-
import requests, json
from keywords.httpkeys import HTTP
import inspect

# a = 'post'
# http = HTTP()
# func = getattr(http, a)
# func('http://112.74.191.10:8081/inter/HTTP/auth')  # 反射
# args = inspect.getfullargspec(func).__str__()  # 获取函数的参数
# args = args[args.find('args=') + 5:args.find(', varargs')]
# args = eval(args)  # 变成参数列表
# args.remove('self')  # 移除self参数，因为这个代表实例本身不用传递
# print('参数列表' + str(args))
# print('参数个数' + str(len(args)))  # 参数长度
# print('获取注释信息')
# print(func.__doc__)

a = ['', '', '无token', 'post','http://112.74.191.10:8081/inter/HTTP/auth', '', '', '', '']
http = HTTP()
func = getattr(http, a[3])
args = inspect.getfullargspec(func).__str__()  # 获取函数的参数
print(args)
args = args[args.find('args=') + 5:args.find(', varargs')]
args = eval(args)  # 变成参数列表
args.remove('self') # 移除self参数，因为这个代表实例本身不用传递
print('参数列表' + str(args))
print('参数个数' + str(len(args)))  # 参数长度
len1 = len(args)
if len1 < 1:
    func()
if len1 < 2:
    func(a[4])
if len1 < 3:
    func(a[4], a[5])
