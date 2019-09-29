# coding:utf-8
import logging
from baseView.baseView import BaseView
from tools.common import Common


class PurchaseOrderView(BaseView):

    config_purchase_order = Common.read_config('/page/purchaseorderView.ini')
    config_purchase = Common.read_config('/page/purchaseView.ini')
    purchase_btn = Common.get_content(config_purchase_order, "库存按钮", "value")
    purchaseorder_btn = Common.get_content(config_purchase_order, "采购单界面", "value")
    goods_name = Common.get_content(config_purchase_order, "采购单列表商品名称", "value")
    filter_btn = Common.get_content(config_purchase_order, "采购单列表筛选按钮", "value")
    keyword_edit = Common.get_content(config_purchase_order, "关键字输入框", "value")
    purchase_order_data = Common.get_content(config_purchase_order, "采购单列表单据生成时间", "value")
    purchase_order_cost = Common.get_content(config_purchase_order, "采购单列表成本价", "value")
    purchase_order_goods_num = Common.get_content(config_purchase_order, "采购单列表采购商品数量", "value")
    purchase_order_total_money = Common.get_content(config_purchase_order, "采购单列表单据总金额", "value")
    return_btn = Common.get_content(config_purchase_order, "采购单详情退货按钮", "value")
    creat_time_start = Common.get_content(config_purchase_order, "创建时间", "value1")
    creat_time_end = Common.get_content(config_purchase_order, "创建时间", "value2")
    time_year = Common.get_content(config_purchase_order, "时间框", "value1")
    time_month = Common.get_content(config_purchase_order, "时间框", "value2")
    time_day = Common.get_content(config_purchase_order, "时间框", "value3")
    swipe_define = Common.get_content(config_purchase_order, "滑动框确认", "value")
    choose_settlement = Common.get_content(config_purchase_order, "选择结算方式", "value")
    settlement_value = Common.get_content(config_purchase_order, "结算类型值", "value")
    choose_supplier = Common.get_content(config_purchase_order, "选择供应商", "value")
    supplier_name = Common.get_content(config_purchase_order, "采购单列表供应商名称", "value")
    is_return = Common.get_content(config_purchase_order, "有无退货", "value")
    choose_status = Common.get_content(config_purchase_order, "状态选择", "value")
    status_module = Common.get_content(config_purchase_order, "状态滑动框", "value")
    filter_define_btn = Common.get_content(config_purchase_order, "筛选界面确认按钮", "value")
    purchase_ordernum = Common.get_content(config_purchase_order, "采购单详情中采购单号", "value")
    operation_action_btn = Common.get_content(config_purchase_order, "采购单详情操作按钮", "value")
    invalid_btn = Common.get_content(config_purchase_order, "作废订单", "value")
    copy_btn = Common.get_content(config_purchase_order, "复制订单", "value")
    back_btn = Common.get_content(config_purchase_order, "返回首页", "value")
    box_define = Common.get_content(config_purchase_order, "弹框确认按钮", "value")
    modify_btn = Common.get_content(config_purchase_order, "改价", "value")
    add_btn = Common.get_content(config_purchase_order, "加按钮", "value")
    return_define = Common.get_content(config_purchase_order, "退货确认", "value")
    modify_edit = Common.get_content(config_purchase_order, "改价输入", "value")
    purchase_return_status = Common.get_content(config_purchase_order, "采购退货成功", "value")
    purchase_return_order = Common.get_content(config_purchase_order, "采购退货单单号", "value")
    purchase_order = Common.get_content(config_purchase_order, "原始采购单单号", "value")
    purchase_return_num = Common.get_content(config_purchase_order, "退货数量", "value")

    # 采购界面
    purchase_choose_supplier = Common.get_content(config_purchase, "供应商选择", "value")
    confirm_storage_btn = Common.get_content(config_purchase, "确认按钮", "value")
    purchase_transaction = Common.get_content(config_purchase, "交易状态", "value")

    # sql语句
    config1 = Common.read_config('/db/purchaseSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config1, "采购单单号查询语句", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")
    sql3 = Common.get_content(config1, "作废采购单号查询", "sql")

    # 进入采购单界面
    def enter_puchaseorder_interface(self):
        logging.info(r'进入库存模块')
        self.click(self.purchase_btn)
        logging.info(r'进入采购单界面')
        self.click_text(self.purchaseorder_btn)

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, supplier_name=None, returned=None, status=None):
        logging.info(r'点击筛选按钮')
        self.click(self.filter_btn)
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.keyword_edit, keyword)
        if settlement is not None:
            logging.info('结算方式')
            self.click(self.choose_settlement)
            self.click_text(settlement)
        if supplier_name is not None:
            logging.info('选择供应商')
            self.click(self.choose_supplier)
            self.click_text(supplier_name)
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
    def copy_follow_operation(self, name):
        logging.info(r'进入供应商选择界面')
        self.click(self.purchase_choose_supplier)
        logging.info(r'选择供应商')
        self.click_text(name)
        logging.info(r'确认入库')
        self.click(self.confirm_storage_btn)

    # 退货
    def purchase_order_return(self, modify=False, price=None):
        logging.info('进入订单详情')
        self.click(self.goods_name)
        logging.info('点击退货按钮')
        self.click(self.return_btn)
        if modify is True:
            logging.info('点击改价按钮')
            self.click(self.modify_btn)
            logging.info('输入修改后价格')
            self.type(self.modify_edit, price)
            self.click(self.box_define)
        logging.info('点击添加商品')
        self.click(self.add_btn)
        self.click(self.return_define)
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
        order_num = self.get_text(self.purchase_return_order)
        return order_num

    # 获取原始采购单单号
    def get_purchase_order_num(self):
        order_num = self.get_text(self.purchase_order)
        return order_num

    # 获取退货数量
    def get_return_num(self):
        list = self.get_text(self.purchase_return_num)
        num = list[0]
        return int(num)

    # 采购单详情采购单单号
    def get_detail_ptuchase_order(self):
        order_num = self.get_text(self.purchase_ordernum)
        return order_num

    # 获取采购成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.purchase_transaction)
        if text == r'采购单录入成功':
            return True
        else:
            return False
