# coding:utf-8
from businessView.cashierView import CashierView
from businessView.loginView import LoginView
from airtest.core.api import *
from tools.common import Common
import unittest,logging, time


class CashierTest(unittest.TestCase):
    config = Common.read_config('/db/goodsSQL.ini')
    sql = Common.get_content(config, "商品库存查询语句", "sql")

    def setUp(self):
        connect_device('Android:///CLB7N18403015180')
        start_app('com.gengcon.android.jxc')

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 获取原始库存数
    def get_goods_qty(self):
        login = LoginView()
        num = int(login.select_data_from_db(self.sql)[0]['stockQty'])
        return num

    # 正常收银
    def test_01_cashier_case(self):
        '''
        正常收银
        '''
        num1 = self.get_goods_qty() - 1
        self.login_action()
        # 销售之前商品库存数
        logging.info('开始收银')
        cashier = CashierView()
        cashier.cashier_action()
        time.sleep(1)
        num2 = int(cashier.select_data_from_db(self.sql)[0]['stockQty'])
        sales_order_num = cashier.get_sales_order_num()
        cashier.save_csv_data('../data/salesOrderNum.csv', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(num1, num2, r'收银商品库存未减少')

    # 改价后成功销售
    def test_02_modfiy_price_case(self):
        '''
        改价后用例
        '''
        self.login_action()
        cashier = CashierView()
        cashier.cashier_modfiy_price()
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(cashier.get_order_price(), r'￥20.00')

    # 打折后成功销售
    def test_03_discount_case(self):
        '''
        打折后正常销售
        '''
        self.login_action()
        cashier = CashierView()
        cashier.cashier_discount_action()
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(cashier.get_order_price(), r'￥12.00')

    # 挂单后销售
    def test_04_hangup_case(self):
        '''
        单据挂单后在销售
        '''
        self.login_action()
        cashier = CashierView()
        cashier.hangup_order_cashier_action()
        self.assertTrue(cashier.check_transaction_success_status())

    # 结账界面打折
    def test_05_zhe_case(self):
        '''
        结账界面打折
        '''
        self.login_action()
        cashier = CashierView()
        cashier.pay_bill_zhe_action()
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(cashier.get_order_price(), r'￥60.00')

    # 结账界面抹零
    def test_06_mo_case(self):
        '''
        结账界面抹零
        '''
        self.login_action()
        cashier = CashierView()
        cashier.pay_bill_mo_action()
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(cashier.get_order_price(), r'￥115.00')

    def tearDown(self):
        clear_app('com.gengcon.android.jxc')
        stop_app('com.gengcon.android.jxc')


if __name__ == '__main__':
    unittest.main()
