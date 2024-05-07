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
from md_processors.WPMarkdown import getMarkdown, WPMarkdown
from md_processors.md_process import process
from urllib.parse import unquote
from utils import util


def ob_push_wp(md: WPMarkdown):
    # 删除原文
    clearConsole()
    logg.info("{::^80}".format("NEW POST AT" + " " + str(util.getTody()) + " " + str(util.getWeekday())))
    log.info(f'开始提交文章 -> {md.title}')
    log.info("正在推送中...")
    try:
        text = run(md)
        log.info(text.msg)
        if text.status:
            log.info("推送/更新 成功！")
        else:
            log.error("推送 失败！")
    except TimeoutError as te:
        log.error(te)
    finally:
        log.info('即将返回文档！')
    flush_console()
    time.sleep(4)
    # 获取返回数据
    post = md.wp
    new_attributes = {
        'id': post.id,
        "link": unquote(post.link),
        'status': post.status,
    }
    # 仅修改wp字段
    md.post.metadata['wp'].update(new_attributes) if 'wp' in md.post.metadata else ''
    return md


def writeMd(mdPath: str, md: WPMarkdown):
    # 写入markdown
    with open(mdPath, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(md.post))


# @timeout(50)
def run(md: WPMarkdown):
    # 处理md
    mdProcessed = process(md)
    # markdown推送
    post = mdProcessed.wp
    return post.create()


def console(msg: str):
    """
    write to file
    :param msg:
    :return:
    """
    with open(MD_PATH, 'a', encoding='utf-8') as f:
        f.write("\n" + msg + "\n")


def flush_console():
    """
    Solve the problem that the log cannot be refreshed in time
    :return:
    """
    with open(MD_PATH, 'a', encoding='utf-8') as f:
        f.write("\n")


def clearConsole():
    """
    delete content of file
    :return:
    """
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write('')


def howLog(argv: list) -> logging.Logger:
    """
    check path and log to file
    :param argv: sys
    :return:
    """
    if len(argv) > 1 and os.path.exists(os.path.normpath(argv[1].replace('/', '\\'))):
        logg = log_to_file()
        logg = log_to_file(log_file=argv[1])
        return logg
    else:
        logg = log_to_file()
        logg.error('There is no path params or path does not exist！ Exit!!!')
        sys.exit(1)


if __name__ == '__main__':
    # get log
    log = howLog(sys.argv)
    MD_PATH = sys.argv[1]
    # 测试
    # log = log_to_file()
    # MD_PATH = r'E:\笔记\博客\推送测试.md'
    # 原生md
    mdOrigin = getMarkdown(MD_PATH)
    md_copy = copy.deepcopy(mdOrigin)
    # 删除文档以作控制台
    clearConsole()
    # 推送
    try:
        mdText = ob_push_wp(mdOrigin)
        # 写入文档
        writeMd(MD_PATH, mdText)
    except Exception as e:
        log.error(e.__str__())
        writeMd(MD_PATH, md_copy)

    # ob_push_wp(MD_PATH)
    # print(sys.argv)
