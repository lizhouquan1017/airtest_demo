from businessView.loginView import LoginView
from businessView.salesreturnView import SalesReturnView
from businessView.salesrorderreturnView import SalesOrderReturnView
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
    def get_goods_qty(self):
        login = LoginView()
        num = int(login.select_data_from_db(self.sql)[0]['stockQty'])
        return num

    # ԭ���˻��ļ�
    def test_05_salesreturn_case(self):
        """ԭ���ļ��˻�"""
        self.login_action()
        # ��ȡ�˻�֮ǰ����Ʒ�����
        num1 = self.get_goods_qty() + 1
        salesreturn = SalesReturnView()
        saleorder = ReadData().get_data('sale_order', 'num')
        salesreturn.originalorder_return_action(saleorder)
        time.sleep(1)
        num2 = int(salesreturn.select_data_from_db(self.sql)[0]['stockQty'])
        ordernum = salesreturn.get_reutrn_order_num()
        ReadData().write_data('sale_return_order', 'num', ordernum)
        # ���ü���
        self.assertEqual(salesreturn.get_return_order_total_amount(), r'��10.00')
        self.assertTrue(salesreturn.check_salesreturn_success_status())
        self.assertEqual(num1, num2)

    # �ҵ�������
    def test_08_hangup_case(self):
        """���ݹҵ���������"""
        self.login_action()
        cashier = CashierView()
        cashier.hangup_order_cashier_action()
        self.assertTrue(cashier.check_transaction_success_status())

    # ֱ�Ӹļ��˻�
    def test_11_sales_direct_return_case(self):
        """�����˻�ֱ�Ӹļ��˻�"""
        self.login_action()
        # ��ȡ�˻�֮ǰ����Ʒ�����
        num1 = self.get_goods_qty() + 1
        salesreturn = SalesReturnView()
        salesreturn.direct_return_action(r'������')
        time.sleep(1)
        # ��ȡ�˻�֮�����Ʒ�����
        num2 = int(salesreturn.select_data_from_db(self.sql)[0]['stockQty'])
        ordernum = salesreturn.get_reutrn_order_num()
        ReadData().write_data('sale_return_order', 'num', ordernum)
        # ���ü���
        self.assertEqual(salesreturn.get_return_order_total_amount(), r'��10.00')
        self.assertTrue(salesreturn.check_salesreturn_success_status())
        self.assertEqual(num1, num2)

    # �����˻�������
    def test_12_sales_return_order_obsolete_case(self):
        """�����˻�������"""
        # ����֮ǰ�����
        num1 = self.get_goods_qty() - 1
        self.login_action()
        salesreturnorder = SalesOrderReturnView()
        sale_return_order = ReadData().get_data('sale_return_order', 'num')
        # ordernum = data[0]
        # ���ϲ���
        salesreturnorder.opeterating_sales_return_order(1, sale_return_order)
        time.sleep(3)
        # ���ü���
        num2 = salesreturnorder.check_stock_qty()
        inv_ordernum = salesreturnorder.check_invalid_purchase_ordernum()
        self.assertEqual(num1, num2)
        self.assertEqual(sale_return_order, inv_ordernum)

    # ֱ���˻�
    def test_13_sales_direct_return_case(self):
        """ֱ�������˻�"""
        self.login_action()
        # ��ȡ�˻�֮ǰ����Ʒ�����
        num1 = self.get_goods_qty() + 1
        salesreturn = SalesReturnView()
        salesreturn.direct_return_action(r'������', modify=False)
        time.sleep(1)
        # ��ȡ�˻�֮�����Ʒ�����
        num2 = int(salesreturn.select_data_from_db(self.sql)[0]['stockQty'])
        ordernum = salesreturn.get_reutrn_order_num()
        ReadData().write_data('sale_return_order', 'num', ordernum)
        # ���ü���
        self.assertTrue(salesreturn.check_salesreturn_success_status())
        self.assertEqual(num1, num2)

    # �����˻����������˻�
    def test_14_sales_return_order_copy_case(self):
        """�����˻����������˻�"""
        num1 = self.get_goods_qty() + 1
        self.login_action()
        salesreturnorder = SalesOrderReturnView()
        sale_return_order = ReadData().get_data('sale_return_order', 'num')
        salesreturnorder.opeterating_sales_return_order(2, sale_return_order)
        time.sleep(3)
        sales_order_num = salesreturnorder.get_reutrn_order_num()
        ReadData().write_data('sale_return_order', 'num', sales_order_num)
        # ���ü���
        num2 = salesreturnorder.check_stock_qty()
        self.assertEqual(num1, num2)
        self.assertTrue(salesreturnorder.check_salesreturn_success_status())

    # �����˻���������ҳ
    def test_15_sales_return_order_gohome_case(self):
        """�����˻���������ҳ��֤"""
        self.login_action()
        salesreturnorder = SalesOrderReturnView()
        ordernum = ReadData().get_data('sale_return_order', 'num')
        salesreturnorder.opeterating_sales_return_order(3, ordernum)
        # ���ü���
        self.assertTrue(salesreturnorder.check_gohome_status())