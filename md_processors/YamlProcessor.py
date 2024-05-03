# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/30
from concurrent.futures import ThreadPoolExecutor
from utils.util import setAttrForObj
from md_processors.AbstractMDProcessor import MDProcessor
from md_processors.WPMarkdown import WPMarkdown


class YamlProcessor(MDProcessor):

    def __init__(self, markdown: WPMarkdown, thread_pool_executor: ThreadPoolExecutor):
        super().__init__(markdown, thread_pool_executor)
        self.md_yaml = markdown.md_yaml
        self.wp = self.markdown.wp

    def preprocess(self):
        self.thread_pool_executor.submit(self.firstYaml)
        pass

    def firstYaml(self):
        """
        first level yaml fields
        :return:
        """
        setAttrForObj(self.wp, self.md_yaml['wp']) if self.md_yaml['wp'] else None
        self.wp.title = self.md_yaml['title'] if 'title' in self.md_yaml else None
        self.wp.excerpt = self.md_yaml['excerpt'] if 'excerpt' in self.md_yaml else None
