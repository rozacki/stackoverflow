import logging


def get_logger(name='main'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

