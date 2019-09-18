# coding:utf-8
import logging, time
from baseView.baseView import BaseView
from tools.common import Common


class PurchaseOrderView(BaseView):

    config = Common.read_config('/page/purchaseorderView.ini')
    config_purchase = Common.read_config('/page/purchaseView.ini')
    purchaseBtn_value = Common.get_content(config, "库存按钮", "value")
    purchaseorder_btn = Common.get_content(config, "采购单界面", "value")
    goods_name_value = Common.get_content(config, "采购单列表商品名称", "value")
    filter_btn_value = Common.get_content(config, "采购单列表筛选按钮", "value")
    keyword_edit_value = Common.get_content(config, "关键字输入框", "value")
    status_value = Common.get_content(config, "状态选择栏", "value")
    status_define_value = Common.get_content(config, "状态确认按钮", "value")
    status_value1 = Common.get_content(config, "状态值", "value1")
    status_value2 = Common.get_content(config, "状态值", "value2")
    purchase_ordernum_value = Common.get_content(config, "采购单详情中采购单号", "value")
    operation_action_btn_value = Common.get_content(config, "采购单详情操作按钮", "value")
    invalid_btn_value = Common.get_content(config, "作废订单", "value")
    copy_btn_value = Common.get_content(config, "复制订单", "value")
    back_btn_value = Common.get_content(config, "返回首页", "value")
    define_btn_value = Common.get_content(config, "弹框确认按钮", "value")
    filter_define_btn_value = Common.get_content(config, "筛选界面确认按钮", "value")

    # 采购界面按钮
    supplierName_value = Common.get_content(config_purchase, "供应商选择", "value")
    # supplierValue_value = Common.get_content(config_purchase, "供应商名称", "value")
    confirmStorageBtn_value = Common.get_content(config_purchase, "采购入库按钮", "value")
    transaction_value = Common.get_content(config_purchase, "交易状态", "value")

    # sql语句
    config1 = Common.read_config('/db/purchaseSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config1, "采购单单号查询语句", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")
    sql3 = Common.get_content(config1, "作废采购单号查询", "sql")

    # 进入采购单界面
    def enter_puchase_order(self):
        logging.info(r'进入库存模块')
        self.click(self.purchaseBtn_value)
        logging.info(r'进入采购单界面')
        self.click_text(self.purchaseorder_btn)

    # 筛选单据进入详情界面
    def filter_document_actioin(self, ordernum):
        logging.info(r'点击筛选按钮')
        self.click(self.filter_btn_value)
        logging.info(r'输入单号')
        self.type(self.keyword_edit_value, ordernum)
        logging.info(r'点击确认')
        self.click(self.filter_define_btn_value)
        logging.info(r'点击进入单据详情')
        self.click_text(self.goods_name_value)

    # 对单据进行操作
    def operating_document_action(self, x):
        if x == 1:
            logging.info(r'作废单据')
            self.click(self.operation_action_btn_value)
            logging.info(r'点击作废')
            self.click(self.invalid_btn_value)
            logging.info(r'点击确认')
            self.click(self.define_btn_value)
        elif x == 2:
            logging.info(r'复制订单')
            self.click(self.operation_action_btn_value)
            logging.info(r'点击复制订单')
            self.click(self.copy_btn_value)
            logging.info(r'点击确认')
            self.click(self.define_btn_value)

    # 复制后续操作
    def copy_follow_operation(self):
        logging.info(r'进入供应商选择界面')
        self.click(self.supplierName_value)
        logging.info(r'选择供应商')
        self.click_text(self.supplierValue_value)
        logging.info(r'确认入库')
        self.click(self.confirmStorageBtn_value)

    # 作废采购单
    def obsolete_purchase_order(self, x, ordernum):
        self.enter_puchase_order()
        self.filter_document_actioin(ordernum)
        self.operating_document_action(x)

    # 复制采购单
    def copy_purchase_order(self, x, ordernum):
        self.enter_puchase_order()
        self.filter_document_actioin(ordernum)
        self.operating_document_action(x)
        self.copy_follow_operation()

    # 获取界面采购单单号
    def get_purchase_order_num(self):
        logging.info(r'获取采购单单号')
        ordernum = self.get_text(self.purchase_ordernum_value)
        return ordernum

    # 检查数据库商品库存
    def check_stock_qty(self):
        res = self.select_data_from_db(self.sql2)
        num = int(res[0]['stockQty'])
        return num

    # 检查生成的采购单单号
    def check_purchase_ordernum(self):
        res = self.select_data_from_db(self.sql1)
        ordernum = res[0]['order_code']
        return ordernum

    # 检查作废采购单单号
    def check_invalid_purchase_ordernum(self):
        res = str(self.select_data_from_db(self.sql3)[0]['order_code'])
        return res

    # 获取采购成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.transaction_value)
        if text == r'采购单录入成功':
            return True
        else:
            return False

