# -*- coding: UTF-8 -*-
import requests, json


class HTTP:

    def __init__(self):  # 构造函数
        self.session = requests.session()  # 保存cookie信息
        self.jsonres = {}  # 存放json返回的数据

    def post(self, path, data=None):  # post实例方法
        if data is None:
            result = self.session.post(path)
        else:
            result = self.session.post(path, data=data)
        self.jsonres = json.loads(result.text)
        print('返回结果'+str(self.jsonres))
        # print(type(self.jsonres))

    def assertequals(self, key, value):  # 断言相等方法
        if str(self.jsonres[key]) == str(value):
            print('PASS')
        else:
            print('FAIL')
