# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19

class Message:
    def __init__(self, status: bool, msg: str, code: int = 999):
        self.__status = status
        self.__msg = msg
        self.__netCode = code

    @property
    def status(self):
        return self.__status

    @property
    def msg(self):
        return self.__msg

    @property
    def netCode(self):
        return self.__netCode

    def __str__(self):
        return self.__dict__.__str__().replace('_Message__', '')

