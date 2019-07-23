# coding:utf-8
from businessView.purchaseView import PurchaseView
from businessView.purchaseorderView import PurchaseOrderView
from businessView.loginView import LoginView
from tools.common import Common
from airtest.core.api import *
import unittest, time


class PurchaseTest(unittest.TestCase):
    config1 = Common.read_config('/db/purchaseSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config1, "采购单单号查询语句", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")

    def setUp(self):
        connect_device('Android:///CLB7N18403015180')
        start_app('com.gengcon.android.jxc')

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 未操作前获取商品库存数
    def get_goods_num(self):
        login = LoginView()
        num = int(login.select_data_from_db(self.sql2)[0]['stockQty'])
        return num

    # 正常采购用例
    def test_01_purchase_case(self):
        '''
        正常采购成功用例
        '''
        self.login_action()
        num1 = self.get_goods_num()
        purchase = PurchaseView()
        purchase.purchase_success_action()
        order_num = purchase.get_purchase_order_num()
        purchase.save_csv_data('../data/purchaseOrderNum.csv', order_num)
        num2 = purchase.select_data_from_db(self.sql2)[0]['stockQty']
        db_order_num = purchase.select_data_from_db(self.sql1)[0]['order_code']
        purchase_num = purchase.get_purchase_num()
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase.check_transaction_success_status())
        self.assertEqual(order_num, db_order_num, r'采购单单号与数据库中一致')
        self.assertEqual(num1+purchase_num, num2, r'采购后库存增加正常')

    # 采购单作废用例
    def test_02_obsolete_order_case(self):
        self.login_action()
        num1 = self.get_goods_num() - 1
        purchaseorder = PurchaseOrderView()
        ordernum = purchaseorder.get_csv_data('../data/purchaseOrderNum.csv', 1)[0]
        purchaseorder.obsolete_purchase_order(1, ordernum)
        time.sleep(3)
        num2 = purchaseorder.check_stock_qty()
        inv_ordernum = purchaseorder.check_invalid_purchase_ordernum()
        # 设置检查点
        self.assertEqual(num1, num2)
        self.assertTrue(ordernum, inv_ordernum)

    # 采购改价用例
    def test_03_purchase_modfiy_price_case(self):
        '''
        采购进货修改价格采购成功
        '''
        self.login_action()
        num1 = self.get_goods_num()
        purchase = PurchaseView()
        purchase.purchase_modfiy_price_action()
        order_num = purchase.get_purchase_order_num()
        purchase.save_csv_data('../data/purchaseOrderNum.csv', order_num)
        num2 = purchase.select_data_from_db(self.sql2)[0]['stockQty']
        db_order_num = purchase.select_data_from_db(self.sql1)[0]['order_code']
        purchase_num = purchase.get_purchase_num()
        purchase_price = purchase.get_order_price()
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase.check_transaction_success_status())
        self.assertEqual(order_num, db_order_num, r'采购单单号与数据库中一致')
        self.assertEqual(num1+purchase_num, num2, r'采购后库存增加正常')
        self.assertEqual(purchase_price, r'￥30.00')

    # 复制订单用例
    def test_04_copy_order_case(self):
        '''
        复制订单
        '''
        self.login_action()
        num1 = self.get_goods_num()
        purchaseorder = PurchaseOrderView()
        ordernum = purchaseorder.get_csv_data('../data/purchaseOrderNum.csv', 1)[0]
        purchaseorder.copy_purchase_order(2, ordernum)
        order_num = purchaseorder.get_purchase_order_num()
        purchaseorder.save_csv_data('../data/purchaseOrderNum.csv', order_num)
        time.sleep(2)
        num2 = purchaseorder.check_stock_qty()
        # 设置检查点
        self.assertTrue(purchaseorder.check_transaction_success_status())
        self.assertEqual(num1+1, num2)

    def tearDown(self):
        clear_app('com.gengcon.android.jxc')
        stop_app('com.gengcon.android.jxc')


if __name__ == '__main__':
    unittest.main()
