# coding:gbk
import unittest, time, sys
from BeautifulReport import BeautifulReport

path = 'D:\\airtest_demo\\'
sys.path.append(path)

test_dir = '../testcase'
report_dir = 'D:/software/jenkins/workspace/jxc_autoTest/report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = 'jxcreport.html'
BeautifulReport(discover).report(filename=report_name, description='进销存Android端全流程测试报告', report_dir=report_dir)
