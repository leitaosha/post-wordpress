# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
from urllib.parse import urljoin
from utiles.util import setAttrForObj
from posts.AbstractPost import AbstractPost
from utiles.config import *


class Post(AbstractPost):

    def __init__(self):
        super().__init__()
        self.URL_POST = urljoin(WORDPRESS_SITE, '/wp-json/wp/v2/posts')

    def list(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def retrieve(self):
        pass

    def toDict(self, containList):
        attrDict = self.__dict__
        return {key: attrDict.pop(key) for key in containList if key in attrDict}


# 测试
obj = Post()
obj.toDict()
