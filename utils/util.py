# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
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


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        log.info(f"函数 {func.__name__} 的执行时间为: {execution_time} 秒")
        return result

    return wrapper

