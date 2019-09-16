# coding:utf-8

import logging
from baseView.baseView import BaseView
from tools.common import Common
from tools.readCfg import ReadData
from airtest.core.api import *


class HomeViews(BaseView):
    config = Common.read_config('/page/homeView.ini')
    home_search_bar = Common.get_content(config, "首页搜索", "value")
    search_edit = Common.get_content(config, "搜索输入框", "value")
    goods_icon = Common.get_content(config, "商品图标", "value")
    goods_num = Common.get_content(config, "商品货号", "value")
    sales_order = Common.get_content(config, "销售单号", "value")

    # 销售单号
    sales_order_num = ReadData().get_data('sale_order', 'num')
    # 销售退货单号
    sale_return_order_num = ReadData().get_data('sale_return_order', 'num')
    # 采购单号
    purchase_order_num = ReadData().get_data('purchase_order', 'num')
    # 采购退货单号
    purchase_return_order_num = ReadData().get_data('purchase_return_order', 'num')
    # 商品货号
    goods_bar_code = ReadData().get_data('goods_bar_code', 'num')

    # 首页搜索商品
    def search_goods(self):
        """搜索商品信息"""
        logging.info('点击进入搜索界面')
        self.click(self.home_search_bar)
        logging.info('输入搜索商品货号')
        self.click(self.search_edit)
        text(self.goods_bar_code)
        dev = device()
        dev.yosemite_ime.code("3")
        logging.info('点击查询商品，查看详细信息')
        self.click(self.goods_icon)

    def search_sales_order(self):
        """搜索销售单"""
        logging.info('点击进入搜索界面')
        self.click(self.home_search_bar)
        logging.info('输入销售单')
        self.type(self.search_edit, self.sales_order_num)
        logging.info('点击查询商品，查看详细信息')
        self.click(self.goods_icon)

    # 获取商品货号
    def get_goods_barcode(self):
        logging.info('获取商品货号')
        goods_num = self.get_text(self.goods_num)
        logging.info(goods_num)
        list1 = goods_num.split('：')
        return list1[1]

    # 获取销售单单号
    def get_sales_num(self):
        logging.info('获取销售单单号')
        sales_order_num = self.get_text(self.sales_order)
        return sales_order_num




