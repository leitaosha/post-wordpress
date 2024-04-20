# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
from posts.AbstractPost import AbstractPost
from utiles.util import setAttrForObj


class WordPressMeta(AbstractPost):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return self.__dict__.__str__()
