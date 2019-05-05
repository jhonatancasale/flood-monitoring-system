# -*- coding: utf-8 -*-

import logging
from sys import stdout


def get_logger(name: str, log_file: str = None, level=logging.DEBUG,
               formatter='%(asctime)s:%(name)s:%(levelname)s:%(message)s'
               ):
    """Configure and get a new logger"""

    handler = logging.FileHandler(log_file) if log_file else logging.StreamHandler(stdout)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(formatter))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
