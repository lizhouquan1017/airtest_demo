# coding = utf-8
import unittest, time, sys
from BeautifulReport import BeautifulReport

path = 'D:\\airtest_demo\\'
sys.path.append(path)

test_dir = '../testcase'
report_dir = '../report'
test_dir1 = '../smokecase'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_06_cashier_module.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+' test_report.html'
BeautifulReport(discover).report(filename=report_name, description='jxc Android app test report',report_dir=report_dir)
