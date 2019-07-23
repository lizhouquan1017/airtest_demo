# coding:utf-8

import logging, time, random
from selenium.common.exceptions import NoSuchElementException
from baseView.baseView import BaseView
from common.common import Common


class SalesReturnView(BaseView):

    # 注册页面元素
    config = Common.read_config('/page/salesreturn.ini')
    InventoryBtn_selector = Common.get_content(config, '库存按钮', 'selector')
    InventoryBtn_value = Common.get_content(config, '库存按钮', 'value')
    SalesReturnBtn_value = Common.get_content(config, '销售退货', 'value')
    SalesReturnAccount_selector = Common.get_content(config, '退货账户', 'selector')
    SalesReturnAccount_value = Common.get_content(config, '退货账户', 'value')
    AccountType_value = Common.get_content(config, '账户类型', 'value')
    OrderSelection_selector = Common.get_content(config, '原始单选择', 'selector')
    OrderSelection_value = Common.get_content(config, '原始单选择', 'value')
    FilterBtn_selector = Common.get_content(config, '筛选按钮', 'selector')
    FilterBtn_value = Common.get_content(config, '筛选按钮', 'value')
    KeyWordInput_selecotr = Common.get_content(config, '关键字', 'selector')
    KeyWordInput_value = Common.get_content(config, '关键字', 'value')
    Confirm_selector = Common.get_content(config, '确认按钮', 'selector')
    Confirm_value = Common.get_content(config, '确认按钮', 'value')
    GoodsName_selector = Common.get_content(config, '销售单列表商品名称', 'selector')
    GoodsName_value = Common.get_content(config, '销售单列表商品名称', 'value')
    AddBtn_selector = Common.get_content(config, '加减按钮', 'selector')
    AddBtn_value = Common.get_content(config, '加减按钮', 'value')
    ReturnListConfirmBtn_selector = Common.get_content(config, '退货商品界面确认按钮', 'selector')
    ReturnListConfirmBtn_value = Common.get_content(config, '退货商品界面确认按钮', 'value')
    ConfirmReturn_selector = Common.get_content(config, '确认退货', 'selector')
    ConfirmReturn_value = Common.get_content(config, '确认退货', 'value')
    SalesReturnStatus_selector = Common.get_content(config, '退货成功', 'selector')
    SalesReturnStatus_value = Common.get_content(config, '退货成功', 'value')

    def salesreturn_action(self, SalesOrderNum):
        logging.info(r'进入库存界面')
        e1 = self.find_element(self.InventoryBtn_selector, self.InventoryBtn_value)
        e1.click()
        logging.info(r'点击进入销售退货界面')
        logging.info(self.SalesReturnBtn_value)
        # e2 = self.find_element_xpath(self.SalesReturnBtn_value)
        xpath = '//*[@text=\'{}\']'.format(self.SalesReturnBtn_value)
        e2 = self.driver.find_element_by_xpath(xpath)
        e2.click()
        logging.info(r'选择账户界面')
        e3 = self.find_element(self.SalesReturnAccount_selector, self.SalesReturnAccount_value)
        e3.click()
        logging.info(r'选择账户类型')
        e4 = self.find_element_xpath(self.AccountType_value)
        e4.click()
        logging.info(r'选择原始销售单')
        e5 = self.find_element(self.OrderSelection_selector, self.OrderSelection_value)
        e5.click()
        logging.info(r'进入筛选界面')
        e6 = self.find_element(self.FilterBtn_selector, self.FilterBtn_value)
        e6.click()
        logging.info(r'输入销售单号')
        e7 = self.find_element(self.KeyWordInput_selecotr, self.KeyWordInput_value)
        e7.send_keys(SalesOrderNum)
        logging.info(r'点击确认按钮')
        e8 = self.find_element(self.Confirm_selector, self.Confirm_value)
        e8.click()
        logging.info(r'点击筛选出的销售单')
        e9 = self.find_element(self.GoodsName_selector, self.GoodsName_value)
        e9.click()
        logging.info(r'点击添加退货数量')
        e10 = self.find_element(self.AddBtn_selector, self.AddBtn_value)
        e10.click()
        logging.info(r'退货列表点击确认')
        e11 = self.find_element(self.ReturnListConfirmBtn_selector, self.ReturnListConfirmBtn_value)
        e11.click()
        logging.info(r'点击确认退货按钮')
        e12 = self.find_element(self.ConfirmReturn_selector, self.ConfirmReturn_value)
        e12.click()

        # 获取采购成功状态
    def check_salesreturn_status(self, tips, casename):
        logging.info(r'检查交易成功状态')
        try:
            e = self.find_element(self.SalesReturnStatus_selector, self.SalesReturnStatus_value)
        except NoSuchElementException:
            self.get_windows_img(casename)
            return False
        else:
            if e.text == tips:
                logging.info(casename + '用例成功!')
                return True










