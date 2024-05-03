# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
from urllib.parse import urljoin

import requests

from error.Message import Message
from posts.AbstractPost import AbstractPost
from utils.config import *
from utils.util import setAttrForObj


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
        if id exists, update article. if not, then create.
        :return:
        """
        if self.id:
            return self.update()
        res = requests.post(self.URL_POST, json=self.postData, auth=AUTHORIZATION)
        return Message(setAttrForObj(self, res.json()), f"id: {self.id}, title: {self.title} pushed successfully!",
                       res.status_code) \
            if res.status_code == 201 else Message(False, f"id: {self.id}, title: {self.title} pushed failed!",
                                                   res.status_code)

    def update(self):
        res = requests.post(self.URL_UPDATE_POST, json=self.postData, auth=AUTHORIZATION)
        if res.status_code == 200:
            return Message(setAttrForObj(self, res.json()), f"id: {self.id}, title: {self.title} updated successfully!",
                           res.status_code)
        # if delete article remotely, then create.
        elif res.status_code == 404:
            self.id = None
            self.create()
        else:
            return Message(False, f"id: {self.id}, title: {self.title}  updated failed!", res.status_code)

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

    def __str__(self):
        return self.__dict__.__str__()
