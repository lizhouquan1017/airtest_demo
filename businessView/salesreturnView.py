# coding:utf-8

import logging
from selenium.common.exceptions import NoSuchElementException
from baseView.baseView import BaseView
from tools.common import Common


class SalesReturnView(BaseView):

    # 注册页面元素
    config = Common.read_config('/page/salesreturn.ini')
    InventoryBtn_value = Common.get_content(config, '库存按钮', 'value')
    SalesReturnBtn_value = Common.get_content(config, '销售退货', 'value')
    SalesReturnAccount_value = Common.get_content(config, '退货账户', 'value')
    AccountType_value = Common.get_content(config, '账户类型', 'value')
    OrderSelection_value = Common.get_content(config, '原始单选择', 'value')
    FilterBtn_value = Common.get_content(config, '筛选按钮', 'value')
    KeyWordInput_value = Common.get_content(config, '关键字', 'value')
    Confirm_value = Common.get_content(config, '确认按钮', 'value')
    GoodsName_value = Common.get_content(config, '销售单列表商品名称', 'value')
    AddBtn_value = Common.get_content(config, '加减按钮', 'value')
    ReturnListConfirmBtn_value = Common.get_content(config, '退货商品界面确认按钮', 'value')
    ConfirmReturn_value = Common.get_content(config, '确认退货', 'value')
    SalesReturnStatus_value = Common.get_content(config, '退货成功', 'value')

    def salesreturn_action(self, salesordernum):
        logging.info(r'进入库存界面')
        self.click(self.InventoryBtn_value)
        logging.info(r'点击进入销售退货界面')
        self.click_text(self.SalesReturnBtn_value)
        logging.info(r'选择原始销售单')
        self.click(self.OrderSelection_value)
        logging.info(r'进入筛选界面')
        self.click(self.FilterBtn_value)
        logging.info(r'输入销售单号')
        self.type(self.KeyWordInput_value, salesordernum)
        logging.info(r'点击确认按钮')
        self.click(self.Confirm_value)
        logging.info(r'点击筛选出的销售单')
        self.click(self.GoodsName_value)
        logging.info(r'点击添加退货数量')
        self.click(self.AddBtn_value)
        logging.info(r'退货列表点击确认')
        self.click(self.ReturnListConfirmBtn_value)
        logging.info(r'点击确认退货按钮')
        self.click(self.ConfirmReturn_value)

        # 获取采购成功状态
    def check_salesreturn_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.SalesReturnStatus_value)
        if text == r'退货成功':
            return True
        else:
            return False









