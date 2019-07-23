# coding:utf-8

import unittest
from airtest.core.api import *
import yaml

yaml.warnings({'YAMLLoadWarning': False})
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
