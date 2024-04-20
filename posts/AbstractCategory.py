# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18

from abc import ABC, abstractmethod


# tag类
class AbstractCategory(ABC):

    def __init__(self, categoryName: str, categoryId: int = None):
        self.id = categoryId
        self.count = None
        self.description = None
        self.link = None
        self.name = categoryName
        self.slug = None
        self.taxonomy = None
        self.parent = None
        self.meta = None

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def search(self):
        pass


