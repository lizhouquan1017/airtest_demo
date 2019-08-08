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
        start_app(package)

    def tearDown(self):
        clear_app(package)
        stop_app(package)

