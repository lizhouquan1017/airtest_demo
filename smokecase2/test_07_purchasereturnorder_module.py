# coding:utf-8
from businessView.purchasereturnorderView import PurchaseReturnOrderView
from businessView.loginView import LoginView
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.readCfg import ReadData


class PurchaseReturnOrderTest(StartEnd, TestCase_):

    config1 = Common.read_config('/db/purchasereturnSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 获取操作之前商品库存数
    def get_goods_num(self, name):
        login = LoginView()
        array = login.select_data_from_db(self.sql2)
        for i in range(0, len(array)):
            if array[i]['goods_name'] == name:
                num = array[i]['stockQty']
                return int(num)

    # 采购退货单筛选
    def test_01_purchase_return_order(self):
        """正常筛选"""
        self.login_action()
        p = PurchaseReturnOrderView()
        purchase_return_order = ReadData().get_data('purchase_return_order', 'num1')
        p.purchase_return_order_action(keyword=purchase_return_order)
        confim_num = p.get_detail_ptuchase_order()
        self.assertEqual(purchase_return_order, confim_num)

    def test_02_purchase_return_order(self):
        """采购退货单作废"""
        self.login_action()
        old_stock = self.get_goods_num('测试商品8号')+1
        p = PurchaseReturnOrderView()
        purchase_return_order = ReadData().get_data('purchase_return_order', 'num2')
        p.purchase_return_order_action(keyword=purchase_return_order, obsolete=True)
        new_stock = p.check_stock_qty('测试商品8号')
        self.assertEqual(old_stock, new_stock)

    def test_03_purchase_return_order(self):
        """作废单据筛选"""
        self.login_action()
        p = PurchaseReturnOrderView()
        purchase_return_order = ReadData().get_data('purchase_return_order', 'num2')
        p.purchase_return_order_action(status=False)
        confim_num = p.get_detail_ptuchase_order()
        self.assertEqual(purchase_return_order, confim_num)

    def test_04_purchase_return_order(self):
        """单据复制（原单退货）"""
        self.login_action()
        old_stock = self.get_goods_num('测试商品8号') - 1
        p = PurchaseReturnOrderView()
        purchase_return_order = ReadData().get_data('purchase_return_order', 'num3')
        p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='供应商2', is_original=True)
        purchase_return_num = p.get_detail_ptuchase_order()
        ReadData().write_data('purchase_return_order', 'num19', purchase_return_num)
        new_stock = p.check_stock_qty('测试商品8号')
        self.assertEqual(old_stock, new_stock)

    def test_05_purchase_return_order(self):
        """单据复制（直接退货）"""
        self.login_action()
        old_stock = self.get_goods_num('测试商品8号') - 1
        p = PurchaseReturnOrderView()
        purchase_return_order = ReadData().get_data('purchase_return_order', 'num10')
        p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='供应商2')
        purchase_return_num = p.get_detail_ptuchase_order()
        ReadData().write_data('purchase_return_order', 'num19', purchase_return_num)
        new_stock = p.check_stock_qty('测试商品8号')
        self.assertEqual(old_stock, new_stock)

    def test_06_purchase_return_order(self):
        """结算方式（现金）"""
        self.login_action()
        p = PurchaseReturnOrderView()
        p.purchase_return_order_action(settlement='现金')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('现金', settlement_type)

    def test_07_purchase_return_order(self):
        """结算方式（银行卡）"""
        self.login_action()
        p = PurchaseReturnOrderView()
        p.purchase_return_order_action(settlement='银行卡')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('银行卡', settlement_type)

    def test_08_purchase_return_order(self):
        """结算方式（支付宝账户）"""
        self.login_action()
        p = PurchaseReturnOrderView()
        p.purchase_return_order_action(settlement='支付宝账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('支付宝账户', settlement_type)

    def test_09_purchase_return_order(self):
        """结算方式（微信支付账户）"""
        self.login_action()
        p = PurchaseReturnOrderView()
        p.purchase_return_order_action(settlement='微信支付账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('微信支付账户', settlement_type)

    def test_10_purchase_return_order(self):
        """结算方式（其他账户）"""
        self.login_action()
        p = PurchaseReturnOrderView()
        p.purchase_return_order_action(settlement='其他账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('其他账户', settlement_type)
