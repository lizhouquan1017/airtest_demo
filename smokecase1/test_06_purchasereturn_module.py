# coding:utf-8
from businessView.purchasereturnView import PurchaseReturnView
from businessView.loginView import LoginView
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.readCfg import ReadData


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

    # 原始销售单退货
    def test_01_original_sales_return_case(self):
        """原始销售单退货"""
        self.login_action()
        puchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, normal=True, keyword=pruchase_order)
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num1', purchasereturn_num)
        puchasereutrn.check_purchase_return_success_status()
        self.assertTrue(puchasereutrn.check_purchase_return_success_status())

    # 原始采购单退货
    def test_02_original_purchase_return_case(self):
        """原单退货（现金）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='现金')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num2', purchasereturn_num)
        puchasereutrn.check_purchase_return_success_status()
        self.assertEqual(puchasereutrn.check_account_type(), '现金')

    # 原始采购单退货
    def test_03_original_purchase_return_case(self):
        """原单退货（银行卡）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='银行卡')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num3', purchasereturn_num)
        puchasereutrn.check_purchase_return_success_status()
        self.assertEqual(puchasereutrn.check_account_type(), '银行卡')

    # 原始采购单退货
    def test_04_original_purchase_return_case(self):
        """原单退货（支付宝账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='支付宝账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num4', purchasereturn_num)
        puchasereutrn.check_purchase_return_success_status()
        self.assertEqual(puchasereutrn.check_account_type(), '支付宝账户')

    # 原始采购单退货
    def test_05_original_purchase_return_case(self):
        """原单退货（微信支付账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='微信支付账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num5', purchasereturn_num)
        puchasereutrn.check_purchase_return_success_status()
        self.assertEqual(puchasereutrn.check_account_type(), '微信支付账户')

    # 原始采购单退货
    def test_06_original_purchase_return_case(self):
        """原单退货（其他账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='其他账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num6', purchasereturn_num)
        puchasereutrn.check_purchase_return_success_status()
        self.assertEqual(puchasereutrn.check_account_type(), '其他账户')

    # 原始采购单退货
    def test_07_original_purchase_return_case(self):
        """原单退货（继续退货）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        purchasereutrn.original_order_return_action(1, normal=True, keyword=pruchase_order, is_continue=True)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num7', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 原始采购单退货
    def test_08_original_purchase_return_case(self):
        """原单退货（改价）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        purchasereutrn.original_order_return_action(1, keyword=pruchase_order, modify=1000)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        total_money = purchasereutrn.check_total_money()
        ReadData().write_data('purchase_return_order', 'num8', purchasereturn_num)
        self.assertEqual(total_money, '￥1000.00')

    # 原始采购单退货
    def test_09_original_purchase_return_case(self):
        """原单退货（备注）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        pruchase_order = ReadData().get_data('purchase_order', 'num2')
        purchasereutrn.original_order_return_action(1, keyword=pruchase_order, remark='退货商品')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        info = purchasereutrn.check_remaks()
        ReadData().write_data('purchase_return_order', 'num9', purchasereturn_num)
        self.assertEqual(info, '退货商品')

    # 直接退货
    def test_10_direct_purchase_return_case(self):
        """直接退货（正常）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', normal=True, name='测试商品8号', num=1)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num10', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_11_direct_purchase_return_case(self):
        """直接退货（现金）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', name='测试商品8号', num=1, account='现金')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num11', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_12_direct_purchase_return_case(self):
        """直接退货（银行卡）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', name='测试商品8号', num=1, account='银行卡')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num12', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_13_direct_purchase_return_case(self):
        """直接退货（支付宝账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', name='测试商品8号', num=1, account='支付宝账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num13', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_14_direct_purchase_return_case(self):
        """直接退货（微信支付账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', name='测试商品8号', num=1, account='微信支付账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num14', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_15_direct_purchase_return_case(self):
        """直接退货（其他账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', name='测试商品8号', num=1, account='其他账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num15', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_16_direct_purchase_return_case(self):
        """直接退货（继续退货）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', normal=True, name='测试商品8号', num=1, is_continue=True)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num16', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_17_direct_purchase_return_case(self):
        """直接退货（改价）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', name='测试商品8号', num=1, modify=1000)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num17', purchasereturn_num)
        total_money = purchasereutrn.check_total_money()
        self.assertEqual(total_money, '￥1000.00')

    # 直接退货
    def test_18_direct_purchase_return_case(self):
        """直接退货（备注）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView()
        purchasereutrn.direct_return_action('供应商2', name='测试商品8号', num=1, remark='直接退货备注')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('purchase_return_order', 'num18', purchasereturn_num)
        info = purchasereutrn.check_remaks()
        self.assertEqual(info, '直接退货备注')
