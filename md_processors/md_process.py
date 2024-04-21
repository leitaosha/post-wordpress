# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/20


from concurrent.futures import ThreadPoolExecutor

from md_processors.TagProcessor import TagProcessor
from md_processors.CategoryProcessor import CategoryProcessor
from utiles.config import *
from md_processors.WPMarkdown import WPMarkdown, getMarkdown

MDProcessors = [
    TagProcessor,
    CategoryProcessor,

]


def process(markdown: WPMarkdown):
    with ThreadPoolExecutor(THREAD_POOL_MAX_WORKER) as executor:
        futures = []
        for processor in MDProcessors:
            processor = processor(markdown, executor)
            future = executor.submit(processor.preprocess)
            futures.append(future)
            markdown = processor.markdown
    return markdown


mdPath = r'E:\Project\PythonProject\postWordpress\测试.md'
md = getMarkdown(mdPath)
print(md.wp)
md2 = process(md)
# print(md.wp.tags, md.wp.categories)
print(md2.wp.tags, md2.wp.categories)
