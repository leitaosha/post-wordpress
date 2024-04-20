# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
import time
from concurrent.futures import ThreadPoolExecutor
from posts.tag import Tag
from concurrent.futures import as_completed


def submitTag(tagName: str):
    return Tag(tagName).create()


def deleteTag(tagName: str):
    return Tag(tagName).delete()


tag_list = [
    '线程1',
    '线程2',
    '线程3',
    '线程4',
]
# 创建线程池
with ThreadPoolExecutor(max_workers=8) as executor:
    start_time = time.time()
    # 提交任务给线程池
    futures = [executor.submit(deleteTag, tag) for tag in tag_list]

    # 获取结果
    for future in as_completed(futures):
        try:
            print(future.result())
        except Exception as e:
            print(f"An error occurred: {e}")
        # 记录结束时间
        end_time = time.time()
    execution_time = end_time - start_time
print(f"All requests completed.\nExecution time: {execution_time} seconds")
