# coding:utf-8
from businessView.cashierView import CashierView
from businessView.loginView import LoginView
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from businessView.salesorderView import SalesOrderView
from businessView.salesreturnView import SalesReturnView
from businessView.salesrorderreturnView import SalesOrderReturnView
from tools.readCfg import ReadData
import time
import logging


class CashierTest(StartEnd, TestCase_):
    config = Common.read_config('/db/goodsSQL.ini')
    sql = Common.get_content(config, "商品库存查询语句", "sql")

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
        """正常收银"""
        num1 = self.get_goods_qty() - 1
        self.login_action()
        # 销售之前商品库存数
        logging.info('开始收银')
        cashier = CashierView()
        cashier.cashier_action()
        time.sleep(1)
        num2 = int(cashier.select_data_from_db(self.sql)[0]['stockQty'])
        sales_order_num = cashier.get_sales_order_num()
        # cashier.save_csv_data('../data/salesOrderNum.csv', sales_order_num)
        ReadData().write_data('sale_order', 'num', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(num1, num2, r'收银商品库存未减少')

    # 销售单复制在销售
    def test_02_sales_order_copy_case(self):
        """销售单复制并生成新的销售单"""
        num1 = self.get_goods_qty() - 1
        self.login_action()
        salesorder = SalesOrderView()
        # ordernum = salesorder.get_csv_data('../data/salesOrderNum.csv', 1)[0]
        ordernum = ReadData().get_data('sale_order', 'num')
        salesorder.copy_pay_action(ordernum)
        time.sleep(3)
        sales_order_num = salesorder.get_sales_order_num()
        # salesorder.save_csv_data('../data/salesOrderNum.csv', sales_order_num)
        ReadData().write_data('sale_order', 'num', sales_order_num)
        # 设置检查点
        num2 = salesorder.check_stock_qty()
        self.assertEqual(num1, num2)
        self.assertTrue(salesorder.check_transaction_success_status())

    # 销售单作废
    def test_03_sales_order_obsolete_case(self):
        """销售单作废"""
        # 操作之前库存数
        num1 = self.get_goods_qty() + 1
        self.login_action()
        salesorder = SalesOrderView()
        # data = salesorder.get_csv_data('../data/salesOrderNum.csv', 1)
        ordernum = ReadData().get_data('sale_order', 'num')
        # 作废操作
        salesorder.obsolete_action(ordernum)
        time.sleep(3)
        # 设置检查点
        num2 = salesorder.check_stock_qty()
        inv_ordernum = salesorder.check_invalid_purchase_ordernum()
        self.assertEqual(num1, num2)
        self.assertEqual(ordernum, inv_ordernum)

    # 改价后成功销售
    def test_04_modfiy_price_case(self):
        """改价后销售"""
        self.login_action()
        cashier = CashierView()
        cashier.cashier_modfiy_price()
        sales_order_num = cashier.get_sales_order_num()
        # cashier.save_csv_data('../data/salesOrderNum.csv', sales_order_num)
        ReadData().write_data('sale_order', 'num', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(cashier.get_order_price(), r'￥20.00')

    # 原单退货改价
    def test_05_salesreturn_case(self):
        """原单改价退货"""
        self.login_action()
        # 获取退货之前的商品库存数
        num1 = self.get_goods_qty() + 1
        salesreturn = SalesReturnView()
        # data = salesreturn.get_csv_data('../data/salesOrderNum.csv', 1)
        saleorder = ReadData().get_data('sale_order', 'num')
        salesreturn.originalorder_return_action(saleorder)
        time.sleep(1)
        # 获取退货之后的商品库存数
        num2 = int(salesreturn.select_data_from_db(self.sql)[0]['stockQty'])
        ordernum = salesreturn.get_reutrn_order_num()
        # salesreturn.save_csv_data('../data/salesreturnOrderNum.csv', ordernum)
        ReadData().write_data('sale_return_order', 'num', ordernum)
        # 设置检查点
        self.assertEqual(salesreturn.get_return_order_total_amount(), r'￥10.00')
        self.assertTrue(salesreturn.check_salesreturn_success_status())
        self.assertEqual(num1, num2)

    # 打折后成功销售
    def test_06_discount_case(self):
        """打折后正常销售"""
        self.login_action()
        cashier = CashierView()
        cashier.cashier_discount_action()
        sales_order_num = cashier.get_sales_order_num()
        # cashier.save_csv_data('../data/salesOrderNum.csv', sales_order_num)
        ReadData().write_data('sale_order', 'num', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(cashier.get_order_price(), r'￥12.00')

    # 原单正常改价
    def test_07_salesreturn_case(self):
        """原单正常退货"""
        self.login_action()
        # 获取退货之前的商品库存数
        num1 = self.get_goods_qty() + 1
        salesreturn = SalesReturnView()
        # data = salesreturn.get_csv_data('../data/salesOrderNum.csv', 1)
        saleorder = ReadData().get_data('sale_order', 'num')
        salesreturn.originalorder_return_action(saleorder, modify=False)
        time.sleep(1)
        # 获取退货之后的商品库存数
        num2 = int(salesreturn.select_data_from_db(self.sql)[0]['stockQty'])
        ordernum = salesreturn.get_reutrn_order_num()
        # salesreturn.save_csv_data('../data/salesreturnOrderNum.csv', ordernum)
        ReadData().write_data('sale_return_order', 'num', ordernum)
        # 设置检查点
        self.assertTrue(salesreturn.check_salesreturn_success_status())
        self.assertEqual(num1, num2)

    # 挂单后销售
    def test_08_hangup_case(self):
        """单据挂单后在销售"""
        self.login_action()
        cashier = CashierView()
        cashier.hangup_order_cashier_action()
        self.assertTrue(cashier.check_transaction_success_status())

    # # 结账界面打折
    # def test_09_zhe_case(self):
    #     """结账界面打折"""
    #     self.login_action()
    #     cashier = CashierView()
    #     cashier.pay_bill_zhe_action()
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     self.assertEqual(cashier.get_order_price(), r'￥60.00')
    #
    # # 结账界面抹零
    # def test_10_mo_case(self):
    #     """结账界面抹零"""
    #     self.login_action()
    #     cashier = CashierView()
    #     cashier.pay_bill_mo_action()
    #     sales_order_num = cashier.get_sales_order_num()
    #     # cashier.save_csv_data('../data/salesOrderNum.csv', sales_order_num)
    #     ReadData().write_data('sale_order', 'num', sales_order_num)
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     self.assertEqual(cashier.get_order_price(), r'￥115.00')

    # 直接改价退货
    def test_11_sales_direct_return_case(self):
        """销售退货直接改价退货"""
        self.login_action()
        # 获取退货之前的商品库存数
        num1 = self.get_goods_qty() + 1
        salesreturn = SalesReturnView()
        salesreturn.direct_return_action(r'龙啊搞')
        time.sleep(1)
        # 获取退货之后的商品库存数
        num2 = int(salesreturn.select_data_from_db(self.sql)[0]['stockQty'])
        ordernum = salesreturn.get_reutrn_order_num()
        # salesreturn.save_csv_data('../data/salesreturnOrderNum.csv', ordernum)
        ReadData().write_data('sale_return_order', 'num', ordernum)
        # 设置检查点
        self.assertEqual(salesreturn.get_return_order_total_amount(), r'￥10.00')
        self.assertTrue(salesreturn.check_salesreturn_success_status())
        self.assertEqual(num1, num2)

    # 销售退货单作废
    def test_12_sales_return_order_obsolete_case(self):
        """销售退货单作废"""
        # 操作之前库存数
        num1 = self.get_goods_qty() - 1
        self.login_action()
        salesreturnorder = SalesOrderReturnView()
        # data = salesreturnorder.get_csv_data('../data/salesreturnOrderNum.csv', 1)
        sale_return_order = ReadData().get_data('sale_return_order', 'num')
        # ordernum = data[0]
        # 作废操作
        salesreturnorder.opeterating_sales_return_order(1, sale_return_order)
        time.sleep(3)
        # 设置检查点
        num2 = salesreturnorder.check_stock_qty()
        inv_ordernum = salesreturnorder.check_invalid_purchase_ordernum()
        self.assertEqual(num1, num2)
        self.assertEqual(sale_return_order, inv_ordernum)

    # 直接退货
    def test_13_sales_direct_return_case(self):
        """直接正常退货"""
        self.login_action()
        # 获取退货之前的商品库存数
        num1 = self.get_goods_qty() + 1
        salesreturn = SalesReturnView()
        salesreturn.direct_return_action(r'龙啊搞', modify=False)
        time.sleep(1)
        # 获取退货之后的商品库存数
        num2 = int(salesreturn.select_data_from_db(self.sql)[0]['stockQty'])
        ordernum = salesreturn.get_reutrn_order_num()
        # salesreturn.save_csv_data('../data/salesreturnOrderNum.csv', ordernum)
        ReadData().write_data('sale_return_order', 'num', ordernum)
        # 设置检查点
        self.assertTrue(salesreturn.check_salesreturn_success_status())
        self.assertEqual(num1, num2)

    # 销售退货单复制在退货
    def test_14_sales_return_order_copy_case(self):
        """销售退货单复制在退货"""
        num1 = self.get_goods_qty() + 1
        self.login_action()
        salesreturnorder = SalesOrderReturnView()
        # ordernum = salesreturnorder.get_csv_data('../data/salesreturnOrderNum.csv', 1)[0]
        sale_return_order = ReadData().get_data('sale_return_order', 'num')
        salesreturnorder.opeterating_sales_return_order(2, sale_return_order)
        time.sleep(3)
        sales_order_num = salesreturnorder.get_reutrn_order_num()
        # salesreturnorder.save_csv_data('../data/salesreturnOrderNum.csv', sales_order_num)
        ReadData().write_data('sale_return_order', 'num', sales_order_num)
        # 设置检查点
        num2 = salesreturnorder.check_stock_qty()
        self.assertEqual(num1, num2)
        self.assertTrue(salesreturnorder.check_salesreturn_success_status())

    # 销售退货单返回首页
    def test_15_sales_return_order_gohome_case(self):
        """销售退货单返回首页验证"""
        self.login_action()
        salesreturnorder = SalesOrderReturnView()
        # ordernum = salesreturnorder.get_csv_data('../data/salesreturnOrderNum.csv', 1)[0]
        ordernum = ReadData().get_data('sale_return_order', 'num')
        salesreturnorder.opeterating_sales_return_order(3, ordernum)
        # 设置检查点
        self.assertTrue(salesreturnorder.check_gohome_status())
