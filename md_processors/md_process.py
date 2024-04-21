# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/20
import time
from concurrent.futures import ThreadPoolExecutor, wait

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
        wait(futures)
    return markdown


# mdPath = r'E:\Project\PythonProject\postWordpress\测试.md'
# md = getMarkdown(mdPath)
# print(md.wp)
# starttime = time.time()
# md2 = process(md)
# endtime = time.time()
# print(md.wp.tags, md.wp.categories)
# print(md2.wp)
# print(endtime-starttime)
