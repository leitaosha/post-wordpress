# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
import json
from urllib.parse import urljoin

import requests

from error.Message import Message
from utiles.util import setAttrForObj
from posts.AbstractPost import AbstractPost
from utiles.config import *


class Post(AbstractPost):

    def __init__(self):
        super().__init__()
        self.URL_POST = urljoin(WORDPRESS_SITE, '/wp-json/wp/v2/posts')

    @property
    def URL_UPDATE_POST(self):
        return urljoin(WORDPRESS_SITE, f'/wp-json/wp/v2/posts/{self.id}') if self.id else self.URL_POST

    def list(self):
        pass

    def create(self):
        """
        if id exists, update article
        :return:
        """
        if self.id:
            return self.update()
        res = requests.post(self.URL_POST, json=self.postData, auth=AUTHORIZATION, verify=False)
        return Message(setAttrForObj(self, res.json()), f"<<{self.title}>> pushed successfully!", res.status_code) \
            if res.status_code == 201 else Message(False, f"<<{self.title}>> pushed failed!", res.status_code)

    def update(self):
        res = requests.post(self.URL_UPDATE_POST, json=self.postData, auth=AUTHORIZATION)
        return Message(setAttrForObj(self, res.json()), f"<<{self.title}>> updated successfully!", res.status_code) \
            if res.status_code == 200 else Message(False, f"<<{self.title}>> updated failed!", res.status_code)

    def delete(self):
        pass

    def retrieve(self):
        pass

    @property
    def postData(self, excluded_fields=['URL_POST']) -> dict:
        """
        delete none fields and excluded fields
        :param excluded_fields:
        :return: dict
        """
        if excluded_fields is None:
            excluded_fields = []
        return {key: value for key, value in self.__dict__.items() if key not in excluded_fields and value}


# 测试
# obj = Post()
# print(obj.__dict__)
#
# print(obj.toDict())

# 提交
# obj = Post()
# obj.content = "content22222222222222"
# obj.title = 'title222222222222'
# obj.excerpt = 'excerpt2222222222222222222222222'
# obj.categories = [65]
# obj.tags = [66, 52, 22]
# print(obj.create())
# print(json.dumps(obj.postData))
# print(type(obj.postData['tags']))
# print(type(obj.postData()))
# 更新
# obj = Post()
# obj.id = 99
# obj.content = "contentUp"
# obj.title = 'titleUp'
# obj.excerpt = 'excerptUp'
# obj.categories = [65]
# obj.tags = [66, 52]
# print(obj.create())
# print(obj.postData)
