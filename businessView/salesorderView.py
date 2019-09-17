# coding:utf-8
import logging, time
from baseView.baseView import BaseView
from tools.common import Common


class SalesOrderView(BaseView):

    # 销售单界面
    config = Common.read_config('/page/salesorderView.ini')
    stock_btn = Common.get_content(config, "库存按钮", "value")
    sales_btn = Common.get_content(config, "销售单按钮", "value")
    filter_btn = Common.get_content(config, "筛选按钮", "value")
    keyword_edit = Common.get_content(config, "单号输入按钮", "value")
    filter_define_btn = Common.get_content(config, "筛选确认按钮", "value")
    goodsname = Common.get_content(config, "商品列表名称", "value")
    operating_btn = Common.get_content(config, "销售单详情操作按钮", "value")
    obsolete_btn = Common.get_content(config, "作废按钮", "value")
    copy_btn = Common.get_content(config, "复制按钮", "value")
    gohome_btn = Common.get_content(config, "返回首页按钮", "value")
    return_btn = Common.get_content(config, "销售单退货按钮", "value")
    box_define_btn = Common.get_content(config, "弹框确认", "value")

    # 首页界面
    config3 = Common.read_config('/page/cashierView.ini')
    payBtn_value = Common.get_content(config3, "结账", "value")
    cashBtn_value = Common.get_content(config3, "收款类型", "value")
    confirmCashBtn_value = Common.get_content(config3, "确认收款", "value")
    transaction_value = Common.get_content(config3, "交易状态", "value")
    total_money_value = Common.get_content(config3, "实际收款金额", "value")
    sales_order_num_value = Common.get_content(config3, "销售单单号", "value")

    # sql语句
    config1 = Common.read_config('/db/salesSQL.ini')
    config2 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config1, "销售单作废查询", "sql")
    sql2 = Common.get_content(config2, "商品库存查询语句", "sql")

    # 进入销售单界面
    def enter_sales_order_action(self):
        logging.info(r'点击库存按钮')
        self.click(self.stock_btn)
        logging.info(r'点击进入销售单界面')
        self.click_text(self.sales_btn)

    # 查询销售单进入详情
    def enter_sales_order_details_action(self, ordernum):
        logging.info(r'点击筛选按钮')
        self.click(self.filter_btn)
        logging.info(r'输入销售单单号')
        self.type(self.keyword_edit, ordernum)
        logging.info(r'点击确认')
        self.click(self.filter_define_btn)
        logging.info(r'进入销售单详情')
        self.click(self.goodsname)

    # 结账action
    def pay_bill_action(self):
        logging.info(r'去结账')
        self.click(self.payBtn_value)
        logging.info(r'现金支付')
        self.click_text(self.cashBtn_value)
        logging.info('确认收银')
        self.click(self.confirmCashBtn_value)

    # 作废操作
    def obsolete_action(self, ordernum):
        self.enter_sales_order_action()
        self.enter_sales_order_details_action(ordernum)
        logging.info(r'点击操作按钮')
        self.click(self.operating_btn)
        logging.info(r'点击作废按钮')
        self.click(self.obsolete_btn)
        logging.info(r'点击确认')
        self.click(self.box_define_btn)

    # 复制操作并结账
    def copy_pay_action(self, ordernum):
        self.enter_sales_order_action()
        self.enter_sales_order_details_action(ordernum)
        logging.info(r'点击操作按钮')
        self.click(self.operating_btn)
        logging.info(r'点击复制按钮')
        self.click(self.copy_btn)
        logging.info(r'点击确认按钮')
        self.click(self.box_define_btn)
        logging.info(r'去结账')
        self.pay_bill_action()

    # 返回首页按钮
    def go_home_action(self, ordernum):
        self.enter_sales_order_action()
        self.enter_sales_order_details_action(ordernum)
        logging.info(r'点击返回首页')
        self.click(self.gohome_btn)

    # 检查交易成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.transaction_value)
        if text == r'交易成功':
            return True

    # 获取交易价格
    def get_order_price(self):
        logging.info(r'获取订单金额')
        price = self.get_text(self.total_money_value)
        return price

    # 获取销售单号
    def get_sales_order_num(self):
        logging.info(r'获取采购单单号')
        sales_order_num = self.get_text(self.sales_order_num_value)
        return sales_order_num

    # 检查数据库商品库存
    def check_stock_qty(self, name):
        arraylist = self.select_data_from_db(self.sql2)
        for i in range(0, len(arraylist)):
            if arraylist[i]['goods_name'] == name:
                num = arraylist[i]['stockQty']
                return num

    # 检查作废采购单单号
    def check_invalid_purchase_ordernum(self):
        res = str(self.select_data_from_db(self.sql1)[0]['order_code'])
        return res
