import logging, os
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, name=None, format=None, ):
        if not format:
            format = '%(asctime)s %(name)s %(funcName)s %(levelname)s (%(lineno)d) %(message)s'
        log_formatter = logging.Formatter(format)
        log_dir = os.path.join(os.path.abspath(os.path.curdir), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        print("name: {}".format(name))
        logFile = os.path.join(log_dir, name)
        if os.path.exists(logFile):
            os.remove(logFile)
        my_handler = RotatingFileHandler(
            logFile,
            mode='a',
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8',
            delay=0
        )
        my_handler.setFormatter(log_formatter)
        my_handler.setLevel(logging.INFO)

        self.__logger = logging.getLogger(__file__)  # 如果没有__name__那么调取的就是root logger, 即所有的消息
        self.__logger.setLevel(logging.INFO)
        self.__logger.addHandler(my_handler)

    def info(self, msg):
        self.__logger.info(msg)

    def debug(self, msg):
        self.__logger.debug(msg)

    def warn(self, msg):
        self.__logger.warn(msg)

    def error(self, msg):
        self.__logger.error(msg)

    def critical(self, msg):
        self.__logger.critical(msg)