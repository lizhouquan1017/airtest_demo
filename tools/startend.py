# coding:utf-8

import unittest
from airtest.core.api import *
import yaml, logging.config

yaml.warnings({'YAMLLoadWarning': False})
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/log.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger()

with open('../config/devices.yaml', 'r', encoding='gbk') as file:
    data = yaml.load(file)

    devicesname = data['devicesname']
    package = data['package']


class StartEnd(unittest.TestCase):

    def setUp(self):
        connect_device('Android:///' + devicesname)
        wake()
        start_app(package)

    def tearDown(self):
        clear_app(package)
        stop_app(package)

    def rerun(self, setup, teardown, n):
        def wrapper(func):
            def inner(*args, **kwargs):
                for i in range(n):
                    try:
                        print('第%s次尝试' % i)
                        ret = func(*args, **kwargs)
                        return ret
                    except Exception:
                        print('have a error')
                        setup(*args)
                        teardown(*args)
                raise Exception
            return inner
        return wrapper
