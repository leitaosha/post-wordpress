# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18

import frontmatter
from md_process.AbstractMarkdownInfo import AbstractMarkdownInfo
from md_process.WordPressMeta import WordPressMeta
from utiles.util import setAttrForObj


class MarkdownInfo(AbstractMarkdownInfo):
    def __init__(self, post: frontmatter.Post):
        super().__init__()
        # 需要设置的
        # 草稿、发布
        self.wpStatus = None
        # 评论
        self.wpComment = None
        # 分类
        self.wpCategory = None
        # wp站点元信息
        self.wp = WordPressMeta()
        # 初始化yaml和content
        self.post = post if type(post) is frontmatter.Post and post else None
        self.md_content, self.md_yaml = self.post.content, self.post.metadata if self.post else None
        # 初始化属性赋值
        self.__setAttr()

    def getTags(self):
        return self.tags

    def getTitle(self):
        return self.title

    def getStatus(self):
        return self.wpStatus

    def getContent(self):
        return self.md_content

    def getWpComment(self):
        return self.wpComment

    def getWpCategory(self):
        return self.wpCategory

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


# 解析markdown
def getMarkdown(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        parseMd = frontmatter.load(f)
    if type(parseMd.metadata) is dict and "wp" in parseMd.metadata and parseMd.metadata['wp']:
        wpMeta = dict(parseMd.metadata['wp'])
        obj = WordPressMeta()
        setAttrForObj(obj, wpMeta)
        parseMd.metadata['wp'] = obj
    return MarkdownInfo(parseMd)


# test
path = r"E:\Project\PythonProject\postWordpress\测试.md"
markdown = getMarkdown(path)
print(markdown.title, markdown.wp.wpLink)
# 更新测试
print("-----update-----")
wpmeta = WordPressMeta()
wpmeta.wpLink = "测试"
markdown.updateYaml({"title": '测试更新', 'wp': wpmeta})
print(markdown.title, markdown.wp.wpLink, markdown.post.metadata)
