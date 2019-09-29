# coding:utf-8
from businessView.salesreturnView import SalesReturnView
from businessView.loginView import LoginView
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.readCfg import ReadData


class salesReturnTest(StartEnd, TestCase_):

    config1 = Common.read_config('/db/salerreturnSQL.ini')
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

    # 原始销售单退货
    def test_01_original_sales_return_case(self):
        """原始销售单退货"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, normal=True, keyword=sales_order)
        sales_return_num = salesreturn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num1', sales_return_num)
        self.assertTrue(salesreturn.check_sales_return_success_status())

    # 原始销售单退货
    def test_02_original_sales_return_case(self):
        """原单退货（现金）"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, keyword=sales_order, account='现金')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('sale_return_order', 'num2', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '现金')

    # 原始销售单退货
    def test_03_original_sales_return_case(self):
        """原单退货（银行卡）"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, keyword=sales_order, account='银行卡')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('sale_return_order', 'num3', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '银行卡')

    # 原始销售单退货
    def test_04_original_sales_return_case(self):
        """原单退货（支付宝账户）"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, keyword=sales_order, account='支付宝账户')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('sale_return_order', 'num4', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '支付宝账户')

    # 原始销售单退货
    def test_05_original_sales_return_case(self):
        """原单退货（微信支付账户）"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, keyword=sales_order, account='微信支付账户')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('sale_return_order', 'num5', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '微信支付账户')

    # 原始销售单退货
    def test_06_original_sales_return_case(self):
        """原单退货（其他账户）"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, keyword=sales_order, account='其他账户')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('sale_return_order', 'num6', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '其他账户')

    # 原始销售单退货
    def test_07_original_sales_return_case(self):
        """原单退货（继续退货）"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, normal=True, keyword=sales_order, is_continue=True)
        salesreturn_num = salesreturn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num7', salesreturn_num)
        self.assertTrue(salesreturn.check_sales_return_success_status())

    # 原始销售单退货
    def test_08_original_sales_return_case(self):
        """原单退货（改价）"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, keyword=sales_order, modify=1000)
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        total_money = salesreturn.check_total_money()
        ReadData().write_data('sale_return_order', 'num8', salesreturn_num)
        self.assertEqual(total_money, '￥1000.00')

    # 原始销售单退货
    def test_09_original_sales_return_case(self):
        """原单退货（备注）"""
        self.login_action()
        salesreturn = SalesReturnView()
        sales_order = ReadData().get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(1, keyword=sales_order, remark='退货商品')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        info = salesreturn.check_remaks()
        ReadData().write_data('sale_return_order', 'num9', salesreturn_num)
        self.assertEqual(info, '退货商品')

    # 直接退货
    def test_10_direct_sales_return_case(self):
        """直接退货（正常）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', normal=True, name='测试商品8号', num=1)
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num10', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_11_direct_sales_return_case(self):
        """直接退货（现金）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='现金')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num11', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_12_direct_sales_return_case(self):
        """直接退货（银行卡）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='银行卡')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num12', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_13_direct_sales_return_case(self):
        """直接退货（支付宝账户）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='支付宝账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num13', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_14_direct_sales_return_case(self):
        """直接退货（微信支付账户）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='微信支付账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num14', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_15_direct_sales_return_case(self):
        """直接退货（其他账户）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='其他账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num15', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_16_direct_sales_return_case(self):
        """直接退货（继续退货）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', normal=True, name='测试商品8号', num=1, is_continue=True)
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('sale_return_order', 'num16', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_17_direct_sales_return_case(self):
        """直接退货（改价）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, modify=1000)
        salesreturn_num = salesreutrn.get_detail_return_ordernum()
        ReadData().write_data('sale_return_order', 'num17', salesreturn_num)
        total_money = salesreutrn.check_total_money()
        self.assertEqual(total_money, '￥1000.00')

    # 直接退货
    def test_18_direct_sales_return_case(self):
        """直接退货（备注）"""
        self.login_action()
        salesreutrn = SalesReturnView()
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, remark='直接退货备注')
        salesreturn_num = salesreutrn.get_detail_return_ordernum()
        ReadData().write_data('sale_return_order', 'num18', salesreturn_num)
        info = salesreutrn.check_remaks()
        self.assertEqual(info, '直接退货备注')
