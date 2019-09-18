# coding:utf-8
import logging
import time
from baseView.baseView import BaseView
from tools.common import Common


class PurchaseView(BaseView):

    config = Common.read_config('/page/purchaseView.ini')
    purchase_btn = Common.get_content(config, "库存按钮", "value")
    purchase_interface = Common.get_content(config, "采购进货", "value")
    chooseGoods_value = Common.get_content(config, "选择已有商品", "value")
    add_btn = Common.get_content(config, "加减按钮", "value")
    goods_confirm_btn = Common.get_content(config, "商品确认按钮", "value")
    confirm_btn = Common.get_content(config, "确认按钮", "value")
    goods_list_interface = Common.get_content(config, "商品列表界面", "value")
    supplier_choose = Common.get_content(config, "供应商选择", "value")
    supplier_add = Common.get_content(config, "供应商新增", "value")
    supplier_swipe1 = Common.get_content(config, "供应商滑动块", "value1")
    supplier_swipe2 = Common.get_content(config, "供应商滑动块", "value2")
    supplier_swipe3 = Common.get_content(config, "供应商滑动块", "value3")
    supplier_edit_btn = Common.get_content(config, "供应商编辑", "value")
    supplier_edit = Common.get_content(config, "供应商编辑输入框", "value")
    supplier_enable_disable_btn = Common.get_content(config, "供应商启禁用", "value")
    supplier_tab1 = Common.get_content(config, "启禁用供应商tab", "value1")
    supplier_tab2 = Common.get_content(config, "启禁用供应商tab", "value2")
    supplier_tab3 = Common.get_content(config, "启禁用供应商tab", "value3")
    supplier_tab4 = Common.get_content(config, "启禁用供应商tab", "value4")
    goods_delete_btn = Common.get_content(config, "采购列表删除", "value")
    purchase_transaction = Common.get_content(config, "交易状态", "value")
    purchase_ordernum = Common.get_content(config, "采购单单号", "value")
    modfiy_btn = Common.get_content(config, "采购改价", "value")
    price_edit = Common.get_content(config, "悬浮框价格输入框", "value")
    box_define = Common.get_content(config, "悬浮框确认", "value")
    order_total_money_value = Common.get_content(config, "订单总金额", "value")
    purchase_detail = Common.get_content(config, "查看详情", "value")
    continue_purchase = Common.get_content(config, "继续入库", "value")
    go_home = Common.get_content(config, "回到首页", "value")
    purchase_total_num = Common.get_content(config, "采购数", "value")

    # sql语句
    config1 = Common.read_config('/db/purchaseSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config1, "采购单单号查询语句", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")
    sql3 = Common.get_content(config1, "供应商状态", "sql")
    sql4 = Common.get_content(config1, "供应商新状态", "sql")

    # 进入采购界面
    def enter_purchase_interface(self):
        logging.info(r'进入库存模块')
        self.click(self.purchase_btn)
        logging.info(r'进入采购进货界面')
        self.click_text(self.purchase_interface)

    # 新建供应商
    def add_supplier(self, name):
        self.enter_purchase_interface()
        logging.info('点击进入供应商界面')
        self.click(self.supplier_choose)
        logging.info('点击新增按钮')
        self.click(self.supplier_add)
        logging.info('输入供应商名称')
        self.type(self.supplier_edit, name)
        logging.info('点击确认')
        self.click(self.box_define)

    # 供应商启禁用
    def supplier_enable_disable(self, name, flag=True,):
        self.enter_purchase_interface()
        logging.info('点击进入供应商界面')
        self.click(self.supplier_choose)
        status = self.select_data_from_db(self.sql3)
        for i in range(0, len(status)):
            if flag is True:
                if status[i]['supplier_name'] == name and status[i]['common_status'] == 0:
                    pass
                elif status[i]['supplier_name'] == name and status[i]['common_status'] == 1:
                    self.switch_supplier_tab('禁用供应商')
                    logging.info('滑动供应商')
                    self.swipe_supplier(name)
                    logging.info('点击启用')
                    self.click(self.supplier_enable_disable_btn)
            elif flag is False:
                if status[i]['supplier_name'] == name and status[i]['common_status'] == 1:
                    pass
                elif status[i]['supplier_name'] == name and status[i]['common_status'] == 0:
                    self.switch_supplier_tab('启用供应商')
                    logging.info('滑动供应商')
                    self.swipe_supplier(name)
                    logging.info('点击禁用')
                    self.click(self.supplier_enable_disable_btn)

    # 切换供应商tab
    def switch_supplier_tab(self, name):
        elements = self.get_elements(self.supplier_tab1, self.supplier_tab2, self.supplier_tab3,
                                     self.supplier_tab4)
        for i in range(0, len(elements)):
            if elements[i].get_text() == name:
                elements[i].click()

    # 滑动对应供应商
    def swipe_supplier(self, name):
        elements = self.get_elements(self.supplier_swipe1, self.supplier_swipe2)
        for i in range(0, len(elements)):
            if elements[i].get_text() == name:
                elements[i].parent().parent().swipe((-0.5, 0))

    # 编辑供应商
    def edit_supplier(self, old_name, new_name):
        self.enter_purchase_interface()
        logging.info('点击进入供应商界面')
        self.click(self.supplier_choose)
        logging.info('滑动需要编辑的供应商')
        self.swipe_supplier(old_name)
        logging.info('点击按钮')
        self.click(self.supplier_edit_btn)
        logging.info('输入供应商名称')
        self.type(self.supplier_edit, new_name)
        logging.info('点击确认')
        self.click(self.box_define)

    # 采购选购商品
    def choose_goods_action(self, name):
        logging.info(r'点击选择已有商品')
        self.click_text(self.chooseGoods_value)
        logging.info(r'选择商品')
        self.click_text(name)
        logging.info(r'添加商品数量')
        self.click(self.add_btn)
        logging.info(r'确认选择商品')
        self.click(self.goods_confirm_btn)
        logging.info(r'商品列表界面确认')
        self.click(self.confirm_btn)

    # 选择供应商
    def choose_supplier(self, supplier_name):
        logging.info(r'进入供应商选择界面')
        self.click(self.supplier_choose)
        logging.info(r'选择供应商')
        self.click_text(supplier_name)

    # 获取供应商状态
    def get_supplier_status(self, name):
        supplier_name = self.select_data_from_db(self.sql4)[0]['supplier_name']
        if supplier_name == name:
            status = self.select_data_from_db(self.sql4)[0]['common_status']
            return int(status)

    # 确认入库
    def define_storage_action(self):
        logging.info(r'确认入库')
        self.click(self.confirm_btn)

    # 改价
    def modfiy_price_action(self,value):
        logging.info(r'改价操作')
        self.click(self.modfiy_btn)
        logging.info(r'悬浮框改价按钮')
        self.click(self.modfiy_btn)
        logging.info(r'输入修改价格')
        self.type(self.price_edit, value)
        logging.info(r'点击改价确认')
        self.click(self.box_define)
        logging.info(r'确认选择商品')
        self.click(self.goods_confirm_btn)

    # 获取采购成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.purchase_transaction)
        if text == r'采购单录入成功':
            return True
        else:
            return False

    # 获取界面采购单单号
    def get_purchase_order_num(self):
        logging.info(r'获取采购单单号')
        purchase_order_num = self.get_text(self.purchase_ordernum)
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
        logging.info(r'获取采购数量')
        num = self.get_text(self.purchase_total_num)
        return int(num)

