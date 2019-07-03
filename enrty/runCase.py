# -*- coding: UTF-8 -*-
from common.Excel import Reader, Writer
from keywords.httpkeys import HTTP
import inspect


# 反射获取关键字
def getfunc(line,http):
    func = None
    try:
        func = getattr(http, line[3])
    except Exception as e:
        print(e)
    return func


# 反射获取参数
def getargs(func):
    if func:
        args = inspect.getfullargspec(func).__str__()
        print('原始参数'+str(args))
        args = args[args.find('args=') + 5:args.find(',varargs')]
        args = eval(args)  # 变成参数列表
        args.remove('self')  # 移除self参数，因为这个代表实例本身不用传递
        print('参数列表' + str(args))
        print('参数个数' + str(len(args)))  # 参数长度
        # print()
        # args = eval(args)
        # args.remove('self')
        len = len(args)
        # print('参数长度' + str(len))
        return len
    else:
        return 0


# 运行一条用例
def run(func, lenargs, line):
    # 如果没有这个函数 就不执行
    if func is None:
        return
    if lenargs < 1:  # 没有参数
        func()
        return
    if lenargs < 2:  # 一个参数
        func(line[4])
        return
    if lenargs < 3:
        func(line[4], line[5])
        return
    if lenargs < 4:
        func(line[4], line[5], line[6])
        return
    print('error: 目前只支持3个参数的关键字')


# 运行测试用例
def runCases():
    http = HTTP()
    reader = Reader()
    # writer = Writer()
    reader.open_excel('../lib/cases/HTTP接口用例.xls')
    # writer.copy_open('../lib/cases/HTTP接口用例.xls', '../lib/results/result-HTTP接口用例.xls')
    sheetname = reader.get_sheets()
    for sheet in sheetname:
        reader.set_sheet(sheet)
        for i in range(reader.rows):
            line = reader.readline()
            print(line)
            # 如果第一列或第二列不为空，则不是测试用例
            if len(line[0]) > 0 or len(line[1]) > 0:
                pass
            else:
                print(line)
                func = getfunc(line,http)
                lenargs = getargs(func)
                run(func, lenargs, line)


runCases()
