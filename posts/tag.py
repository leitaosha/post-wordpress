# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
from urllib.parse import urljoin
from posts.AbstractTag import AbstractSingleTag
import requests
from utiles.config import WORDPRESS_SITE, AUTHORIZATION
from utiles.util import setAttrForObj
from error.Message import Message


class Tag(AbstractSingleTag):
    def __init__(self, name, tagId=None):
        super().__init__(name, tagId)
        self.tagNameBefore = None
        self.URL_TAG = urljoin(WORDPRESS_SITE, '/wp-json/wp/v2/tags')

    @property
    def URL_RETRIEVE_TAG(self):
        return urljoin(WORDPRESS_SITE, f"/wp-json/wp/v2/tags/{self.id}")

    @property
    def URL_DELETE_TAG(self):
        return urljoin(WORDPRESS_SITE, f"/wp-json/wp/v2/tags/{self.id}?force=1")

    @property
    def URL_UPDATE_TAG(self):
        return urljoin(WORDPRESS_SITE, f'/wp-json/wp/v2/tags/{self.id}')

    # Action
    def search(self):
        """
        search tag by name
        :return: class Message
        """
        res = requests.get(self.URL_TAG, {"search": self.name}, auth=AUTHORIZATION)
        if res.status_code == 200:
            if len(res.json()) == 0:
                return Message(False, f"Tag({self.name}) does not exist!", res.status_code)
            elif res.json()[0]['name'] == self.name:
                setAttrForObj(self, res.json()[0])
                return Message(True, f"Search successful! Tag({self.name}) exist", res.status_code)
        else:
            return Message(False, "status code not defined!", res.status_code)

    def create(self):
        """
        create tag by name
        :return: class Message
        """
        res = requests.post(self.URL_TAG, {'name': self.name}, auth=AUTHORIZATION)
        if res.status_code == 201:
            setAttrForObj(self, res.json())
            return Message(True, "Create tag successfully!", res.status_code)
        elif res.status_code == 400:
            self.id = res.json()['data']['term_id']
            self.retrieveTag()
            return Message(True, "Tag already exists!", res.status_code)
        else:
            return Message(False, "Failed to create tag !", res.status_code)

    def update(self, newTagName):
        """
        update tag by name
        :param newTagName: new tag
        :return:
        """
        if self.searchTag().status:
            res = requests.post(self.URL_UPDATE_TAG, {'name': newTagName}, auth=AUTHORIZATION)
            if res.status_code == 200:
                setAttrForObj(self, res.json())
                return Message(True, f"Update tag({self.name}) successfully!", res.status_code)
        else:
            return Message(False, "Tag does not exist!", 404)

    def retrieve(self):
        """
        get tag by id, self.id should be set before retrieve.
        :return: Message
        """
        res = requests.get(self.URL_RETRIEVE_TAG, auth=AUTHORIZATION)
        setAttrForObj(self, res.json()) if res.status_code == 200 else print('retrieved fail! it is not exists!')
        return Message(True, "Retrieve tag successfully!", res.status_code)

    def delete(self):
        """
        delete tag by id
        :return: Message
        """
        if self.id or self.searchTag().status:
            res = requests.delete(self.URL_DELETE_TAG, auth=AUTHORIZATION)
            if res.status_code == 200:
                self.tagNameBefore = self.name
                self.__set_attributes_to_none(['id', 'tagNameBefore'])
                return Message(True, f"Delete tag({self.tagNameBefore}) successfully!", res.status_code)
            else:
                pass
        return Message(False, f"Tag({self.name}) does not exist!", 404)

    def __set_attributes_to_none(self, exclude: list):
        for attr in vars(self):
            if attr not in exclude:
                setattr(self, attr, None)

    def __str__(self):
        return self.__dict__.__str__()


# 测试
# start_time = time.time()
# obj = Tag('pythonTags1')
# print(obj.search())
# print(obj.create())
# print(obj.update("pytonTag"))
# print(str(obj))
# print(str(obj.delete()))
# print(str(obj))
# end_time = time.time()

# print('Execution Time: ', end_time - start_time, 's')
