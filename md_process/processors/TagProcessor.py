# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/20


from md_process.WPMarkdown import WPMarkdown
from concurrent.futures import ThreadPoolExecutor
from md_process.processors.MDProcessor import MDProcessor
from posts.tag import Tag


class TagProcessor(MDProcessor):

    def __init__(self, markdown: WPMarkdown, thread_pool_executor: ThreadPoolExecutor):
        # process tags
        super().__init__(markdown, thread_pool_executor)
        self.tags = markdown.tags

    def preprocess(self):
        futures = [self.thread_pool_executor.submit(self.createTag, tagName) for tagName in self.tags]
        return futures

    def createTag(self, tagName):
        obj = Tag(tagName)
        obj.create()
        self.markdown.wp.tags.append(obj.id)
        return obj
