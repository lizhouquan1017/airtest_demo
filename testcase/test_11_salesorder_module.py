from businessView.loginView import LoginView
from businessView.salesorderView import SalesOrderView
from tools.readCfg import ReadData
from tools.common import Common
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
import time


class SalesReturnTest(StartEnd, TestCase_):
    config = Common.read_config('/db/goodsSQL.ini')
    sql = Common.get_content(config, "��Ʒ����ѯ���", "sql")

    # ��¼����
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # ��ȡԭʼ�����
    def get_goods_qty(self, name):
        login = LoginView()
        arraylist = login.select_data_from_db(self.sql)
        for i in range(0, len(arraylist)):
            if arraylist[i]['goods_name'] == name:
                num = arraylist[i]['stockQty']
                return num

    # ���۵�����������
    def test_02_sales_order_copy_case(self):
        """���۵����Ʋ������µ����۵�"""
        num1 = self.get_goods_qty('������Ʒ8��') - 1
        self.login_action()
        salesorder = SalesOrderView()
        ordernum = ReadData().get_data('sale_order', 'num0')
        salesorder.copy_pay_action(ordernum)
        time.sleep(3)
        sales_order_num = salesorder.get_sales_order_num()
        ReadData().write_data('sale_order', 'num1', sales_order_num)
        # ���ü���
        num2 = salesorder.check_stock_qty('������Ʒ8��')
        self.assertEqual(num1, num2)
        self.assertTrue(salesorder.check_transaction_success_status())

    # ���۵�����
    def test_03_sales_order_obsolete_case(self):
        """���۵�����"""
        # ����֮ǰ�����
        num1 = self.get_goods_qty('������Ʒ8��') + 1
        self.login_action()
        salesorder = SalesOrderView()
        ordernum = ReadData().get_data('sale_order', 'num1')
        # ���ϲ���
        salesorder.obsolete_action(ordernum)
        time.sleep(3)
        # ���ü���
        num2 = salesorder.check_stock_qty('������Ʒ8��')
        inv_ordernum = salesorder.check_invalid_purchase_ordernum()
        self.assertEqual(num1, num2)
        self.assertEqual(ordernum, inv_ordernum)
