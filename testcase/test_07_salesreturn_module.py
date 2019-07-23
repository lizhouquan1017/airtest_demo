# coding:utf-8
from businessView.salesreturnView import SalesReturnView
from businessView.loginView import LoginView
from airtest.core.api import *
from tools.common import Common
import unittest,time,logging


class SalesReturnTest(unittest.TestCase):

    config = Common.read_config('/db/goodsSQL.ini')
    sql = Common.get_content(config, "商品库存查询语句", "sql")

    def setUp(self):
        connect_device('Android:///CLB7N18403015180')
        start_app('com.gengcon.android.jxc')

    # 销售退货正常
    def test_01_salesreturn(self):
        '''
        销售退货正常
        '''
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])
        # 获取退货之前的商品库存数
        num1 = int(login.select_data_from_db(self.sql)[0]['stockQty']) + 1
        salesreturn = SalesReturnView()
        data = salesreturn.get_csv_data('../data/salesOrderNum.csv', 1)
        salesreturn.salesreturn_action(data[0])
        time.sleep(1)
        # 获取退货之后的商品库存数
        num2 = int(salesreturn.select_data_from_db(self.sql)[0]['stockQty'])
        logging.info(num1)
        logging.info(num2)
        self.assertTrue(salesreturn.check_salesreturn_success_status())
        self.assertEqual(num1, num2)

    def tearDown(self):
        clear_app('com.gengcon.android.jxc')
        stop_app('com.gengcon.android.jxc')


if __name__ == '__main__':
    unittest.main()
