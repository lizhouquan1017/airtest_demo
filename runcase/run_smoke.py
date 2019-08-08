# coding = utf-8
import unittest, time, sys
from BeautifulReport import BeautifulReport

path = 'D:\\airtest_demo\\'
sys.path.append(path)

report_dir = 'D:/software/jenkins/workspace/jxc_autoTest/report'
test_dir = '../smokcase'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = 'jxcreport.html'
BeautifulReport(discover).report(filename=report_name, description='jxc Android app test report', report_dir=report_dir)
