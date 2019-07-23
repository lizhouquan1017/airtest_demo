# coding:utf-8

import logging
from baseView.baseView import BaseView
from tools.common import Common


class PurchaseReturnView(BaseView):

    # 注册页面元素
    config = Common.read_config('/page/purchasereturnView.ini')
    InventoryBtn_value = Common.get_content(config, '库存按钮', 'value')
    PurchaseReturnBtn_value = Common.get_content(config, '采购退货按钮', 'value')
    OrderPurchase_value = Common.get_content(config, '原始单选择', 'value')
    FilterBtn_value = Common.get_content(config, '筛选按钮', 'value')
    KeyWordInput_value = Common.get_content(config, '关键字', 'value')
    Confirm_value = Common.get_content(config, '确认按钮', 'value')
    GoodsName_value = Common.get_content(config, '采购单列表商品名称', 'value')
    AddBtn_value = Common.get_content(config, '加减按钮', 'value')
    ReturnListConfirmBtn_value = Common.get_content(config, '退货商品界面确认按钮', 'value')
    ConfirmReturn_value = Common.get_content(config, '确认退货', 'value')
    purchase_return_status_value = Common.get_content(config, '退货成功', 'value')
    directreturn_value = Common.get_content(config, '直接退货', 'value')
    choose_goods_value = Common.get_content(config, '选择商品', 'value')
    pop_define_btn_value = Common.get_content(config, '悬浮框商品确认按钮', 'value')
    goods_name_value = Common.get_content(config, '商品名称', 'value')
    supplier_value = Common.get_content(config, '供应商选择栏', 'value')
    supplier_name_value = Common.get_content(config, '供应商值', 'value')
    purchase_reutrn_ordernum_value = Common.get_content(config, '采购退货单号', 'value')

    # SQL查询
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")

    # 进入采购退货界面
    def enter_purchase_return(self):
        logging.info(r'进入库存界面')
        self.click(self.InventoryBtn_value)
        logging.info(r'点击进入采购退货界面')
        self.click_text(self.PurchaseReturnBtn_value)

    # 确认退货
    def define_purchasereturn(self):
        logging.info(r'点击确认退货按钮')
        self.click(self.ConfirmReturn_value)

    # 原单退货
    def original_purchasereturn_action(self, SalesOrderNum):
        self.enter_purchase_return()
        logging.info(r'选择原始销售单')
        self.click(self.OrderPurchase_value)
        logging.info(r'进入筛选界面')
        self.click(self.FilterBtn_value)
        logging.info(r'输入销售单号')
        self.type(self.KeyWordInput_value, SalesOrderNum)
        logging.info(r'点击确认按钮')
        self.click(self.Confirm_value)
        logging.info(r'点击筛选出的销售单')
        self.click(self.GoodsName_value)
        logging.info(r'点击添加退货数量')
        self.click(self.AddBtn_value)
        logging.info(r'退货列表点击确认')
        self.click(self.ReturnListConfirmBtn_value)
        self.define_purchasereturn()

    # 直接退货
    def direct_puechaseretur_action(self):
        self.enter_purchase_return()
        logging.info(r'点击直接退货')
        self.click_text(self.directreturn_value)
        logging.info('选择供应商')
        self.click(self.supplier_value)
        self.click_text(self.supplier_name_value)
        logging.info(r'点击商品选择按钮')
        self.click_text(self.choose_goods_value)
        logging.info(r'选择退货商品')
        self.click_text(self.goods_name_value)
        logging.info(r'点击添加退货数量')
        self.click(self.AddBtn_value)
        logging.info(r'点击悬浮框确认')
        self.click(self.pop_define_btn_value)
        logging.info(r'退货列表点击确认')
        self.click(self.ReturnListConfirmBtn_value)
        self.define_purchasereturn()

    # 获取采购成功状态
    def check_purchase_return_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.purchase_return_status_value)
        if text == r'采购退货成功':
            return True

    # 获取采购退货单号
    def get_purchase_return_ordernum(self):
        logging.info(r'获取采购单单号')
        purchase_return_ordernum = self.get_text(self.purchase_reutrn_ordernum_value)
        return purchase_return_ordernum

    # 检查数据库商品库存
    def check_stock_qty(self):
        res = self.select_data_from_db(self.sql2)
        num = int(res[0]['stockQty'])
        return num
