# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18

import frontmatter
from md_processors.AbstractMarkdownInfo import AbstractMarkdownInfo
from posts.post import Post
from utils.util import setAttrForObj
from md_processors.check_params import check_params


class WPMarkdown(AbstractMarkdownInfo):
    def __init__(self, post: frontmatter.Post, postMeta: Post):
        super().__init__()
        # yaml必备信息
        self.title = None
        self.tags = None
        self.excerpt = None
        # 分类
        self.categories = None
        # 初始化yaml和content
        self.post = post if type(post) is frontmatter.Post and post else None
        self.md_content, self.md_yaml = self.post.content, self.post.metadata if self.post else None
        # 初始化属性赋值
        self.__setAttr()
        # wp元信息
        self.wp = postMeta

    def getTags(self):
        return self.tags

    def getTitle(self):
        return self.title

    def getContent(self):
        return self.md_content

    def getCategories(self):
        return self.categories

    def __setAttr(self):
        setAttrForObj(self, self.md_yaml)

    def __updatePost(self):
        self.post.metadata = self.md_yaml
        self.post.content = self.md_content

    def updateYaml(self, new_attr: dict):
        """
        :param new_attr: new attributes
        :return: None
        """
        self.md_yaml.update(new_attr)
        self.__setAttr()
        self.__updatePost()

    def updateContent(self, newContent: str):
        """
        :param newContent: changed content of markdown
        :return: None
        """
        self.md_content = newContent
        self.post.content = self.md_content
        self.__updatePost()

    def __str__(self):
        return self.__dict__.__str__()


# 解析markdown
def getMarkdown(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        parseMd = frontmatter.load(f)
    parseMd.metadata = check_params(parseMd.metadata)
    return WPMarkdown(parseMd, Post())
