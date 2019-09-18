# coding:utf-8
from businessView.purchaseView import PurchaseView
from businessView.loginView import LoginView
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.readCfg import ReadData
import time


class PurchaseOrderTest(StartEnd, TestCase_):

    config1 = Common.read_config('/db/purchaseSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config1, "采购单单号查询语句", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")
    sql3 = Common.get_content(config1, "供应商新状态", "sql")

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 未操作前获取商品库存数
    def get_goods_num(self, name):
        login = LoginView()
        goods = login.select_data_from_db(self.sql2)
        for i in range(0, len(goods)):
            if goods[i]['goods_name'] == name:
                num = goods[i]['stockQty']
                return int(num)

    # 采购单作废用例
    def test_02_obsolete_order_case(self):
        """采购单作废用例"""
        self.login_action()
        num1 = self.get_goods_num() - 1
        purchaseorder = PurchaseOrderView()
        # ordernum = purchaseorder.get_csv_data('../data/purchaseOrderNum.csv', 1)[0]
        ordernum = ReadData().get_data('purchase_order', 'num')
        purchaseorder.obsolete_purchase_order(1, ordernum)
        time.sleep(3)
        num2 = purchaseorder.check_stock_qty()
        inv_ordernum = purchaseorder.check_invalid_purchase_ordernum()
        # 设置检查点
        self.assertEqual(num1, num2)
        self.assertTrue(ordernum, inv_ordernum)

    # 复制订单用例
    def test_04_copy_order_case(self):
        """复制订单"""
        self.login_action()
        num1 = self.get_goods_num()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num')
        purchaseorder.copy_purchase_order(2, ordernum)
        order_num = purchaseorder.get_purchase_order_num()
        ReadData().write_data('purchase_order', 'num', order_num)
        time.sleep(2)
        num2 = purchaseorder.check_stock_qty()
        # 设置检查点
        self.assertTrue(purchaseorder.check_transaction_success_status())
        self.assertEqual(num1+1, num2)
