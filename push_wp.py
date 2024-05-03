# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
import copy
import logging
import os.path
import sys
import time
from utils.myLog import log_to_file
import frontmatter
from md_processors.WPMarkdown import getMarkdown
from md_processors.md_process import process
from urllib.parse import unquote


# def ob_push_wp(mdPath):
#     # 原生md
#     mdOrigin = getMarkdown(mdPath)
#     md_copy = copy.deepcopy(mdOrigin)
#     clearConsole()
#     try:
#         console("# 这里将暂时作为控制台")
#         console("### 正在推送中...")
#         # 处理md
#         mdProcessed = process(mdOrigin)
#         # markdown推送
#         post = mdProcessed.wp
#         text = post.create()
#         if text.status:
#             console("### 推送成功")
#         else:
#             console("### 推送失败")
#             raise CustomError('### 推送失败')
#         console("#### " + text.msg)
#         console("### 即将返回...")
#         backNum()
#         # 获取返回数据
#         new_attributes = {
#             'id': post.id,
#             "link": unquote(post.link),
#             'status': post.status,
#         }
#         # 仅修改wp字段
#         mdOrigin.post.metadata['wp'].update(new_attributes) if 'wp' in mdOrigin.post.metadata else ''
#         # 写入markdown
#         with open(mdPath, 'w', encoding='utf-8') as f:
#             f.write(frontmatter.dumps(mdOrigin.post))
#     except Exception as e:
#         console(e.__str__())
#         console('## 出错了，不要担心，文档不会丢失！！')
#         backNum()
#         # 写入markdown
#         with open(mdPath, 'w', encoding='utf-8') as f:
#             f.write(frontmatter.dumps(md_copy.post))

def ob_push_wp(mdPath):
    # 原生md
    mdOrigin = getMarkdown(mdPath)
    md_copy = copy.deepcopy(mdOrigin)
    # 删除原文
    clearConsole()
    log.info('这将短暂作为控制台使用')
    log.info(f'开始提交文章 -> {mdOrigin.title}')
    try:
        log.info("正在推送中...")
        text = run(mdOrigin)
        log.info(text.msg)
        if text.status:
            log.info("推送/更新 成功！")
        else:
            log.error("推送 失败！")
        time.sleep(3)
        # 获取返回数据
        post = mdOrigin.wp
        new_attributes = {
            'id': post.id,
            "link": unquote(post.link),
            'status': post.status,
        }
        # 仅修改wp字段
        mdOrigin.post.metadata['wp'].update(new_attributes) if 'wp' in mdOrigin.post.metadata else ''
        # 写入markdown
        with open(mdPath, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(mdOrigin.post))
    except Exception as e:
        log.error(e.__str__())
        log.error(e)
        log.error('出错了，不要担心，文档不会丢失！！')
        time.sleep(3)
        # 写入markdown
        with open(mdPath, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(md_copy.post))


def run(mdOrigin):
    # 处理md
    mdProcessed = process(mdOrigin)
    # markdown推送
    post = mdProcessed.wp
    return post.create()


def console(msg: str):
    with open(MD_PATH, 'a', encoding='utf-8') as f:
        f.write("\n" + msg + "\n")


def clearConsole():
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write('')


def howLog(argv: list) -> logging.Logger:
    """
    check path and log to file
    :param argv: sys
    :return:
    """
    if len(argv) > 1 and os.path.exists(os.path.normpath(argv[1].replace('/', '\\'))):
        logg = log_to_file(argv[1])
        return logg
    else:
        logg = log_to_file()
        logg.error('There is no path params or path does not exist！ Exit!!!')
        sys.exit(1)


if __name__ == '__main__':
    # get log
    log = howLog(sys.argv)
    MD_PATH = sys.argv[1]
    ob_push_wp(MD_PATH)

    # MD_PATH = r'E:\笔记\博客\推送测试.md'
    # ob_push_wp(MD_PATH)
    # print(sys.argv)
