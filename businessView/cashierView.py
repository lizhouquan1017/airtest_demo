# coding:utf-8
import logging
import time
from baseView.baseView import BaseView
from tools.common import Common
from airtest.core.api import *


class CashierView(BaseView):

    config = Common.read_config('/page/cashierView.ini')
    cashierBtn_value = Common.get_content(config, "收银按钮", "value")
    chooseGoodsBtn_value = Common.get_content(config, "选择商品", "value")
    payBtn = Common.get_content(config, "结账", "value")
    searchInput_value = Common.get_content(config, "商品列表搜索框", "value")
    addBtn_value = Common.get_content(config, "加减按钮", "value")
    confirmBtn = Common.get_content(config, "商品确认按钮", "value")
    goodsConfirmBtn_value = Common.get_content(config, "商品列表确认按钮", "value")
    cashBtn_value = Common.get_content(config, "收款类型", "value")
    confirmCashBtn_value = Common.get_content(config, "确认收款", "value")
    normal_goodsName = Common.get_content(config, "商品名称", "value1")
    moling_goodsName = Common.get_content(config, "商品名称", "value2")
    transaction_value = Common.get_content(config, "交易状态", "value")
    sales_order_num_value = Common.get_content(config, "销售单单号", "value")
    modfiy_btn = Common.get_content(config, "改价按钮", "value")
    modfiy_price_tab_value = Common.get_content(config, "改价tab", "value")
    modify_edit = Common.get_content(config, "改价价格输入框", "value")
    modify_define_btn = Common.get_content(config, "改价确认按钮", "value")
    total_money_value = Common.get_content(config, "实际收款金额", "value")
    offer_bix = Common.get_content(config, "优惠框", "value")
    zhe_edit = Common.get_content(config, "折扣输入框", "value")
    hangup_btn_value = Common.get_content(config, "挂单按钮", "value")
    oreder_ib_value = Common.get_content(config, "挂单界面", "value")
    mo_edit_value = Common.get_content(config, "抹零输入框", "value")
    offer_button = Common.get_content(config, "优惠框", "value")
    offer_choose = Common.get_content(config, "优惠选择", "value")
    offer_define = Common.get_content(config, "优惠确认", "value")
    modify_price_edit = Common.get_content(config, "改价输入框", "value")
    modify_discount_tab1 = Common.get_content(config, "打折改价", "value1")
    modify_discount_tab2 = Common.get_content(config, "打折改价", "value2")
    modify_discount_tab3 = Common.get_content(config, "打折改价", "value3")
    modify_discount_tab4 = Common.get_content(config, "打折改价", "value4")
    search_edit = Common.get_content(config, "搜索栏", "value")

    config = Common.read_config('/db/businessSQL.ini')
    sql1 = Common.get_content(config, "查询抹零开关", "sql")
    sql2 = Common.get_content(config, "开启抹零状态", "sql")
    sql3 = Common.get_content(config, "关闭抹零状态", "sql")

    # 进入收银界面
    def enter_cash(self):
        logging.info(r'进入收银界面')
        self.click(self.cashierBtn_value)
        logging.info(r'点击选择已有商品')
        self.click_text(self.chooseGoodsBtn_value)

    # 选择商品action
    def choose_goods_action(self, num, flag=False):
        self.enter_cash()
        if flag is False:
            logging.info(r'点击选择整数价格商品')
            self.click_text(self.normal_goodsName)
        elif flag is True:
            logging.info(r'点击选择整数价格商品')
            self.click_text(self.moling_goodsName)
        logging.info(r'添加商品数量')
        for i in range(0, num):
            self.click(self.addBtn_value)
        time.sleep(1)
        logging.info(r'确认选择商品')
        self.click(self.confirmBtn)
        logging.info(r'商品列表界面确认')
        self.click(self.goodsConfirmBtn_value)

    # 结账action
    def pay_bill_action(self):
        logging.info(r'现金支付')
        self.click_text(self.cashBtn_value)
        logging.info('确认收银')
        self.click(self.confirmCashBtn_value)

    # 正常收银用例
    def normal_cashier_action(self, num):
        self.choose_goods_action(num)
        logging.info(r'去结账')
        self.click(self.payBtn)
        self.pay_bill_action()

    # 商品打折改价
    def goods_modify_discount(self, num, value1, value2, flag=False):
        self.choose_goods_action(num, flag=flag)
        logging.info('点击改价按钮')
        self.click(self.modfiy_btn)
        logging.info('点击改价')
        self.click(self.modfiy_btn)
        if value1 == '改价':
            logging.info('点击改价tab')
            self.click_modify_discount_tab(value1)
            logging.info('输入修改后的价格')
            self.type(self.modify_edit, value2)
        elif value1 == '打折':
            logging.info('输入折扣')
            self.type(self.zhe_edit, value2)
        logging.info('点击确认')
        self.click(self.modify_define_btn)
        logging.info('点击商品确认')
        self.click(self.confirmBtn)

    # 订单打折改价
    def order_modify_discount(self, value1, value2=None):
        if value1 == '无优惠':
            logging.info(r'去结账')
            self.click(self.payBtn)
            self.pay_bill_action()
        elif value1 == '打折':
            logging.info(r'去结账')
            self.click(self.payBtn)
            logging.info(r'点击整单优惠')
            self.click(self.offer_button)
            logging.info(r'滑动')
            self.swipe(self.offer_choose, 'up', 0, -0.05)
            logging.info(r'确认')
            self.click(self.offer_define)
            logging.info(r'输入折扣')
            self.type(self.zhe_edit, value2)
            self.pay_bill_action()
        elif value1 == '改价':
            logging.info(r'去结账')
            self.click(self.payBtn)
            logging.info(r'点击整单优惠')
            self.click(self.offer_button)
            logging.info(r'滑动')
            self.swipe(self.offer_choose, 'up', 0, -0.1)
            logging.info(r'确认')
            self.click(self.offer_define)
            logging.info(r'输入改价后的价格')
            self.type(self.modify_price_edit, value2)
            self.pay_bill_action()

    # 挂单成功后销售成功
    def hangup_order_cashier_action(self, num):
        self.choose_goods_action(num)
        logging.info(r'点击挂单按钮')
        self.click(self.hangup_btn_value)
        logging.info(r'进入挂单界面')
        self.click(self.oreder_ib_value)
        logging.info(r'选择所挂的单据')
        self.click_text(self.normal_goodsName)
        self.pay_bill_action()

    # 检查交易成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.transaction_value)
        if text == r'交易成功':
            return True

    # 获取交易价格
    def get_order_price(self):
        logging.info(r'获取订单金额')
        price = self.get_text(self.total_money_value)
        return price

    # 获取销售单号
    def get_sales_order_num(self):
        logging.info(r'获取销售单单号')
        sales_order_num = self.get_text(self.sales_order_num_value)
        return sales_order_num

    # 获取打折或改价tab
    def click_modify_discount_tab(self, value):
        elements = self.get_elements(self.modify_discount_tab1, self.modify_discount_tab2,
                                     self.modify_discount_tab3, self.modify_discount_tab4)
        for i in range(0, len(elements)):
            if elements[i].get_text() == value:
                elements[i].click()

    # 设置抹零是否开启
    def moling_switch(self, flag=False):
            status = self.select_data_from_db(self.sql1)[0]['is_erase_money']
            if status == 0 and flag is False:
                pass
            elif status == 1 and flag is False:
                self.update_data_from_db(self.sql3)
                new_status = self.select_data_from_db(self.sql1)[0]['is_erase_money']
                if new_status == 0:
                    pass
            elif status == 0 and flag is True:
                self.update_data_from_db(self.sql2)
                new_status = self.select_data_from_db(self.sql1)[0]['is_erase_money']
                print(new_status)
                if new_status == 1:
                    pass
            elif status == 1 and flag is True:
                pass


