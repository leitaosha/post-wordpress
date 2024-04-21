# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/20

from md_process.processors.TagProcessor import TagProcessor
from concurrent.futures import ThreadPoolExecutor
from utiles.config import *

MDProcessors = [
    TagProcessor,
]


def process(markdown):
    with ThreadPoolExecutor(THREAD_POOL_MAX_WORKER) as executor:
        futures = []
        for processor in MDProcessors:
            processor = processor(markdown, executor)
            future = executor.submit(processor.preprocess)
            futures.append(future)
            markdown = processor.markdown
    return markdown
