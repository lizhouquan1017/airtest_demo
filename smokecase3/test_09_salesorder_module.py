# coding:utf-8
from businessView.loginView import LoginView
from businessView.salesorderView import SalesOrderView
from tools.readCfg import ReadData
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
import time


class SalesReturnTest(StartEnd, TestCase_):

    config = Common.read_config('/db/goodsSQL.ini')
    sql = Common.get_content(config, "商品库存查询语句", "sql")

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 获取原始库存数
    def get_goods_qty(self, name):
        login = LoginView()
        arraylist = login.select_data_from_db(self.sql)
        for i in range(0, len(arraylist)):
            if arraylist[i]['goods_name'] == name:
                num = arraylist[i]['stockQty']
                return num

    # 销售单复制在销售
    def test_01_sales_order_copy_case(self):
        """销售单复制并生成新的销售单"""
        num1 = self.get_goods_qty('测试商品8号') - 1
        self.login_action()
        salesorder = SalesOrderView()
        ordernum = ReadData().get_data('sale_order', 'num2')
        salesorder.sales_order_action(keyword=ordernum, copy=True)
        sales_order_num = salesorder.get_sales_order_num()
        ReadData().write_data('sale_order', 'num17', sales_order_num)
        # 设置检查点
        num2 = salesorder.check_stock_qty('测试商品8号')
        self.assertEqual(num1, num2)
        self.assertTrue(salesorder.check_transaction_success_status())

    # 销售单作废
    def test_02_sales_order_copy_case(self):
        """销售单作废"""
        num1 = self.get_goods_qty('测试商品8号') + 1
        self.login_action()
        salesorder = SalesOrderView()
        ordernum = ReadData().get_data('sale_order', 'num17')
        salesorder.sales_order_action(keyword=ordernum, obsolete=True)
        # 设置检查点
        obsolete_sale_order = salesorder.check_invalid_purchase_ordernum()
        num2 = salesorder.check_stock_qty('测试商品8号')
        self.assertEqual(num1, num2)
        self.assertEqual(obsolete_sale_order, ordernum)
