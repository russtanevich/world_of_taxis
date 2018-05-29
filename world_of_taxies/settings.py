# -*- coding: utf-8 -*-
"""SETTINGS module """
import logging


class LogVars(object):

    EVENT = {
        "name": "WOT_EVENT",
        "filename": "events.log",
        "level": logging.INFO,
        "template": "%(filename)-12s[ln:%(lineno)4d]# %(levelname)-8s [%(asctime)s]  %(message)s"
    }

    STAT = {
        "name": "WOT_STAT",
        "filename": "stats.log",
        "level": logging.INFO,
        "template": "[%(asctime)s]  %(message)s"
    }


def create_logger(name, level, filename, template):

    logger = logging.getLogger(name)
    logger.setLevel(level)
    fh = logging.FileHandler(filename)
    formatter = logging.Formatter(template)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


if __name__ != "__main__":
    logger = create_logger(**LogVars.EVENT)
    statistic = create_logger(**LogVars.STAT)



