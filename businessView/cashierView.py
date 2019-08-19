# coding:utf-8
import logging
import time
from baseView.baseView import BaseView
from tools.common import Common


class CashierView(BaseView):

    config = Common.read_config('/page/cashierView.ini')
    cashierBtn_value = Common.get_content(config, "收银按钮", "value")
    chooseGoodsBtn_value = Common.get_content(config, "选择商品", "value")
    payBtn_value = Common.get_content(config, "结账", "value")
    searchInput_value = Common.get_content(config, "商品列表搜索框", "value")
    addBtn_value = Common.get_content(config, "加减按钮", "value")
    confirmBtn_value = Common.get_content(config, "商品确认按钮", "value")
    goodsConfirmBtn_value = Common.get_content(config, "商品列表确认按钮", "value")
    cashBtn_value = Common.get_content(config, "收款类型", "value")
    confirmCashBtn_value = Common.get_content(config, "确认收款", "value")
    goodsName_value = Common.get_content(config, "商品名称", "value")
    transaction_value = Common.get_content(config, "交易状态", "value")
    sales_order_num_value = Common.get_content(config, "销售单单号", "value")
    seller_value = Common.get_content(config, "销售员选择", "value")
    seller1_name_value = Common.get_content(config, "销售员姓名", "value1")
    seller2_name_value = Common.get_content(config, "销售员姓名", "value2")
    seller_search_value = Common.get_content(config, "销售员搜索框", "value")
    modfiy_btn_value = Common.get_content(config, "修改按钮", "value")
    modfiy_price_btn_value = Common.get_content(config, "修改按钮", "value")
    modfiy_price_tab_value = Common.get_content(config, "改价tab", "value")
    modfiy_edit_value = Common.get_content(config, "改价价格输入框", "value")
    modfiy_define_value = Common.get_content(config, "改价确认按钮", "value")
    total_money_value = Common.get_content(config, "实际收款金额", "value")
    zhe_edit_value = Common.get_content(config, "折扣输入框", "value")
    hangup_btn_value = Common.get_content(config, "挂单按钮", "value")
    oreder_ib_value = Common.get_content(config, "挂单界面", "value")
    mo_edit_value = Common.get_content(config, "抹零输入框", "value")

    # 选择商品action
    def choose_goods_action(self):
        logging.info(r'进入收银界面')
        self.click(self.cashierBtn_value)
        logging.info(r'点击选择已有商品')
        self.click_text(self.chooseGoodsBtn_value)
        logging.info(r'点击选择商品')
        self.click_text(self.goodsName_value)
        logging.info(r'添加商品数量')
        self.click(self.addBtn_value)
        time.sleep(1)
        logging.info(r'确认选择商品')
        self.click(self.confirmBtn_value)
        logging.info(r'商品列表界面确认')
        self.click(self.goodsConfirmBtn_value)

    # 结账action
    def pay_bill_action(self):
        logging.info(r'去结账')
        self.click(self.payBtn_value)
        logging.info(r'现金支付')
        self.click_text(self.cashBtn_value)
        logging.info('确认收银')
        self.click(self.confirmCashBtn_value)

    # 正常收银用例
    def cashier_action(self):
        self.choose_goods_action()
        self.pay_bill_action()

    # 收银员限制用例
    def set_seller_num(self):
        self.choose_goods_action()
        # 选择销售员
        self.click(self.seller_value)
        logging.info(r'跳转至销售员选择界面')
        self.click_text(self.seller1_name_value)
        # 第二销售员
        self.click_text(self.seller2_name_value)

    # 收银改价
    def cashier_modfiy_price(self):
        logging.info(r'进入收银界面')
        self.click(self.cashierBtn_value)
        logging.info(r'点击选择已有商品')
        self.click_text(self.chooseGoodsBtn_value)
        logging.info(r'点击选择商品')
        self.click_text(self.goodsName_value)
        logging.info(r'添加商品数量')
        self.click(self.addBtn_value)
        logging.info(r'点击改价按钮')
        self.click(self.modfiy_price_btn_value)
        logging.info(r'点击改价tab')
        self.click_text(self.modfiy_price_tab_value)
        logging.info(r'输入修改价格')
        self.type(self.modfiy_edit_value, 20)
        logging.info(r'点击确认')
        self.click(self.modfiy_define_value)
        logging.info(r'确认选择商品')
        self.click(self.confirmBtn_value)
        logging.info(r'商品列表界面确认')
        self.click(self.goodsConfirmBtn_value)
        self.pay_bill_action()

    # 收银打折
    def cashier_discount_action(self):
        logging.info(r'进入收银界面')
        self.click(self.cashierBtn_value)
        logging.info(r'点击选择已有商品')
        self.click_text(self.chooseGoodsBtn_value)
        logging.info(r'点击选择商品')
        self.click_text(self.goodsName_value)
        logging.info(r'添加商品数量')
        self.click(self.addBtn_value)
        logging.info(r'点击改价按钮')
        self.click(self.modfiy_price_btn_value)
        logging.info(r'输入打折折扣')
        self.type(self.zhe_edit_value, 1)
        logging.info(r'点击确认')
        self.click(self.modfiy_define_value)
        logging.info(r'确认选择商品')
        self.click(self.confirmBtn_value)
        logging.info(r'商品列表界面确认')
        self.click(self.goodsConfirmBtn_value)
        self.pay_bill_action()

    # 挂单成功后销售成功
    def hangup_order_cashier_action(self):
        self.choose_goods_action()
        logging.info(r'点击挂单按钮')
        self.click(self.hangup_btn_value)
        logging.info(r'进入挂单界面')
        self.click(self.oreder_ib_value)
        logging.info(r'选择所挂的单据')
        self.click_text(self.goodsName_value)
        self.pay_bill_action()

    # 结账界面折扣销售
    def pay_bill_zhe_action(self):
        self.choose_goods_action()
        logging.info(r'去结账')
        self.click(self.payBtn_value)
        logging.info(r'输入折扣')
        self.type(self.zhe_edit_value, 5)
        logging.info(r'现金支付')
        self.click_text(self.cashBtn_value)
        logging.info('确认收银')
        self.click(self.confirmCashBtn_value)

    # 结账界面折扣销售
    def pay_bill_mo_action(self):
        self.choose_goods_action()
        logging.info(r'去结账')
        self.click(self.payBtn_value)
        logging.info(r'输入抹零价格')
        self.type(self.mo_edit_value, 5)
        logging.info(r'现金支付')
        self.click_text(self.cashBtn_value)
        logging.info('确认收银')
        self.click(self.confirmCashBtn_value)

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
        logging.info(r'获取采购单单号')
        sales_order_num = self.get_text(self.sales_order_num_value)
        return sales_order_num
