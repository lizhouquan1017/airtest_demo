# coding:utf-8

import logging
from baseView.baseView import BaseView
from tools.common import Common
from airtest.core.api import *


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
    size_choose = Common.get_content(config, "尺码选择", "value")
    define_btn = Common.get_content(config, "确认选择", "value")
    save_btn = Common.get_content(config, "保存按钮", "value")
    success_status = Common.get_content(config, "添加成功", "value")
    goods_detail = Common.get_content(config, "查看商品详情", "value")
    go_on_add = Common.get_content(config, "继续添加商品", "value")
    back_home = Common.get_content(config, "返回首页", "value")
    shelf_obtained_btn = Common.get_content(config, "上下架按钮", "value")
    box_define = Common.get_content(config, "弹框确认", "value")
    obtained_status = Common.get_content(config, "下架状态", "value")
    choose_goods = Common.get_content(config, "商品列表名称", "value")
    filter_shelf_btn = Common.get_content(config, "筛选上架", "value")
    filter_obtained_btn = Common.get_content(config, "筛选下架", "value")
    filter_define_btn = Common.get_content(config, "筛选确认", "value")
    details_operating_btn = Common.get_content(config, "商品详情页面操作按钮", "value")
    delete_btn = Common.get_content(config, "删除商品", "value")
    list_action = Common.get_content(config, "列表操作按钮", "value")
    list_edit = Common.get_content(config, "列表编辑按钮", "value")
    details_edit = Common.get_content(config, "详情编辑按钮", "value")
    attribute_rule_group_add = Common.get_content(config, "属性规则组添加", "value")
    attribute_add = Common.get_content(config, "规则属性新增", "value")
    group_input_edit = Common.get_content(config, "规则组输入框", "value")
    group_edit = Common.get_content(config, "规则组编辑", "value")
    group_delete = Common.get_content(config, "规则组删除", "value")
    custom_category = Common.get_content(config, "自定义分类", "value")
    category_name = Common.get_content(config, "自定义分类名称", "value")
    edit_category = Common.get_content(config, "自定义类目编辑", "value")
    delete_category = Common.get_content(config, "自定义类目删除", "value")
    add_product_interface = Common.get_content(config, "新增商品界面", "value")
    category_swipe = Common.get_content(config, "自定义分类滑动", "value")
    property_name_edit = Common.get_content(config, "属性输入框", "value")
    prop_value = Common.get_content(config, "属性值获取", "value")
    prop_grop = Common.get_content(config, "属性值组", "value")
    edit_delete_prop1 = Common.get_content(config, "属性值编辑删除", "value1")
    edit_delete_prop2 = Common.get_content(config, "属性值编辑删除", "value2")
    goods_num = Common.get_content(config, "商品货号", "value")
    sku_num = Common.get_content(config, "单品货号", "value")
    goods_code_edit = Common.get_content(config, "商品货号输入", "value")
    init_stock_num = Common.get_content(config, "初始库存输入", "value")
    add_stock_num_btn = Common.get_content(config, "添加库存数按钮", "value")
    stock_info1 = Common.get_content(config, "库存信息", "value1")
    stock_info2 = Common.get_content(config, "库存信息", "value2")
    stock_info3 = Common.get_content(config, "库存信息", "value3")
    stock_info4 = Common.get_content(config, "库存信息", "value4")
    details_stock_num = Common.get_content(config, "详细信息库存数", "value")
    goods_barcode_edit = Common.get_content(config, "商品条码输入", "value")
    goods_remark = Common.get_content(config, "商品备注", "value")
    high_limt_edit = Common.get_content(config, "库存上限", "value")
    low_limt_edit = Common.get_content(config, "库存下限", "value")
    other_parameter1 = Common.get_content(config, "其他参数", "value1")
    other_parameter2 = Common.get_content(config, "其他参数", "value2")
    other_parameter3 = Common.get_content(config, "其他参数", "value3")
    goods_barcode = Common.get_content(config, "商品条码", "value")
    other_parameter_value = Common.get_content(config, "其他参数值", "value")

    # 进入商品管理界面
    def enter_goods_list(self):
        logging.info('进入商品管理界面')
        self.click_text(self.goods_management)

    # 选择类目
    def choose_category(self):
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

    # 新增商品操作
    def type_must_field(self, goodsname, costprice, saleprice, color_value, size_value, *args):
        """
        :param goodsname:
        :param costprice:
        :param saleprice:
        :param color_value:
        :param size_value:
        :param args:
        :return:
        """
        self.choose_category()
        self.type(self.goods_name_edit, goodsname)
        logging.info('输入成本价')
        self.type(self.goods_purchase_price_edit, costprice)
        logging.info('输入零售价')
        self.type(self.goods_sale_price_edit, saleprice)
        logging.info('点击颜色')
        self.click_text(self.colour_choose)
        logging.info('选择颜色')
        self.choose_prop(color_value)
        logging.info('点击确认')
        self.click(self.define_btn)
        logging.info('点击尺码')
        self.click_text(self.size_choose)
        logging.info('选择尺码')
        self.choose_prop(size_value)
        logging.info('点击确认')
        self.click(self.define_btn)
        if args:
            if len(args) == 2:
                logging.info('添加商品货号')
                self.type(self.goods_code_edit, args[0])
                logging.info('滑动到自定义分类界面')
                self.swipe(self.add_product_interface, 'up', 0, -1)
                logging.info('输入初始库存')
                self.click(self.init_stock_num)
                logging.info('输入库存数')
                for i in range(0, args[1]):
                    self.click(self.add_stock_num_btn)
                logging.info('点击确认')
                self.click(self.define_btn)
            elif len(args) == 3:
                logging.info('添加商品货号')
                self.type(self.goods_code_edit, args[0])
                logging.info('滑动到自定义分类界面')
                self.swipe(self.add_product_interface, 'up', 0, -1)
                logging.info('输入初始库存')
                self.click(self.init_stock_num)
                logging.info('输入库存数')
                for i in range(0, args[1]):
                    self.click(self.add_stock_num_btn)
                logging.info('点击确认')
                self.click(self.define_btn)
                logging.info('商品条码输入')
                self.type(self.goods_barcode_edit, args[2])
            elif len(args) == 4:
                logging.info('添加商品货号')
                self.type(self.goods_code_edit, args[0])
                logging.info('滑动到自定义分类界面')
                self.swipe(self.add_product_interface, 'up', 0, -1)
                logging.info('输入初始库存')
                self.click(self.init_stock_num)
                logging.info('输入库存数')
                for i in range(0, args[1]):
                    self.click(self.add_stock_num_btn)
                logging.info('点击确认')
                self.click(self.define_btn)
                logging.info('商品条码输入')
                self.type(self.goods_barcode_edit, args[2])
                logging.info('输入商品备注')
                self.type(self.goods_remark, args[3])
            # elif len(args) == 6:
            #     logging.info('添加商品货号')
            #     self.type(self.goods_code_edit, args[0])
            #     logging.info('滑动到自定义分类界面')
            #     self.swipe(self.add_product_interface, 'up', 0, -1)
            #     logging.info('输入初始库存')
            #     self.click(self.init_stock_num)
            #     logging.info('输入库存数')
            #     for i in range(0, args[1]):
            #         self.click(self.add_stock_num_btn)
            #     logging.info('点击确认')
            #     self.click(self.define_btn)
            #     logging.info('商品条码输入')
            #     self.type(self.goods_barcode_edit, args[2])
            #     logging.info('输入商品备注')
            #     self.type(self.goods_remark, args[3])
            #     logging.info('输入库存上限')
            #     self.type(self.high_limt_edit, 50)
            #     logging.info('输入库存下限')
            #     self.type(self.low_limt_edit, 5)
            elif len(args) == 11:
                logging.info('添加商品货号')
                self.type(self.goods_code_edit, args[0])
                logging.info('滑动到添加库存界面')
                self.swipe(self.add_product_interface, 'up', 0, -1)
                logging.info('输入初始库存')
                self.click(self.init_stock_num)
                logging.info('输入库存数')
                for i in range(0, args[1]):
                    self.click(self.add_stock_num_btn)
                logging.info('点击确认')
                self.click(self.define_btn)
                logging.info('商品条码输入')
                self.type(self.goods_barcode_edit, args[2])
                logging.info('输入商品备注')
                self.type(self.goods_remark, args[3])
                logging.info('输入库存上限')
                self.type(self.high_limt_edit, args[4])
                logging.info('输入库存下限')
                self.type(self.low_limt_edit, args[5])
                logging.info('滑动到其他参数界面')
                self.swipe(self.add_product_interface, 'up', 0, -0.5)
                logging.info('输入单位')
                self.type_other_parameter('请输入单位信息', args[6])
                logging.info('输入成分')
                self.type_other_parameter('请输入成分信息', args[7])
                logging.info('输入季节')
                self.type_other_parameter('请输入季节信息', args[8])
                logging.info('输入款式')
                self.type_other_parameter('请输入款式信息', args[9])
                logging.info('输入品牌')
                self.type_other_parameter('请输入品牌信息', args[10])
            else:
                logging.info('添加商品货号')
                self.type(self.goods_code_edit, args[0])
        else:
            pass

    # 确认添加
    def confirm_add_goods(self):
        logging.info('点击保存')
        self.click(self.save_btn)

    # 获取商品货号
    def get_goods_num(self):
        logging.info('获取商品货号')
        goods_num = self.get_text(self.goods_num)
        logging.info("商品货号：%s" % goods_num)
        list1 = goods_num.split('：')
        return list1[1]

    # 获取商品条码
    def get_goods_barcode(self):
        logging.info('获取商品条码')
        goods_barcode = self.get_text(self.goods_barcode)
        logging.info("商品条码：%s" % goods_barcode)
        list1 = goods_barcode.split('：')
        return list1[1]

    # 获取其他参数
    def get_other_parameter(self):
        other_parameters = self.get_text(self.other_parameter_value)
        return other_parameters

    # 获取单品货号
    def get_sku_barcode(self):
        logging.info('获取单品货号')
        sku_num = self.get_text(self.sku_num)
        logging.info("单品货号：%s" % sku_num)
        return sku_num

    # 获取库存信息
    def get_stock_num(self):
        logging.info('点击库存信息')
        tab_name = self.get_elements(self.stock_info1, self.stock_info2, self.stock_info3, self.stock_info4)
        for i in range(0, len(tab_name)):
            if tab_name[i].get_text() == '库存信息':
                tab_name[i].click()
        stock_num = self.get_text(self.details_stock_num)
        return stock_num

    # 输入其他参数
    def type_other_parameter(self, value, *args):
        logging.info('输入其他参数')
        tab_name = self.get_elements(self.other_parameter1, self.other_parameter2, self.other_parameter3)
        for i in range(0, len(tab_name)):
            if tab_name[i].get_text() == value:
                tab_name[i].set_text(args)

    # 查看商品详情
    def get_goods_details(self):
        logging.info('查看商品详情')
        self.click(self.goods_detail)

    # 继续添加商品
    def go_on_add_goods(self):
        logging.info('继续添加商品')
        self.click(self.go_on_add)

    # 返回首页
    def go_home(self):
        logging.info('返回首页')
        self.click(self.back_home)

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

    # 删除操作
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

    # 列表编辑操作
    def list_edit_action(self, value):
        logging.info('点击列表操作')
        self.click(self.list_action)
        logging.info('点击编辑')
        self.click(self.list_edit)
        logging.info('修改商品名称')
        self.type(self.goods_name_edit, value)
        logging.info('点击保存')
        self.click(self.save_btn)

    # 详情编辑操作
    def details_edit_action(self, value):
        logging.info('点击商品详情')
        self.click(self.goods_name_edit)
        logging.info('点击编辑')
        self.click(self.details_edit)
        logging.info('修改商品名称')
        self.type(self.goods_name_edit, value)
        logging.info('点击保存')
        self.click(self.save_btn)

    # 新增规则组
    def add_rule_group(self, name, group_name):
        self.choose_category()
        logging.info('点击颜色或者尺码')
        self.click_text(name)
        logging.info('点击添加属性规则组')
        self.click(self.attribute_rule_group_add)
        logging.info('输入规则组名称')
        self.type(self.group_input_edit, group_name)
        logging.info('点击确认')
        self.click(self.box_define)

    # 编辑规则组
    def edit_rule_group(self, name, group_name):
        self.choose_category()
        logging.info('点击颜色或者尺码')
        self.click_text(name)
        logging.info('点击编辑规则组名称')
        self.click(self.group_edit)
        logging.info('输入修改后规则组名称')
        self.type(self.group_input_edit, group_name)
        logging.info('点击确认')
        self.click(self.box_define)

    # 编辑规则组
    def delete_rule_group(self, name):
        self.choose_category()
        logging.info('点击颜色或者尺码')
        self.click_text(name)
        logging.info('点击删除按钮')
        self.click(self.group_delete)
        logging.info('点击确认')
        self.click(self.box_define)

    # 新增自定义分类
    def add_custom_classification(self, name):
        logging.info('点击新增商品')
        self.click(self.add_btn)
        logging.info('滑动到自定义分类界面')
        self.swipe(self.add_product_interface, 'up', 0, -0.8)
        logging.info('点击自定义分类')
        self.click(self.custom_category)
        logging.info('点击新增')
        self.click(self.operating_btn)
        logging.info('输入自定义分类名称')
        self.type(self.category_name, name)
        logging.info('点击确认')
        self.click(self.define_btn)

    # 编辑自定义分类
    def edit_custom_classification(self, name):
        logging.info('点击新增商品')
        self.click(self.add_btn)
        logging.info('滑动到自定义分类界面')
        self.swipe(self.add_product_interface, 'up', 0, -0.8)
        logging.info('点击自定义分类')
        self.click(self.custom_category)
        logging.info('向左滑动已有分类')
        self.swipe(self.category_swipe, 'left', -0.5, 0)
        logging.info('点击编辑')
        self.click(self.edit_category)
        logging.info('输入自定义分类名称')
        self.type(self.category_name, name)
        logging.info('点击确认')
        self.click(self.define_btn)

    # 删除自定义分类
    def delete_custom_classification(self):
        logging.info('点击新增商品')
        self.click(self.add_btn)
        logging.info('滑动到自定义分类界面')
        self.swipe(self.add_product_interface, 'up', 0, -0.8)
        logging.info('点击自定义分类')
        self.click(self.custom_category)
        logging.info('向左滑动已有分类')
        self.swipe(self.category_swipe, 'left', -0.5, 0)
        logging.info('点击删除')
        self.click(self.delete_category)

    # 规则属性新增
    def add_rule_attribute(self, name, prop_name):
        self.choose_category()
        logging.info('点击尺码或者颜色')
        self.click_text(name)
        logging.info('点击新增属性')
        self.click(self.attribute_add)
        logging.info('输入新增属性名称')
        self.type(self.property_name_edit, prop_name)
        logging.info('点击保存')
        self.click(self.define_btn)

    # 判断长按的属性
    def long_cilck_prop(self, value):
        array_list = self.get_elements(self.prop_grop, self.prop_value)
        for i in range(0, len(array_list)):
            if array_list[i].get_text() == value:
                array_list[i].long_click()

    # 选择属性规则
    def choose_prop(self, value):
        array_list = self.get_elements(self.prop_grop, self.prop_value)
        for i in range(0, len(array_list)):
            if array_list[i].get_text() == value:
                array_list[i].click()

    # 判断属性编辑或删除
    def edit_delete_prop(self, value):
        array_list = self.get_elements(self.edit_delete_prop1, self.edit_delete_prop2)
        for i in range(0, len(array_list)):
            if array_list[i].get_text() == value:
                array_list[i].click()

    # 规则属性编辑
    def edit_rule_attribute(self, name, prop_name, new_prop_name):
        self.choose_category()
        logging.info('点击尺码或者颜色')
        self.click_text(name)
        logging.info('点击需要编辑的属性值')
        self.long_cilck_prop(prop_name)
        logging.info('点击编辑')
        self.edit_delete_prop('编辑')
        logging.info('编辑属性名称')
        self.type(self.property_name_edit, new_prop_name)
        logging.info('点击保存')
        self.click(self.define_btn)

    # 规则属性删除
    def delete_rule_attribute(self, name, prop_name):
        self.choose_category()
        logging.info('点击尺码或者颜色')
        self.click_text(name)
        logging.info('点击需要编辑的属性值')
        self.long_cilck_prop(prop_name)
        logging.info('点击删除')
        self.edit_delete_prop('删除')
        logging.info('点击确认')
        self.click(self.box_define)

    # 搜索规则属性
    def search_prop(self, prop_name, porp_value):
        self.choose_category()
        logging.info('点击尺码或者颜色')
        self.click_text(prop_name)
        logging.info('输入查询的属性值')
        self.click(self.search_edit)
        text(porp_value)
        time.sleep(3)
        dev = device()
        dev.yosemite_ime.code("3")

    # 搜索颜色属性
    def search_color_prop(self, porp_value):
        self.search_prop(self.colour_choose, porp_value)

    # 新增颜色属性
    def add_color_prop(self, prop_name):
        self.add_rule_attribute(self.colour_choose, prop_name)

    # 新增尺码属性
    def add_size_prop(self, prop_name):
        self.add_rule_attribute(self.size_choose, prop_name)

    # 编辑颜色属性
    def edit_color_prop(self, prop_name, new_prop_name):
        self.edit_rule_attribute(self.colour_choose, prop_name, new_prop_name)

    # 编辑尺码属性
    def edit_size_prop(self, prop_name, new_prop_name):
        self.edit_rule_attribute(self.size_choose, prop_name, new_prop_name)

    # 删除颜色属性
    def delete_color_prop(self, prop_name):
        self.delete_rule_attribute(self.colour_choose, prop_name)

    # 删除尺码属性
    def delete_size_prop(self, prop_name):
        self.delete_rule_attribute(self.size_choose, prop_name)

    # 新增颜色规则组
    def add_color_rule_group(self, group_name):
        self.add_rule_group(self.colour_choose, group_name)

    # 新增尺码规则组
    def add_size_rule_group(self, group_name):
        self.add_rule_group(self.size_choose, group_name)

    # 编辑颜色规则组
    def edit_color_rule_group(self, group_name):
        self.edit_rule_group(self.colour_choose, group_name)

    # 编辑颜色规则组
    def edit_size_rule_group(self, group_name):
        self.edit_rule_group(self.size_choose, group_name)

    # 删除颜色规则组
    def delete_color_rule_group(self):
        self.delete_rule_group(self.colour_choose)

    # 删除尺码规则组
    def delete_size_rule_group(self):
        self.delete_rule_group(self.size_choose)
