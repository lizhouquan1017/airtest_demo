# -*- coding:utf-8 -*-
import logging.config
import os.path


class Logger(object):

    def __init__(self, logger):
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/log.conf')
        logging.config.fileConfig(log_file_path)
        self.logger = logging.getLogger(logger)

    def getlog(self):
        return self.logger
