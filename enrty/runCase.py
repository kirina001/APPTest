# -*- coding: UTF-8 -*-
from common.Excel import Reader
from keywords.httpkeys import HTTP
import inspect


# 反射获取关键字
def getfunc(line):
    http = HTTP()
    func = getattr(http, line[3])
    return func

    # args.remove('self')
    #
    #

    #
    # if l<1:
    #     func()
    # if l<2:
    #     func(a[3])


# 反射获取参数
def getargs(func):
    args = inspect.getfullargspec(func).__str__()
    print(args)
    args = args[args.find('args=') + 5:args.find(',varargs')]
    args = eval(args)
    len = len(args)
    print(len)
    return len


# 运行测试用例
def run():
    reader = Reader()
    reader.open_excel('../lib/cases/HTTP接口用例.xls')
    sheetname = reader.get_sheets()
    for sheet in sheetname:
        reader.set_sheet(sheet)
        for i in range(reader.rows):
            line = reader.readline()
            print(line)
            # 如果第一列或第二列不为空，则不是测试用例
            if len(line[0])>0 or len(line[1])>0:
                pass
            else:
                func = getfunc(line)
                lenargs = getargs(func)


