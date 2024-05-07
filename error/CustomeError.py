# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18

class CustomError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


