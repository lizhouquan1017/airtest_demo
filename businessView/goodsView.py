# coding:utf-8

import logging
from baseView.baseView import BaseView
from tools.common import Common


class GoodsViews(BaseView):
    config = Common.read_config('/page/goodsView.ini')
    goods_management = Common.get_content(config, "商品管理", "value")
    search_edit = Common.get_content(config, "搜索框", "value")
    filter_btn = Common.get_content(config, "筛选按钮", "value")
    add_btn = Common.get_content(config, "新增按钮", "value")
    operating_btn = Common.get_content(config, "操作按钮", "value")
    goods_Category_btn = Common.get_content(config, "商品类目", "value")
    Category_value1 = Common.get_content(config, "类目选择1", "value")
    Category_value2 = Common.get_content(config, "类目选择2", "value")
    Category_value3 = Common.get_content(config, "类目选择3", "value")
    goods_name_edit = Common.get_content(config, "商品名称", "value")
    goods_purchase_price_edit = Common.get_content(config, "采购价格", "value")
    goods_sale_price_edit = Common.get_content(config, "销售价格", "value")
    colour_choose = Common.get_content(config, "颜色选择", "value")
    colour_value = Common.get_content(config, "颜色值", "value")
    size_choose = Common.get_content(config, "尺码选择", "value")
    size_value = Common.get_content(config, "尺码值", "value")
    define_btn = Common.get_content(config, "确认选择", "value")
    save_btn = Common.get_content(config, "保存按钮", "value")
    success_status = Common.get_content(config, "添加成功", "value")
    shelf_obtained_btn = Common.get_content(config, "上下架按钮", "value")
    box_define = Common.get_content(config, "弹框确认", "value")
    obtained_status = Common.get_content(config, "下架状态", "value")
    choose_goods = Common.get_content(config, "商品列表名称", "value")
    filter_shelf_btn = Common.get_content(config, "筛选上架", "value")
    filter_obtained_btn = Common.get_content(config, "筛选下架", "value")
    filter_define_btn = Common.get_content(config, "筛选确认", "value")
    details_operating_btn = Common.get_content(config, "商品详情页面操作按钮", "value")
    delete_btn = Common.get_content(config, "删除商品", "value")

    # 进入商品管理界面
    def enter_goods_list(self):
        logging.info('进入商品管理界面')
        self.click_text(self.goods_management)

    # 新增商品操作
    def add_goods(self, goodsname, costprice, saleprice):
        logging.info('点击新增商品')
        self.click(self.add_btn)
        logging.info('选择商品类目')
        self.click(self.goods_Category_btn)
        logging.info('选择男装')
        self.click_text(self.Category_value1)
        logging.info('选择上装')
        self.click_text(self.Category_value2)
        logging.info('选择男士T恤')
        self.click_text(self.Category_value3)
        logging.info('输入商品名称')
        self.type(self.goods_name_edit, goodsname)
        logging.info('输入成本价')
        self.type(self.goods_purchase_price_edit, costprice)
        logging.info('输入零售价')
        self.type(self.goods_sale_price_edit, saleprice)
        logging.info('点击颜色')
        self.click_text(self.colour_choose)
        logging.info('选择颜色')
        self.click_text(self.colour_value)
        logging.info('点击确认')
        self.click(self.define_btn)
        logging.info('点击尺码')
        self.click_text(self.size_choose)
        logging.info('选择尺码')
        self.click_text(self.size_value)
        logging.info('点击确认')
        self.click(self.define_btn)
        logging.info('点击保存')
        self.click(self.save_btn)

    # 商品下架操作
    def goods_obtained_action(self):
        logging.info('点击商品')
        self.click_text(self.choose_goods)
        logging.info('点击下架')
        self.click(self.shelf_obtained_btn)
        logging.info('点击弹框确认')
        self.click(self.box_define)

    # 商品上架操作
    def goods_shelf_action(self):
        logging.info('点击筛选按钮')
        self.click(self.filter_btn)
        logging.info('点击取消已上架查询')
        self.click(self.filter_shelf_btn)
        logging.info('点击选择已下架查询')
        self.click(self.filter_obtained_btn)
        logging.info('点击确认查询')
        self.click(self.filter_define_btn)
        logging.info('点击商品')
        self.click_text(self.choose_goods)
        logging.info('点击上架')
        self.click(self.shelf_obtained_btn)
        logging.info('点击确认')
        self.click(self.box_define)

    def goods_delete_action(self):
        logging.info('点击商品')
        self.click_text(self.choose_goods)
        logging.info('点击详情页面操作按钮')
        self.click(self.details_operating_btn)
        logging.info('点击删除按钮')
        self.click(self.delete_btn)
        logging.info('点击确认')
        self.click(self.box_define)

    # 检查新增是否成功
    def check_success_status(self):
        status = self.get_text(self.success_status)
        return status

    # 检查下架状态
    def check_obtained_status(self):
        status = self.get_text(self.obtained_status)
        return status


