# coding:utf-8
import logging, time
from baseView.baseView import BaseView
from tools.common import Common


class PurchaseView(BaseView):

    config = Common.read_config('/page/purchaseView.ini')
    purchaseBtn_value = Common.get_content(config, "库存按钮", "value")
    purchaseInterface_value = Common.get_content(config, "采购进货", "value")
    chooseGoods_value = Common.get_content(config, "商品选择", "value")
    goodsName_value = Common.get_content(config, "商品名称", "value")
    addBtn_value = Common.get_content(config, "加减按钮", "value")
    confirmBtn_value = Common.get_content(config, "商品确认按钮", "value")
    goodsConfirmBtn_value = Common.get_content(config, "商品列表确认按钮", "value")
    confirmStorageBtn_value = Common.get_content(config, "采购入库按钮", "value")
    supplierName_value = Common.get_content(config, "供应商选择", "value")
    supplierValue_value = Common.get_content(config, "供应商名称", "value")
    transaction_value = Common.get_content(config, "交易状态", "value")
    purchase_ordernum_value = Common.get_content(config, "采购单单号", "value")
    modfiy_btn_value = Common.get_content(config, "改价按钮", "value")
    modfiy_btn1_value = Common.get_content(config, "改价按钮", "value")
    price_edit_value = Common.get_content(config, "悬浮框价格输入框", "value")
    price_define_value = Common.get_content(config, "悬浮框确认", "value")
    order_total_money_value = Common.get_content(config, "订单总金额", "value")
    purchase_num_value = Common.get_content(config, "采购数", "value")

    # sql语句
    config1 = Common.read_config('/db/purchaseSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config1, "采购单单号查询语句", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")

    # 采购选购商品
    def choose_goods_action(self):
        logging.info(r'进入库存模块')
        self.click(self.purchaseBtn_value)
        logging.info(r'进入采购进货界面')
        self.click_text(self.purchaseInterface_value)
        logging.info(r'进入供应商选择界面')
        self.click(self.supplierName_value)
        logging.info(r'选择供应商')
        self.click_text(self.supplierValue_value)
        logging.info(r'点击选择已有商品')
        self.click_text(self.chooseGoods_value)
        logging.info(r'选择商品')
        self.click_text(self.goodsName_value)
        logging.info(r'添加商品数量')
        self.click(self.addBtn_value)
        logging.info(r'确认选择商品')
        self.click(self.confirmBtn_value)
        logging.info(r'商品列表界面确认')
        self.click(self.goodsConfirmBtn_value)

    # 确认入库
    def define_storage_action(self):
        logging.info(r'确认入库')
        self.click(self.confirmStorageBtn_value)

    def modfiy_price_action(self):
        logging.info(r'改价操作')
        self.click(self.modfiy_btn_value)
        time.sleep(1)
        logging.info(r'悬浮框改价按钮')
        self.click(self.modfiy_btn1_value)
        logging.info(r'输入修改价格')
        self.type(self.price_edit_value, 30)
        logging.info(r'点击改价确认')
        self.click(self.price_define_value)
        logging.info(r'确认选择商品')
        self.click(self.confirmBtn_value)

    # 正常采购用例
    def purchase_success_action(self):
        self.choose_goods_action()
        self.define_storage_action()

    # 采购改价操作
    def purchase_modfiy_price_action(self):
        self.choose_goods_action()
        self.modfiy_price_action()
        self.define_storage_action()

    # 获取采购成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.transaction_value)
        if text == r'采购单录入成功':
            return True
        else:
            return False

    # 获取界面采购单单号
    def get_purchase_order_num(self):
        logging.info(r'获取采购单单号')
        purchase_order_num = self.get_text(self.purchase_ordernum_value)
        return purchase_order_num

    # 数据库中商品库存数
    def check_stock_qty(self):
        # 查询采购商品库存
        res = self.select_data_from_db(self.sql2)
        num = int(res[0]['stockQty'])
        return num

    # 数据库中采购单单号
    def for_db_get_order_num(self):
        res = self.select_data_from_db(self.sql1)
        ordernum = res[0]['order_code']
        return ordernum

    # 获取采购单订单价格
    def get_order_price(self):
        logging.info(r'获取订单价格')
        price = self.get_text(self.order_total_money_value)
        return price

    # 获取采购总数
    def get_purchase_num(self):
        logging.info(r'获取订单价格')
        num = self.get_text(self.purchase_num_value)
        return int(num)

