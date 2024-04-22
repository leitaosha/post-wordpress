# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/20
from concurrent.futures import ThreadPoolExecutor, wait

from md_processors.CategoryProcessor import CategoryProcessor
from md_processors.ContentProcessor import ContentProcessor
from md_processors.TagProcessor import TagProcessor
from md_processors.WPMarkdown import WPMarkdown
from utils.config import *

# processors, All formats and content are processed in here.
MDProcessors = [
    TagProcessor,
    CategoryProcessor,
    ContentProcessor,
]


def process(markdown: WPMarkdown):
    """
    Markdown processed into submittable format: tags, categories
    :param markdown:
    :return:
    """
    with ThreadPoolExecutor(THREAD_POOL_MAX_WORKER) as executor:
        futures = []
        for processor in MDProcessors:
            processor = processor(markdown, executor)
            future = executor.submit(processor.preprocess)
            futures.append(future)
            markdown = processor.markdown
        wait(futures)
    return markdown


