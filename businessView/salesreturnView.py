# coding:utf-8

import logging
from baseView.baseView import BaseView
from tools.common import Common


class SalesReturnView(BaseView):

    # 注册页面元素
    salesreturn_config = Common.read_config('/page/salereturnView.ini')
    stock_btn = Common.get_content(salesreturn_config, '库存', 'value')
    sales_return_btn = Common.get_content(salesreturn_config, '销售退货按钮', 'value')
    return_selection1 = Common.get_content(salesreturn_config, '销售退货tab', 'value1')
    return_selection2 = Common.get_content(salesreturn_config, '销售退货tab', 'value2')
    return_selection3 = Common.get_content(salesreturn_config, '销售退货tab', 'value3')
    return_selection4 = Common.get_content(salesreturn_config, '销售退货tab', 'value4')
    choose_sales_order = Common.get_content(salesreturn_config, '原始单选择', 'value')
    original_order_filter = Common.get_content(salesreturn_config, '原单筛选按钮', 'value')
    keyword_edit = Common.get_content(salesreturn_config, '关键字', 'value')
    choose_settlement = Common.get_content(salesreturn_config, '结算方式', 'value')
    choose_supplier = Common.get_content(salesreturn_config, '供应商选择', 'value')
    is_return = Common.get_content(salesreturn_config, '退货状态', 'value')
    status_module = Common.get_content(salesreturn_config, '状态框', 'value')
    swipe_define = Common.get_content(salesreturn_config, '滑框确认', 'value')
    choose_status = Common.get_content(salesreturn_config, '订单状态', 'value')
    filter_define_btn = Common.get_content(salesreturn_config, '筛选确认', 'value')
    original_order_account = Common.get_content(salesreturn_config, '退款账户', 'value')
    original_order_remarks = Common.get_content(salesreturn_config, '备注信息', 'value')
    define_btn = Common.get_content(salesreturn_config, '确认退货', 'value')
    choose_goods1 = Common.get_content(salesreturn_config, '销售单列表商品名称', 'value1')
    choose_goods2 = Common.get_content(salesreturn_config, '销售单列表商品名称', 'value2')
    choose_goods3 = Common.get_content(salesreturn_config, '销售单列表商品名称', 'value3')
    choose_goods4 = Common.get_content(salesreturn_config, '销售单列表商品名称', 'value4')
    add_btn = Common.get_content(salesreturn_config, '加减按钮', 'value')
    modfiy_btn = Common.get_content(salesreturn_config, '改价按钮', 'value')
    price_edit = Common.get_content(salesreturn_config, '改价输入框', 'value')
    box_define = Common.get_content(salesreturn_config, '弹框确认', 'value')
    goods_confirm_btn = Common.get_content(salesreturn_config, '悬浮框商品确认按钮', 'value')
    direct_return_account = Common.get_content(salesreturn_config, '直接退货退款账户', 'value')
    direct_return_remarks = Common.get_content(salesreturn_config, '直接退货备注', 'value')
    direct_return_choose_goods = Common.get_content(salesreturn_config, '选择商品', 'value')
    salesreturn_success_status = Common.get_content(salesreturn_config, '退货成功', 'value')
    salesreturn_order_num = Common.get_content(salesreturn_config, '销售退货单号', 'value')
    settlemen_type = Common.get_content(salesreturn_config, '检查结算方式', 'value')
    continue_return_btn = Common.get_content(salesreturn_config, '继续退货', 'value')
    total_money_value = Common.get_content(salesreturn_config, '退货金额', 'value')
    detail_btn = Common.get_content(salesreturn_config, '查看详情', 'value')
    remarks_info = Common.get_content(salesreturn_config, '详情备注', 'value')
    stock_low = Common.get_content(salesreturn_config, '库存低值', 'value')
    stock_high = Common.get_content(salesreturn_config, '库存高值', 'value')
    choose_selles = Common.get_content(salesreturn_config, '选择销售员', 'value')
    selles = Common.get_content(salesreturn_config, '选择销售员', 'value')
    detail_sales_return_no = Common.get_content(salesreturn_config, '详情销售退货单号', 'value')



    # SQL查询
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")

    # 进入采购退货界面
    def enter_sales_return(self):
        logging.info(r'进入库存界面')
        self.click(self.stock_btn)
        logging.info(r'点击进入销售退货界面')
        self.click_text(self.sales_return_btn)

    # 确认原单退货/直接退货
    def sales_return_selection(self, flag=True):
        if flag is True:
            elements = self.get_elements(self.return_selection1, self.return_selection2,
                                         self.return_selection3, self.return_selection4)
            for i in range(0, len(elements)):
                if elements[i].get_text() == '关联原单退货':
                    pass
        if flag is False:
            elements = self.get_elements(self.return_selection1, self.return_selection2,
                                         self.return_selection3, self.return_selection4)
            for i in range(0, len(elements)):
                if elements[i].get_text() == '直接退货':
                    elements[i].click()

    # 选择原单退货
    def sales_order_selection(self):
        logging.info('选择原单')
        self.click(self.choose_sales_order)
        logging.info('点击筛选')
        self.click(self.original_order_filter)

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, seller_name=None, returned=None, status=None):
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.keyword_edit, keyword)
        if settlement is not None:
            logging.info('输入开始时间')
            self.click(self.choose_settlement)
            self.click_text(settlement)
        if seller_name is not None:
            logging.info('选择销售员')
            self.click(self.selles)
            self.click_text(seller_name)
        if returned is not None:
            logging.info('选择退货状态')
            self.click(self.is_return)
            if returned is True:
                logging.info('选择有退货')
                self.swipe(self.status_module, 'up', 0, -0.05)
                self.click(self.swipe_define)
            elif returned is False:
                logging.info('选择无退货')
                self.swipe(self.status_module, 'up', 0, -0.1)
                self.click(self.swipe_define)
        if status is not None:
            logging.info('选择订单状态')
            self.click(self.choose_status)
            if status is True:
                logging.info('选择订单正常')
                self.swipe(self.status_module, 'up', 0, -0.05)
                self.click(self.swipe_define)
            elif status is False:
                logging.info('选择订单作废')
                self.swipe(self.status_module, 'up', 0, -0.1)
                self.click(self.swipe_define)
        else:
            pass
        logging.info(r'点击确认')
        self.click(self.filter_define_btn)

    # 原单账户选择
    def original_order_account_selection(self, name):
        self.click(self.original_order_account)
        self.click_text(name)

    # 原单备注填写
    def original_order_remarks_edit(self, info):
        self.type(self.original_order_remarks, info)

    # 直接退货选择销售员
    def direct_return_seller_selection(self, seller_name):
        self.click(self.choose_selles)
        self.click_text(seller_name)
        self.click(self.define_btn)

    # 直接退货账户选择
    def direct_return_account_selection(self, name):
        self.click(self.direct_return_account)
        self.click_text(name)

    # 直接退货备注填写
    def direct_return_remarks_edit(self,info):
        logging.info('填写备注信息')
        self.type(self.direct_return_remarks, info)

    # 直接退货选择商品
    def direct_return_goods_selection(self, name, num):
        logging.info('点击选择已有商品')
        self.click_text(self.direct_return_choose_goods)
        goods = self.get_elements(self.choose_goods1, self.choose_goods2, self.choose_goods3)
        for i in range(0, len(goods)):
            if goods[i].get_text() == name:
                goods[i].click()
        for i in range(0, num):
            self.click(self.add_btn)
        logging.info('点击确认')
        self.click(self.goods_confirm_btn)
        self.click(self.define_btn)

    # 选择退货商品
    def choose_return_goods(self, num):
        self.click(self.choose_goods4)
        for i in range(0, num):
            self.click(self.add_btn)
        logging.info('点击确认')
        self.click(self.define_btn)

    # 改价
    def modfiy_price_action(self, price):
        logging.info(r'改价操作')
        self.click(self.modfiy_btn)
        logging.info(r'悬浮框改价按钮')
        self.click(self.modfiy_btn)
        logging.info(r'输入修改价格')
        self.type(self.price_edit, price)
        logging.info(r'点击改价确认')
        self.click(self.box_define)
        logging.info(r'确认选择商品')
        self.click(self.goods_confirm_btn)

    # 确认退货
    def define_salesreturn(self):
        logging.info(r'点击确认退货按钮')
        self.click(self.define_btn)

    # 查看详情
    def enter_detail_interface(self):
        logging.info('进入详情界面')
        self.click(self.detail_btn)

    # 获取销售成功状态
    def check_sales_return_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.salesreturn_success_status)
        if text == r'退货成功':
            return True

    # 获取销售退货单号
    def get_sales_return_ordernum(self):
        logging.info(r'获取销售退货单号')
        sales_return_ordernum = self.get_text(self.salesreturn_order_num)
        return sales_return_ordernum

    def get_detail_return_ordernum(self):
        logging.info(r'获取销售退货单号')
        sales_return_ordernum = self.get_text(self.detail_sales_return_no)
        return sales_return_ordernum

    # 检查数据库商品库存
    def check_stock_qty(self):
        res = self.select_data_from_db(self.sql2)
        num = int(res[0]['stockQty'])
        return num

    # 检查结算方式
    def check_account_type(self):
        info = self.get_text(self.settlemen_type)
        return info

    # 检查退款金额
    def check_total_money(self):
        total = self.get_text(self.total_money_value)
        return total

    # 检查备注信息
    def check_remaks(self):
        info = self.get_text(self.remarks_info)
        return info

    # 原单退货
    def original_order_return_action(self, num, normal=False, keyword=None, account=None, remark=None, modify=None,
                                     is_continue=False):
        self.enter_sales_return()
        self.sales_return_selection(flag=True)
        self.sales_order_selection()
        self.filter_order(keyword=keyword)
        self.choose_return_goods(num)
        if normal is True:
            self.define_salesreturn()
        if modify is not None:
            self.modfiy_price_action(modify)
            self.define_salesreturn()
            self.enter_detail_interface()
        if account is not None:
            self.original_order_account_selection(account)
            self.define_salesreturn()
            self.enter_detail_interface()
        if remark is not None:
            self.original_order_remarks_edit(remark)
            self.define_salesreturn()
            self.enter_detail_interface()
        if is_continue:
            self.click(self.continue_return_btn)
            self.sales_order_selection()
            self.filter_order(keyword=keyword)
            self.choose_return_goods(num)
            if modify is not None:
                self.modfiy_price_action(modify)
            if account is not None:
                self.original_order_account_selection(account)
            if remark is not None:
                self.original_order_remarks_edit(remark)
            self.define_salesreturn()

    # 直接退货
    def direct_return_action(self, seller_name, normal=False, name=None, num=None, account=None,
                             modify=None, remark=None, is_continue=False):
        self.enter_sales_return()
        self.sales_return_selection(flag=False)
        self.direct_return_goods_selection(name, num)
        self.direct_return_seller_selection(seller_name=seller_name)
        if normal:
            self.define_salesreturn()
        if account is not None:
            logging.info('选择账户')
            self.direct_return_account_selection(account)
            self.define_salesreturn()
        if modify is not None:
            self.modfiy_price_action(modify)
            self.define_salesreturn()
            self.enter_detail_interface()
        if remark is not None:
            self.direct_return_remarks_edit(remark)
            self.define_salesreturn()
            self.enter_detail_interface()
        if is_continue:
            self.click(self.continue_return_btn)
            self.sales_return_selection(flag=False)
            self.direct_return_goods_selection(name, num)
            self.direct_return_seller_selection(seller_name=seller_name)
            self.define_salesreturn()






