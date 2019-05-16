# -*- coding: UTF-8 -*-


import logging
import config
import os
from logging.handlers import RotatingFileHandler


class MyLogging:
    def __init__(self):
        self.log_path = config.log_path
        self.loggers = {}  # channel:logging
        self.handle_type = config.handle_type
        self.formatter = logging.Formatter('%(asctime)s - %(filename)s-%(lineno)s: %(message)s')
        self.with_formatter = config.formatter
        self.pid = os.getpid()
        self.__mkdir(self.log_path)

    def __mkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def __get_logging(self, prefix='log'):
        logger = self.loggers.get(prefix, None)
        if logger is None:
            logger = logging.getLogger(prefix)
            path = os.path.join(self.log_path, prefix)
            if not os.path.exists(path):
                os.mkdir(path)
            if self.handle_type == 't':
                handler = logging.handlers.TimedRotatingFileHandler(filename=path + '/' + prefix + str(self.pid) + '.log',
                                                                    when='D',
                                                                    interval=1,
                                                                    backupCount=0
                                                                    )
            elif self.handle_type == 'f':
                handler = logging.handlers.RotatingFileHandler(filename=path + '/' + prefix + '.log',
                                                               mode='a',
                                                               maxBytes=1024*1024*1024,  # 1G
                                                               backupCount=0
                                                               )
            if self.with_formatter:
                handler.setFormatter(self.formatter)
            logger.addHandler(handler)
            self.loggers[prefix] = logger
        return logger

    def debug(self, prefix, message):
        logger = self.__get_logging(prefix)
        logger.debug(message)

    def debug(self, message):
        self.__get_logging().debug(message)

    def info(self, prefix, message):
        logger = self.__get_logging(prefix)
        logger.info(message)

    def info(self, message):
        self.__get_logging().info(message)

    def warning(self, prefix, message):
        logger = self.__get_logging(prefix)
        logger.warning(message)

    def warning(self, message):
        self.__get_logging().warning(message)
