# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/21


from md_process.processors.AbstractMDProcessor import MDProcessor
from md_process.WPMarkdown import WPMarkdown
from concurrent.futures import ThreadPoolExecutor, as_completed

from posts.category import Category


class CategoryProcessor(MDProcessor):

    def __init__(self, markdown: WPMarkdown, thread_pool_executor: ThreadPoolExecutor):
        # process tags
        super().__init__(markdown, thread_pool_executor)
        self.categories = markdown.categories

    def preprocess(self):
        futures = [self.thread_pool_executor.submit(self.createCategory, categoryName) for categoryName in self.categories]
        return futures

    def createCategory(self, categoryName: str):
        obj = Category(categoryName)
        obj.create()
        self.markdown.wp.categories.append(obj.id)
        return obj
