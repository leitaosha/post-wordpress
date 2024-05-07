# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
import datetime
import os
import time


def setAttrForObj(obj, anydict: dict) -> bool:
    try:
        for key, value in anydict.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return True
    except Exception as e:
        print(e.__str__())
        return False


# 函数运行时间
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        log.info(f"函数 {func.__name__} 的执行时间为: {execution_time} 秒")
        return result

    return wrapper


# 获得根路径
def getRootPath():
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    parent_path = os.path.abspath(os.path.join(curPath, os.pardir))
    rootPath = parent_path
    return rootPath


def getTody():
    return datetime.datetime.now().date()


def getWeekday():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[datetime.datetime.now().weekday()]


