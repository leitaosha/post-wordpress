# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18


from abc import ABC, abstractmethod


# Posts类
class AbstractPosts(ABC):

    def __init__(self):
        self.tags = None
        self.categories = None
        self.template = None
        self.sticky = None
        self.meta = None
        self.format = None
        self.ping_status = None
        self.comment_status = None
        self.featured_media = None
        self.excerpt = None
        self.author = None
        self.content = None
        self.title = None
        self.generated_slug = None
        self.permalink_template = None
        self.password = None
        self.type = None
        self.status = None
        self.slug = None
        self.modified_gmt = None
        self.modified = None
        self.link = None
        self.id = None
        self.guid = None
        self.date_gmt = None
        self.date = None


    @abstractmethod
    def listPosts(self):
        pass

    @abstractmethod
    def createPosts(self):
        pass

    @abstractmethod
    def updatePosts(self):
        pass

    @abstractmethod
    def deletePosts(self):
        pass

