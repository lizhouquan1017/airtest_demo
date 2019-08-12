# coding:gbk
import unittest
import time
import sys
import yaml
from BeautifulReport import BeautifulReport
from tools.PushApkToDevices import push_apk_to_devices

with open('../config/devices.yaml', 'r', encoding='gbk') as file:
    data = yaml.load(file)
    devicesname = data['devicesname']

push_apk_to_devices(devicesname)
time.sleep(3)
path = 'D:\\airtest_demo\\'
sys.path.append(path)

test_dir = '../testcase'
report_dir = 'D:/software/jenkins/workspace/jxc_autoTest/report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = 'jxcreport.html'
BeautifulReport(discover).report(filename=report_name, description='进销存Android端全流程测试报告', report_dir=report_dir)
