# coding:utf-8
import logging
import time
from baseView.baseView import BaseView
from tools.common import Common


class SalesOrderView(BaseView):

    # 销售单界面
    config = Common.read_config('/page/salesorderView.ini')
    stock_btn = Common.get_content(config, "库存按钮", "value")
    sales_btn = Common.get_content(config, "销售单按钮", "value")
    filter_btn = Common.get_content(config, "筛选按钮", "value")
    keyword_edit = Common.get_content(config, "关键字", "value")
    select_settlement = Common.get_content(config, "结算方式选择", "value")
    seller = Common.get_content(config, "销售员选择", "value")
    cashier = Common.get_content(config, "收营员选择", "value")
    is_return = Common.get_content(config, "有无退货选择", "value")
    status = Common.get_content(config, "状态选择", "value")
    swipe_moudle = Common.get_content(config, "状态框", "value")
    swipe_define = Common.get_content(config, "状态框确认", "value")
    filter_define_btn = Common.get_content(config, "筛选确认按钮", "value")
    goodsname = Common.get_content(config, "商品列表名称", "value")
    operating_btn = Common.get_content(config, "销售单详情操作按钮", "value")
    obsolete_btn = Common.get_content(config, "作废按钮", "value")
    copy_btn = Common.get_content(config, "复制按钮", "value")
    gohome_btn = Common.get_content(config, "返回首页按钮", "value")
    return_btn = Common.get_content(config, "销售单退货按钮", "value")
    add_btn = Common.get_content(config, "加按钮", "value")
    modify_btn = Common.get_content(config, "改价", "value")
    modify_edit = Common.get_content(config, "改价输入框", "value")
    box_define_btn = Common.get_content(config, "弹框确认", "value")
    goods_define = Common.get_content(config, "商品确认", "value")
    return_define = Common.get_content(config, "确认退货", "value")
    return_total_money = Common.get_content(config, "退款金额", "value")
    return_order_num = Common.get_content(config, "销售退货单单号", "value")

    # 首页界面
    config3 = Common.read_config('/page/cashierView.ini')
    payBtn_value = Common.get_content(config3, "结账", "value")
    cashBtn_value = Common.get_content(config3, "收款类型", "value")
    confirmCashBtn_value = Common.get_content(config3, "确认收款", "value")
    transaction_value = Common.get_content(config3, "交易状态", "value")
    total_money_value = Common.get_content(config3, "实际收款金额", "value")
    sales_order_num_value = Common.get_content(config3, "销售单单号", "value")

    # sql语句
    config1 = Common.read_config('/db/salesSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config1, "销售单作废查询", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")

    # 进入销售单界面
    def enter_sales_order_action(self):
        logging.info(r'点击库存按钮')
        self.click(self.stock_btn)
        logging.info(r'点击进入销售单界面')
        self.click_text(self.sales_btn)

    # 进入销售单详情
    def enter_sales_order_detail(self):
        logging.info('进入销售单详情')
        self.click(self.goodsname)

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, seller_name=None, cashier_name=None,
                     returned=None, status=None):
        logging.info(r'点击筛选按钮')
        self.click(self.filter_btn)
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.keyword_edit, keyword)
        if settlement is not None:
            logging.info('结算方式')
            self.click(self.select_settlement)
            self.click_text(settlement)
        if seller_name is not None:
            logging.info('选择销售员')
            self.click(self.seller)
            self.click_text(seller_name)
        if cashier_name is not None:
            logging.info('选择收银员')
            self.click(self.cashier)
            self.click_text(cashier_name)
        if returned is not None:
            logging.info('选择退货状态')
            self.click(self.is_return)
            if returned is True:
                logging.info('选择有退货')
                self.swipe(self.swipe_moudle, 'up', 0, -0.05)
                self.click(self.swipe_define)
            elif returned is False:
                logging.info('选择无退货')
                self.swipe(self.swipe_moudle, 'up', 0, -0.1)
                self.click(self.swipe_define)
        if status is not None:
            logging.info('选择订单状态')
            self.click(self.status)
            if status is True:
                logging.info('选择订单正常')
                self.swipe(self.swipe_moudle, 'up', 0, -0.05)
                self.click(self.swipe_define)
            elif status is False:
                logging.info('选择订单作废')
                self.swipe(self.swipe_moudle, 'up', 0, -0.1)
                self.click(self.swipe_define)
        else:
            pass
        logging.info(r'点击确认')
        self.click(self.filter_define_btn)
        self.enter_sales_order_detail()

    # 结账action
    def pay_bill_action(self):
        logging.info(r'去结账')
        self.click(self.payBtn_value)
        logging.info(r'现金支付')
        self.click_text(self.cashBtn_value)
        logging.info('确认收银')
        self.click(self.confirmCashBtn_value)

    # 对单据进行操作
    def operating_document_action(self, obsolete=False, copy=False):
        if obsolete is True:
            logging.info(r'作废单据')
            self.click(self.operating_btn)
            logging.info(r'点击作废')
            self.click(self.obsolete_btn)
            logging.info(r'点击确认')
            self.click(self.box_define_btn)
        if copy is True:
            logging.info(r'复制订单')
            self.click(self.operating_btn)
            logging.info(r'点击复制订单')
            self.click(self.copy_btn)
            logging.info(r'点击确认')
            self.click(self.box_define_btn)
            self.pay_bill_action()

    # 退货
    def sales_order_return(self, modify=False, price=None):
        logging.info('点击退货按钮')
        self.click(self.return_btn)
        if modify is True:
            logging.info('点击改价按钮')
            self.click(self.modify_btn)
            logging.info('输入修改后价格')
            self.type(self.modify_edit, price)
            self.click(self.box_define_btn)
        logging.info('点击添加商品')
        self.click(self.add_btn)
        self.click(self.return_define)
        self.click(self.return_define)

    # 检查交易成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.transaction_value)
        if text == r'交易成功':
            return True

    # 获取退款总金额
    def check_return_total_money(self):
        money = self.get_text(self.return_total_money)
        return money

    # 获取交易价格
    def get_order_price(self):
        logging.info(r'获取订单金额')
        price = self.get_text(self.total_money_value)
        return price

    # 获取销售单号
    def get_sales_order_num(self):
        logging.info(r'获取单号')
        sales_order_num = self.get_text(self.sales_order_num_value)
        return sales_order_num

    # 获取销售退货单单号
    def get_sales_return_order_num(self):
        logging.info(r'获取单号')
        sales_return_order_num = self.get_text(self.return_order_num)
        return sales_return_order_num

    # 检查数据库商品库存
    def check_stock_qty(self, name):
        arraylist = self.select_data_from_db(self.sql2)
        for i in range(0, len(arraylist)):
            if arraylist[i]['goods_name'] == name:
                num = arraylist[i]['stockQty']
                return num

    # 检查作废采购单单号
    def check_invalid_purchase_ordernum(self):
        res = str(self.select_data_from_db(self.sql1)[0]['order_code'])
        return res

    # 销售单测试用例
    def sales_order_action(self, keyword=None, settlement=None, seller_name=None, cashier_name=None,
                           returned=None, status=None, obsolete=False, copy=False, modify=False, price=None):
        self.enter_sales_order_action()
        self.filter_order(keyword=keyword, settlement=settlement, seller_name=seller_name, cashier_name=cashier_name,
                          returned=returned, status=status)
        self.operating_document_action(obsolete=obsolete, copy=copy)
        # self.sales_order_return(modify=modify, price=price)
