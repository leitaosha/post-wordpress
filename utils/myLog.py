# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/5/2
import logging
import os.path
from utils.config import BASE_PROJECT_PATH

# 创建一个日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 定义日志记录的格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
default_log_path = os.path.join(BASE_PROJECT_PATH, 'log.txt')

file_handler = None


def log_to_file(log_file: str = default_log_path) -> logging.Logger:
    # 创建一个文件处理器，用于将日志记录追加到文件中
    file_handler = logging.FileHandler(log_file, delay=True)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def flush_log():
    file_handler.flush() if type(file_handler) is logging.FileHandler else None


def log_to_console(console: bool = False):
    # 创建一个控制台处理器，用于将日志记录输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    # 将处理器添加到日志记录器
    logger.addHandler(console_handler) if console else None
