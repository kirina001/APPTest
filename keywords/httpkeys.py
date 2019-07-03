# -*- coding: UTF-8 -*-
import requests, json


class HTTP:

    def __init__(self):  # 构造函数
        self.session = requests.session()  # 保存cookie信息
        self.jsonres = {}  # 存放json返回的数据
        self.params = {}  # 保存参数变量，实现关联
        self.url = ''  # 全局url参数

    def post(self, path, data=None):  # post实例方法
        if data is None or data == '':
            result = self.session.post(path)
        else:
            data = self.__getparams(data)  # 替换参数
            data = self.__todict(data)  # 转为字典
            result = self.session.post(path, data=data)
        self.jsonres = json.loads(result.text)
        print('返回结果' + str(self.jsonres))
        # print(type(self.jsonres))

    def assertequals(self, key, value):  # 断言相等方法
        if str(self.jsonres[key]) == str(value):
            print('PASS')
        else:
            print('FAIL')

    def addheader(self, key, value):  # 添加头信息 key value
        value = self.__getparams(value)
        self.session.headers[key] = value

    def savejson(self, param, key):
        self.params[param] = self.jsonres[key]
        print('获取到的参数信息' + str(self.params[param]))

    def __getparams(self, s):
        print('关联参数' + str(self.params))
        for key in self.params:
            s = s.replace('{' + key + '}', self.params[key])

        return s

    def __todict(self, s):
        httpparam = {}
        param = s.split('&')  # 分参数
        print('URL传入参数' + str(param))
        for ss in param:
            p = ss.split('=')  # 分键值对
            httpparam[p[0]] = p[1]
        print('RUL参数处理后' + str(httpparam))
        return httpparam

    def seturl(self, url):
        # url =''
        if url.startswith('http') or url.startswith('https'):
            self.url = url
        else:
            print('url地址不合法')
