# coding:utf-8
from businessView.purchaseorderView import PurchaseOrderView
from businessView.loginView import LoginView
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.readCfg import ReadData


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

    # 采购单筛选用例
    def test_01_purchase_order_filer_case(self):
        """关键字筛选(单号)"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_02_purchase_order_filer_case(self):
        """关键字筛选(备注)"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword='采购两种商品')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_03_purchase_order_filer_case(self):
        """结算账户筛选（现金）"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(settlement='现金')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_04_purchase_order_filer_case(self):
        """供应商名称筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(supplier_name='供应商2')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05_purchase_order_filer_case(self):
        """无退货进行筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(returned=False)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_06_purchase_order_filer_case(self):
        """正常状态筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(status=True)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    # 采购单作废用例
    def test_07_obsolete_purchase_order_case(self):
        """采购单作废"""
        self.login_action()
        old_num = self.get_goods_num('测试商品8号') - 1
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.operating_document_action(obsolete=True)
        new_num = purchaseorder.check_stock_qty('测试商品8号')
        invalid_purchase_ordernum = purchaseorder.check_invalid_purchase_ordernum()
        ReadData().write_data('obsolete_purchase_order', 'num1', invalid_purchase_ordernum)
        # 设置检查点
        self.assertEqual(old_num, new_num)
        self.assertTrue(ordernum, invalid_purchase_ordernum)

    # 复制订单用例
    def test_08_copy_purchase_order_case(self):
        """复制采购单"""
        self.login_action()
        old_num = self.get_goods_num('测试商品8号')+30
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num2')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.operating_document_action(copy=True)
        purchaseorder.copy_follow_operation('供应商2')
        new_num = purchaseorder.check_stock_qty('测试商品8号')
        order_num = purchaseorder.get_detail_ptuchase_order()
        ReadData().write_data('purchase_order', 'num6', order_num)
        # 设置检查点
        self.assertTrue(purchaseorder.check_transaction_success_status())
        self.assertEqual(old_num, new_num)

    def test_09_purchase_order_return_case(self):
        """采购单退货"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num3')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.purchase_order_return()
        self.assertTrue(purchaseorder.get_purchase_return_status())

    def test_10_purchase_order_return_case(self):
        """采购单改价退货"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num4')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.purchase_order_return(modify=True, price=50)
        self.assertTrue(purchaseorder.get_purchase_return_status())

    # 采购单筛选用例
    def test_11_purchase_order_filer_case(self):
        """关键字筛选(作废单据)"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('obsolete_purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(status=False)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    # 采购单筛选用例
    def test_12_purchase_order_filer_case(self):
        """关键字筛选(退货)"""
        self.login_action()
        purchaseorder = PurchaseOrderView()
        ordernum = ReadData().get_data('purchase_order', 'num4')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(returned=True)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)
