# coding:utf-8
from businessView.purchaseView import PurchaseView
from businessView.loginView import LoginView
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.readCfg import ReadData
import time


class PurchaseTest(StartEnd, TestCase_):
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

    # 新增供应商
    def test_01_add_supplier_case(self):
        """新增供应商"""
        self.login_action()
        purchase = PurchaseView()
        purchase.add_supplier('供应商3')
        supplier_name = purchase.select_data_from_db(self.sql3)[0]['supplier_name']
        self.assertEqual(supplier_name, '供应商3')

    # 编辑供应商
    def test_02_edit_supplier_case(self):
        """编辑供应商"""
        self.login_action()
        purchase = PurchaseView()
        purchase.edit_supplier('供应商3', '供应商4')
        supplier_name = purchase.select_data_from_db(self.sql3)[0]['supplier_name']
        self.assertEqual(supplier_name, '供应商4')

    # 禁用供应商
    def test_03_disable_supplier_case(self):
        """禁用供应商"""
        self.login_action()
        purchase = PurchaseView()
        purchase.supplier_enable_disable('供应商4', False)
        time.sleep(5)
        new_purchase = PurchaseView()
        new_status = new_purchase.get_supplier_status('供应商4')
        print("new_status:", new_status)
        self.assertEqual(new_status, 1)

    # 启用供应商
    def test_04_enable_supplier_case(self):
        """启用供应商"""
        self.login_action()
        purchase = PurchaseView()
        purchase.supplier_enable_disable('供应商4', True)
        time.sleep(5)
        new_purchase = PurchaseView()
        new_status = new_purchase.get_supplier_status('供应商4')
        print("new_status:", new_status)
        self.assertEqual(new_status, 0)

    # 正常采购用例
    def test_05_first_purchase_case(self):
        """第一次采购（后选供应商）"""
        self.login_action()
        old_stock = self.get_goods_num('测试商品3号')
        print("old_stock:", old_stock)
        purchase = PurchaseView()
        purchase.enter_purchase_interface()
        purchase.choose_goods_action('测试商品3号')
        purchase.choose_supplier('供应商1')
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('purchase_order', 'num1', purchase_order_num)
        new_stock = purchase.select_data_from_db(self.sql2)[0]['stockQty']
        print("new_stock:", new_stock)
        db_purchase_order_num = purchase.select_data_from_db(self.sql1)[0]['order_code']
        purchase_num = purchase.get_purchase_num()
        print("purchase_num:", purchase_num)
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase.check_transaction_success_status())
        self.assertEqual(purchase_order_num, db_purchase_order_num, r'采购单单号与数据库中一致')
        self.assertEqual(int(old_stock)+int(purchase_num), new_stock, r'采购后库存增加正常')

    # 正常采购用例
    def test_06_second_purchase_case(self):
        """第二次采购（后选供应商）"""
        self.login_action()
        old_stock = self.get_goods_num('测试商品3号')
        print("old_stock:", old_stock)
        purchase = PurchaseView()
        purchase.enter_purchase_interface()
        purchase.choose_supplier('供应商1')
        purchase.choose_goods_action('测试商品3号')
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('purchase_order', 'num2', purchase_order_num)
        new_stock = purchase.select_data_from_db(self.sql2)[0]['stockQty']
        print("new_stock:", new_stock)
        db_purchase_order_num = purchase.select_data_from_db(self.sql1)[0]['order_code']
        purchase_num = purchase.get_purchase_num()
        print("purchase_num:", purchase_num)
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase.check_transaction_success_status())
        self.assertEqual(purchase_order_num, db_purchase_order_num, r'采购单单号与数据库中一致')
        self.assertEqual(int(old_stock)+int(purchase_num), new_stock, r'采购后库存增加正常')

    # 正常采购用例
    def test_07_purchase_multiple_goods_case(self):
        """采购多种商品"""
        self.login_action()
        old_stock = self.get_goods_num('测试商品3号')
        purchase = PurchaseView()
        purchase.enter_purchase_interface()
        purchase.choose_supplier('供应商1')
        purchase.choose_goods_action('测试商品3号')
        purchase.choose_goods_action('测试商品4号')
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('purchase_order', 'num3', purchase_order_num)
        db_purchase_order_num = purchase.select_data_from_db(self.sql1)[0]['order_code']
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase.check_transaction_success_status())
        self.assertEqual(purchase_order_num, db_purchase_order_num, r'采购单单号与数据库中一致')

    # 采购改价用例
    def test_08_purchase_modfiy_price_case(self):
        """采购进货修改价格采购成功"""
        self.login_action()
        old_stock = self.get_goods_num('测试商品3号')
        purchase = PurchaseView()
        purchase.enter_purchase_interface()
        purchase.choose_supplier('供应商1')
        purchase.choose_goods_action('测试商品3号')
        purchase.modfiy_price_action(30)
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('purchase_order', 'num4', purchase_order_num)
        new_stock = purchase.select_data_from_db(self.sql2)[0]['stockQty']
        print("new_stock:", new_stock)
        db_purchase_order_num = purchase.select_data_from_db(self.sql1)[0]['order_code']
        purchase_num = purchase.get_purchase_num()
        print("purchase_num:", purchase_num)
        purchase_price = purchase.get_order_price()
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase.check_transaction_success_status())
        self.assertEqual(purchase_order_num, db_purchase_order_num, r'采购单单号与数据库中一致')
        self.assertEqual(int(old_stock) + int(purchase_num), new_stock, r'采购后库存增加正常')
        self.assertEqual(purchase_price, r'￥30.00')
