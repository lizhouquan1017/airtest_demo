# coding:utf-8
from businessView.purchasereturnView import PurchaseReturnView
from businessView.purchasereturnorderView import PurchaseReturnOrderView
from businessView.loginView import LoginView
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.readCfg import ReadData

import time


class PurchaseReturnTest(StartEnd, TestCase_):

    config1 = Common.read_config('/db/purchasereturnSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 获取操作之前商品库存数
    def get_goods_num(self):
        login = LoginView()
        num = int(login.select_data_from_db(self.sql2)[0]['stockQty'])
        return num

    # 原始采购单退货
    def test_01_original_purchase_return_case(self):
        """原始采购退货成功"""
        self.login_action()
        # 采购退货之前库存
        num1 = self.get_goods_num() - 1
        purchasereturn = PurchaseReturnView()
        # data = purchasereturn.get_csv_data('../data/purchaseOrderNum.csv', 1)
        purchase_order_num = ReadData().get_data('purchase_order', 'num')
        purchasereturn.original_purchasereturn_action(purchase_order_num)
        time.sleep(1)
        # 采购退货之后库存
        num2 = purchasereturn.check_stock_qty()
        ordernum = purchasereturn.get_purchase_return_ordernum()
        # purchasereturn.save_csv_data('../data/purchasereturnOrderNum.csv', ordernum)
        ReadData().write_data('purchase_return_order', 'num', ordernum)
        self.assertTrue(purchasereturn.check_purchase_return_success_status())
        self.assertEqual(num1, num2)

    # 采购退货单作废
    def test_02_obsolete_putchase_return_case(self):
        """作废采购单退货单"""
        self.login_action()
        # 作废之前库存查询
        num1 = self.get_goods_num() + 1
        pruchasereturnorder = PurchaseReturnOrderView()
        # ordernum = pruchasereturnorder.get_csv_data('../data/purchasereturnOrderNum.csv', 1)[0]
        ordernum = ReadData().get_data('purchase_return_order', 'num')
        pruchasereturnorder.obsolete_purchase_return_order(1, ordernum)
        time.sleep(3)
        num2 = pruchasereturnorder.check_stock_qty()
        inv_ordernum = pruchasereturnorder.check_invalid_purchase_return_ordernum()
        # 设置检查点
        self.assertEqual(num1, num2)
        self.assertTrue(ordernum, inv_ordernum)

    # 采购直接退货
    def test_03_direct_purchase_return_case(self):
        """采购退货直接退货"""
        self.login_action()
        # 采购退货之前库存
        num1 = self.get_goods_num() - 1
        purchasereturn = PurchaseReturnView()
        purchasereturn.direct_puechaseretur_action()
        time.sleep(1)
        # 采购退货之后库存
        num2 = purchasereturn.check_stock_qty()
        ordernum = purchasereturn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num', ordernum)
        self.assertTrue(purchasereturn.check_purchase_return_success_status())
        self.assertEqual(num1, num2)

    # 复制订单用例
    def test_04_copy_purchase_return_order_case(self):
        """复制订单"""
        self.login_action()
        num1 = self.get_goods_num() - 1
        purchasereturnorder = PurchaseReturnOrderView()
        # ordernum = purchasereturnorder.get_csv_data('../data/purchasereturnOrderNum.csv', 1)[0]
        ordernum = ReadData().get_data('purchase_return_order', 'num')
        purchasereturnorder.copy_purchase_return_order(2, ordernum)
        order_num = purchasereturnorder.get_purchase_return_order_num()
        # purchasereturnorder.save_csv_data('../data/purchasereturnOrderNum.csv', order_num)
        ReadData().write_data('purchase_return_order', 'num', order_num)
        time.sleep(2)
        num2 = purchasereturnorder.check_stock_qty()
        # 设置检查点
        self.assertTrue(purchasereturnorder.check_transaction_success_status())
        self.assertEqual(num1, num2)

