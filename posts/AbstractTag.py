# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18


from abc import ABC, abstractmethod


# tag类
class AbstractSingleTag(ABC):

    def __init__(self, name, tagId=None):
        self.id = tagId
        self.count = None
        self.description = None
        self.link = None
        self.name = name
        self.slug = None
        self.taxonomy = None
        self.meta = None

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def retrieve(self):
        pass

    @abstractmethod
    def update(self, newTagName):
        pass

    @abstractmethod
    def delete(self):
        pass
