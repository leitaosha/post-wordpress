# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18

from abc import ABC, abstractmethod


# tag类
class AbstractCategory(ABC):

    def __init__(self):
        self.id = None
        self.count = None
        self.description = None
        self.link = None
        self.name = None
        self.slug = None
        self.taxonomy = None
        self.parent = None
        self.meta = None

    @abstractmethod
    def listCategories(self):
        pass


