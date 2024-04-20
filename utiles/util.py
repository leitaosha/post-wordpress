# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19

def setAttrForObj(obj, anydict: dict) -> bool:
    try:
        for key, value in anydict.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return True
    except Exception as e:
        print(e.__str__())
        return False
