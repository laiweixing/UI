import logging
import time
import os

from config_path.path_file import read_file
from . Yaml import MyConfig
from . TimeConversion import return_y_d_m


def _logger():
    logs_day = MyConfig('logs_save').config
    for day in return_y_d_m(ends_day_time=logs_day):
        log_dir = read_file('log', day + '.log')
        exists = os.path.exists(log_dir)
        if exists:
            os.remove(log_dir)
    log_path = read_file('log', f'{time.strftime("%Y-%m-%d")}.log')
    logging.basicConfig(format="%(asctime)s %(filename)s: [%(levelname)s]: %(message)s",
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S -> %A || -> ',
                        filename=log_path,
                        filemode='a+')
    return logging


logger = _logger()
