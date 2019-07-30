# coding:utf-8

import logging
from baseView.baseView import BaseView
from tools.common import Common


class SalesOrderReturnView(BaseView):

    # 销售退货单页面控件
    config = Common.read_config('/page/salesorderreturnView.ini')
    inventory_btn = Common.get_content(config, '库存按钮', 'value')
    salesorder_btn = Common.get_content(config, '销售退货单按钮', 'value')
    filter_btn = Common.get_content(config, '筛选按钮', 'value')
    keyword_edit = Common.get_content(config, '关键字输入', 'value')
    define_text = Common.get_content(config, '筛选确认', 'value')
    goods_name = Common.get_content(config, '商品名称', 'value')
    operating_btn = Common.get_content(config, '操作按钮', 'value')
    obsolete_btn = Common.get_content(config, '作废按钮', 'value')
    copy_btn = Common.get_content(config, '复制按钮', 'value')
    gohome_btn = Common.get_content(config, '返回首页按钮', 'value')
    box_define_btn = Common.get_content(config, '弹框确认', 'value')
    home_view = Common.get_content(config, '首页金额', 'value')

    # 销售退货界面控件
    config1 = Common.read_config('/page/salereturnView.ini')
    choose_goods_define = Common.get_content(config1, '选择退货确认按钮', 'value')
    salers_select = Common.get_content(config1, '销售员状态栏', 'value')
    saler = Common.get_content(config1, '销售员姓名', 'value')
    sales_return_ordernum = Common.get_content(config1, '销售退货单单号', 'value')
    total_amount = Common.get_content(config1, '销售退货金额', 'value')
    sales_return_status = Common.get_content(config1, '退货状态', 'value')

    # SQL语句
    config2 = Common.read_config('/db/salesSQL.ini')
    config3 = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config2, "销售退货单作废查询", "sql")
    sql2 = Common.get_content(config3, "商品库存查询语句", "sql")

    # 进入销售退货单界面
    def enter_sales_return_action(self):
        logging.info(r'点击库存')
        self.click(self.inventory_btn)
        logging.info(r'点击销售退货')
        self.click_text(self.salesorder_btn)

    # 操作单据1,2,3，(1.作废，2.复制，3.返回首页)
    def opeterating_sales_return_order(self, flag, ordernum):
        self.enter_sales_return_action()
        logging.info(r'点击筛选按钮')
        self.click(self.filter_btn)
        logging.info(r'输入销售作废单号:%s' % ordernum)
        self.type(self.keyword_edit, ordernum)
        logging.info(r'点击确认')
        self.click(self.define_text)
        logging.info(r'进入销售退货单详情界面')
        self.click(self.goods_name)
        logging.info(r'点击操作按钮')
        self.click(self.operating_btn)
        if flag == 1:
            logging.info(r'点击作废')
            self.click(self.obsolete_btn)
            logging.info(r'点击确认')
            self.click(self.box_define_btn)
        elif flag == 2:
            logging.info(r'点击复制按钮')
            self.click(self.copy_btn)
            logging.info(r'点击确认')
            self.click(self.box_define_btn)
            logging.info(r'点击销售员选择栏')
            self.click(self.salers_select)
            logging.info(r'选择销售员')
            self.click_text(self.saler)
            logging.info(r'点击确认')
            self.click(self.choose_goods_define)
            logging.info(r'点击确认退货')
            self.click(self.choose_goods_define)
        else:
            logging.info(r'点击返回按钮')
            self.click(self.gohome_btn)

    # 获取生成的销售退货单单号
    def get_reutrn_order_num(self):
        ordernum = self.get_text(self.sales_return_ordernum)
        return ordernum

    # 获取采购成功状态
    def check_salesreturn_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.sales_return_status)
        if text == r'退货成功':
            return True
        else:
            return False

    # 获取销售退货单退货价格
    def get_return_order_total_amount(self):
        total_amount = self.get_text(self.total_amount)
        return total_amount

    # 判断是否回到首页
    def check_gohome_status(self):
        flag = self.is_exists(self.home_view)
        return flag

    # 检查数据库商品库存
    def check_stock_qty(self):
        res = self.select_data_from_db(self.sql2)
        num = int(res[0]['stockQty'])
        return num

    # 检查作废采购单单号
    def check_invalid_purchase_ordernum(self):
        res = str(self.select_data_from_db(self.sql1)[0]['order_code'])
        return res
