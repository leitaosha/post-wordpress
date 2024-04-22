# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
from abc import ABC
from urllib.parse import urljoin

import requests

from posts.AbstractCategory import AbstractCategory
from utils.config import *
from utils.util import setAttrForObj
from error.Message import Message


class Category(AbstractCategory):
    def __init__(self, categoryName: str, categoryId: int = None):
        super().__init__(categoryName, categoryId)
        self.URL_CAT = urljoin(WORDPRESS_SITE, '/wp-json/wp/v2/categories')

    @property
    def URL_CREATE_CAT(self):
        return urljoin(WORDPRESS_SITE, f'/wp-json/wp/v2/categories?name={self.name}')

    @property
    def URL_RETRIEVE_CAT(self):
        return urljoin(WORDPRESS_SITE, f'/wp-json/wp/v2/categories/{self.id}')

    def list(self):
        res = requests.get(self.URL_CAT, auth=AUTHORIZATION)
        print(res.json())

    def search(self):
        res = requests.get(self.URL_CAT, {'search': self.name}, auth=AUTHORIZATION)
        result = [result for result in res.json() if result['name'] == self.name]
        return Message(setAttrForObj(self, result[0]), f'Search({self.name}) successfully!', res.status_code) \
            if result else Message(False, f"Category({self.name}) does not exist!", res.status_code)

    def create(self):
        res = requests.post(self.URL_CREATE_CAT, auth=AUTHORIZATION)
        if res.status_code == 400:
            self.id = res.json()['data']['term_id'] if res.json()['data'] and res.json()['data']['term_id'] else None
            # retrieve_status = self.retrieve().status
            return Message(True, f"Category({self.name} already exist! )", res.status_code)
        elif res.status_code == 201:
            return Message(setAttrForObj(self, res.json()), f"Category({self.name}) create successfully!",
                           res.status_code)
        else:
            return Message(False, "status code not recognized, unknown mistake!", res.status_code)

    def retrieve(self):
        if self.id:
            res = requests.get(self.URL_RETRIEVE_CAT, auth=AUTHORIZATION)
            return Message(setAttrForObj(self, res.json()), f"Retrieve successfully!", res.status_code) \
                if res.status_code == 200 else Message(False, f"Retrieve failed!", res.status_code)
        else:
            return Message(False, 'Retrieve category need id!')

    def __str__(self):
        return self.__dict__.__str__()


# 　测试
# obj = Category('Python')
# print(obj.search())
# print("list\n\n\n\n\n\n")
# obj.list()
# print(obj.create())
# print(str(obj))
# ojb = Category('python')
# print(obj.create())
