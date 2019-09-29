# coding:utf-8
import logging
from baseView.baseView import BaseView
from tools.common import Common


class PurchaseReturnOrderView(BaseView):

    config_purchasereturn_order = Common.read_config('/page/purchasereturnorderView.ini')
    config_purchase_return = Common.read_config('/page/purchasereturnView.ini')
    purchase_btn = Common.get_content(config_purchasereturn_order, "库存按钮", "value")
    purchase_return_order_btn = Common.get_content(config_purchasereturn_order, "采购退货单界面", "value")
    goods_name = Common.get_content(config_purchasereturn_order, "采购退货单列表商品名称", "value")
    filter_btn = Common.get_content(config_purchasereturn_order, "筛选按钮", "value")
    keyword_edit = Common.get_content(config_purchasereturn_order, "关键字输入框", "value")
    swipe_define = Common.get_content(config_purchasereturn_order, "状态框确认", "value")
    choose_settlement = Common.get_content(config_purchasereturn_order, "选择结算方式", "value")
    choose_supplier = Common.get_content(config_purchasereturn_order, "选择供应商", "value")
    choose_status = Common.get_content(config_purchasereturn_order, "选择状态栏", "value")
    status_module = Common.get_content(config_purchasereturn_order, "状态框", "value")
    filter_define_btn = Common.get_content(config_purchasereturn_order, "筛选界面确认按钮", "value")
    purchase_return_ordernum = Common.get_content(config_purchasereturn_order, "采购退货单详情中采购退货单号", "value")
    operation_action_btn = Common.get_content(config_purchasereturn_order, "采购退货单详情操作按钮", "value")
    invalid_btn = Common.get_content(config_purchasereturn_order, "作废订单", "value")
    copy_btn = Common.get_content(config_purchasereturn_order, "复制订单", "value")
    back_btn = Common.get_content(config_purchasereturn_order, "返回首页", "value")
    box_define = Common.get_content(config_purchasereturn_order, "弹框确认按钮", "value")
    modify_btn = Common.get_content(config_purchasereturn_order, "改价", "value")
    add_btn = Common.get_content(config_purchasereturn_order, "加按钮", "value")
    return_define = Common.get_content(config_purchasereturn_order, "确认退货", "value")
    modify_edit = Common.get_content(config_purchasereturn_order, "改价输入", "value")
    purchase_return_status = Common.get_content(config_purchasereturn_order, "采购退货成功", "value")
    settlement_type = Common.get_content(config_purchasereturn_order, "采购退货单详情结算方式", "value")
    # purchase_return_order = Common.get_content(config_purchasereturn_order, "采购退货单单号", "value")
    # purchase_return_num = Common.get_content(config_purchasereturn_order, "退货数量", "value")

    # sql语句
    config1 = Common.read_config('/db/purchasereturnSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    # sql1 = Common.get_content(config1, "采购单单号查询语句", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")
    sql3 = Common.get_content(config1, "采购退货单作废单号查询", "sql")

    # 进入采购单界面
    def enter_puchas_return_eorder_interface(self):
        logging.info(r'进入库存模块')
        self.click(self.purchase_btn)
        logging.info(r'进入采购退货单界面')
        self.click_text(self.purchase_return_order_btn)

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, supplier_name=None, status=None):
        logging.info(r'点击筛选按钮')
        self.click(self.filter_btn)
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.keyword_edit, keyword)
        if settlement is not None:
            logging.info('输入开始时间')
            self.click(self.choose_settlement)
            self.click_text(settlement)
        if supplier_name is not None:
            logging.info('选择供应商')
            self.click(self.choose_supplier)
            self.click_text(supplier_name)
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

    # 进入单据详情
    def enter_order_detail(self):
        logging.info('进入订单详情')
        self.click(self.goods_name)

    # 对单据进行操作
    def operating_document_action(self, obsolete=False, copy=False):
        self.enter_order_detail()
        if obsolete is True:
            logging.info(r'作废单据')
            self.click(self.operation_action_btn)
            logging.info(r'点击作废')
            self.click(self.invalid_btn)
            logging.info(r'点击确认')
            self.click(self.box_define)
        if copy is True:
            logging.info(r'复制订单')
            self.click(self.operation_action_btn)
            logging.info(r'点击复制订单')
            self.click(self.copy_btn)
            logging.info(r'点击确认')
            self.click(self.box_define)

    # 复制后续操作
    def copy_follow_operation(self, name, is_original=False):
        if is_original is False:
            logging.info(r'进入供应商选择界面')
            self.click(self.choose_supplier)
            logging.info(r'选择供应商')
            self.click_text(name)
            logging.info(r'确认入库')
            self.click(self.return_define)
        else:
            logging.info(r'确认入库')
            self.click(self.return_define)

    # 检查数据库商品库存
    def check_stock_qty(self, name):
        array = self.select_data_from_db(self.sql2)
        for i in range(0, len(array)):
            if array[i]['goods_name'] == name:
                num = array[i]['stockQty']
                return int(num)

    # 检查作废采购单单号
    def check_invalid_purchase_ordernum(self):
        res = str(self.select_data_from_db(self.sql3)[0]['order_code'])
        return res

    # 获取采购退货成功状态
    def get_purchase_return_status(self):
        text = self.get_text(self.purchase_return_status)
        if text == '采购退货成功':
            return True

    # 获取采购单退货生成的采购退货单单号
    def get_purchase_return_order_num(self):
        order_num = self.get_text(self.purchase_return_ordernum)
        return order_num

    # 采购退货单详情采购单单号
    def get_detail_ptuchase_order(self):
        order_num = self.get_text(self.purchase_return_ordernum)
        return order_num

    def get_detail_settlement_type(self):
        settlement = self.get_text(self.settlement_type)
        return settlement

    # 获取采购成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.purchase_return_status)
        if text == r'采购单录入成功':
            return True
        else:
            return False

    # 采购退货单操作
    def purchase_return_order_action(self, keyword=None, settlement=None, supplier_name=None, status=None,
                                     copy=False, obsolete=False, is_original=False):
        self.enter_puchas_return_eorder_interface()
        self.filter_order(keyword=keyword, settlement=settlement, supplier_name=supplier_name, status=status)
        self.enter_order_detail()
        self.operating_document_action(copy=copy, obsolete=obsolete)
        if copy:
            self.copy_follow_operation(supplier_name, is_original=is_original)
