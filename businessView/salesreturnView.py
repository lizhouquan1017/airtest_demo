# coding:utf-8

import logging
from baseView.baseView import BaseView
from tools.common import Common


class SalesReturnView(BaseView):

    # 销售退货页面控件
    config = Common.read_config('/page/salesreturnView.ini')
    inventory_btn = Common.get_content(config, '库存按钮', 'value')
    sales_return_btn = Common.get_content(config, '销售退货', 'value')
    sales_return_account = Common.get_content(config, '退货账户', 'value')
    accounttype = Common.get_content(config, '账户类型', 'value')
    original_order = Common.get_content(config, '原始单选择', 'value')
    filter_btn = Common.get_content(config, '筛选按钮', 'value')
    keyword_edit = Common.get_content(config, '原始销售单搜索栏', 'value')
    confirm_btn = Common.get_content(config, '确认按钮', 'value')
    goods_name = Common.get_content(config, '销售单列表商品名称', 'value')
    add_btn = Common.get_content(config, '加按钮', 'value')
    sub_btn = Common.get_content(config, '减按钮', 'value')
    sales_return_status = Common.get_content(config, '退货状态', 'value')
    sales_return_num_edit = Common.get_content(config, '退货数输入框', 'value')
    direct_return = Common.get_content(config, '直接退货', 'value')
    salers_select = Common.get_content(config, '销售员状态栏', 'value')
    saler = Common.get_content(config, '销售员姓名', 'value')
    choose_goods = Common.get_content(config, '选择商品', 'value')
    goods_edit = Common.get_content(config, '商品搜索栏', 'value')
    modify_price_btn = Common.get_content(config, '改价按钮', 'value')
    pop_define_btn = Common.get_content(config, '悬浮框确认', 'value')
    modify_price_edit = Common.get_content(config, '改价输入框', 'value')
    box_define_btn = Common.get_content(config, '弹框确认', 'value')
    allow_return_num = Common.get_content(config, '可退数', 'value')
    sales_return_ordernum = Common.get_content(config, '销售退货单单号', 'value')
    total_amount = Common.get_content(config, '销售退货金额', 'value')
    choose_goods_define = Common.get_content(config, '选择退货确认按钮', 'value')

    # 进入销售界面
    def enter_sales_return_action(self):
        logging.info(r'点击库存')
        self.click(self.inventory_btn)
        logging.info(r'点击销售退货')
        self.click_text(self.sales_return_btn)

    # 原单退货
    def originalorder_return_action(self, ordernum, modify=True):
        self.enter_sales_return_action()
        logging.info(r'点击请选择原始单据')
        self.click(self.original_order)
        logging.info(r'点击赛选按钮')
        self.click(self.filter_btn)
        logging.info(r'输入需要退货的原始销售单单号')
        self.type(self.keyword_edit, ordernum)
        logging.info(r'点击确认')
        self.click(self.confirm_btn)
        logging.info(r'点击所选择的单号,进入详情界面')
        self.click(self.goods_name)
        logging.info('获取可退数')
        num = int(self.get_text(self.allow_return_num))
        if num > 0:
            # 改价退货
            if modify:
                logging.info(r'点击改价按钮')
                self.click(self.modify_price_btn)
                logging.info(r'输入改价价格')
                self.type(self.modify_price_edit, 10)
                logging.info(r'点击确认')
                self.click(self.box_define_btn)
                logging.info(r'点击加号按钮')
                self.click(self.add_btn)
                logging.info(r'点击确认按钮')
                self.click(self.choose_goods_define)
            else:
                logging.info(r'点击加号按钮')
                self.click(self.add_btn)
                logging.info(r'点击确认按钮')
                self.click(self.choose_goods_define)
        logging.info(r'确认退货')
        self.click(self.choose_goods_define)

    # 直接退货
    def direct_return_action(self, goodsname, modify=True):
        self.enter_sales_return_action()
        logging.info(r'点击直接退货')
        self.click_text(self.direct_return)
        logging.info(r'点击销售员选择栏')
        self.click(self.salers_select)
        logging.info(r'选择销售员')
        self.click_text(self.saler)
        logging.info(r'点击确认')
        self.click(self.choose_goods_define)
        logging.info(r'选择已有商品')
        self.click_text(self.choose_goods)
        logging.info(r'输入需要退货的商品名称')
        self.type(self.goods_edit, goodsname)
        logging.info(r'点击所选商品，进入详情页')
        self.click(self.goods_name)
        logging.info(r'判断是否改价')
        if modify:
            logging.info(r'点击改价按钮')
            self.click(self.modify_price_btn)
            logging.info(r'输入改价价格')
            self.type(self.modify_price_edit, 10)
            logging.info(r'点击确认')
            self.click(self.box_define_btn)
        logging.info(r'点击加号按钮')
        self.click(self.add_btn)
        logging.info(r'点击确认')
        self.click(self.pop_define_btn)
        logging.info(r'点击选好了')
        self.click(self.choose_goods_define)
        logging.info(r'点击确认退货')
        self.click(self.choose_goods_define)

    # 获取生成的销售退货单单号
    def get_reutrn_order_num(self):
        ordernum = self.get_text(self.sales_return_ordernum)
        return ordernum

    # 获取采购成功状态
    def check_salesreturn_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.sales_return_status)
        if text == r'退货成功':
            return True
        else:
            return False

    # 获取销售退货单退货价格
    def get_return_order_total_amount(self):
        total_amount = self.get_text(self.total_amount)
        return total_amount

