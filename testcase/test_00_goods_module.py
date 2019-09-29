# coding:utf-8

from businessView.goodsView import GoodsViews
from businessView.loginView import LoginView
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.common import Common
from tools.readCfg import ReadData


class GoodsTest(StartEnd, TestCase_):
    config = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config, "新增商品查询", "sql")
    sql2 = Common.get_content(config, "下架商品查询", "sql")
    sql3 = Common.get_content(config, "尺码规则组查询", "sql")
    sql4 = Common.get_content(config, "颜色规则组查询", "sql")
    sql5 = Common.get_content(config, "自定义分类查询", "sql")
    sql6 = Common.get_content(config, "编辑商品查询", "sql")

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 正常添加商品
    def test_01_add_case(self):
        """正常添加商品"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        """
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.type_must_field('测试商品1号', 100, 200, '均色', '均码')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_num = goods.get_sku_barcode()
        ReadData().write_data('goods_bar_code', 'num', goods_num)
        ReadData().write_data('goods_single_barcode', 'num', sku_num)
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        self.assertEqual('测试商品1号', goods_name)
        self.assertEqual('添加新品成功', status)

    def test_02_add_case(self):
        """自定义商品货号添加商品"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.type_must_field('测试商品2号', 100, 200, '均色', '均码', 19891017)
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData().write_data('goods_bar_code', 'num', goods_num)
        ReadData().write_data('goods_single_barcode', 'num', sku_code)
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        self.assertEqual('测试商品2号', goods_name)
        self.assertEqual('添加新品成功', status)
        self.assertEqual('19891017-01', sku_code)

    def test_03_add_case(self):
        """自定义商品货号添加商品,添加初始库存"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.type_must_field('测试商品3号', 100, 200, '均色', '均码', 19891018, 10)
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_code = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        stock_num = goods.get_stock_num()
        ReadData().write_data('goods_bar_code', 'num', goods_code)
        ReadData().write_data('goods_single_barcode', 'num', sku_code)
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        self.assertEqual('测试商品3号', goods_name)
        self.assertEqual('添加新品成功', status)
        self.assertEqual('19891018-01', sku_code)
        self.assertEqual('10', stock_num)

    def test_04_add_case(self):
        """自定义商品货号添加商品,添加初始库存，添加商品条码"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.type_must_field('测试商品4号', 50, 90.4, '均色', '均码', 19891019, 50, '20190916-01')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        goods_bar_code = goods.get_goods_barcode()
        sku_code = goods.get_sku_barcode()
        stock_num = goods.get_stock_num()
        ReadData().write_data('goods_bar_code', 'num', goods_num)
        ReadData().write_data('goods_single_barcode', 'num', sku_code)
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        self.assertEqual('测试商品4号', goods_name)
        self.assertEqual('添加新品成功', status)
        self.assertEqual('19891019-01', sku_code)
        self.assertEqual('10', stock_num)
        self.assertEqual('20190916-01', goods_bar_code)

    def test_05_add_case(self):
        """自定义商品货号添加商品,添加初始库存，添加商品条码,添加备注"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.type_must_field('测试商品5号', 100, 200, '均色', '均码', 19891020, 80, '20190917-01', '测试商品备注')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        goods_bar_code = goods.get_goods_barcode()
        sku_code = goods.get_sku_barcode()
        stock_num = goods.get_stock_num()
        ReadData().write_data('goods_bar_code', 'num', goods_num)
        ReadData().write_data('goods_single_barcode', 'num', sku_code)
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        goods_remarks = goods.select_data_from_db(self.sql1)[0]['remarks']
        self.assertEqual('测试商品5号', goods_name)
        self.assertEqual('添加新品成功', status)
        self.assertEqual('19891020-01', sku_code)
        self.assertEqual('10', stock_num)
        self.assertEqual('20190917-01', goods_bar_code)
        self.assertEqual('测试商品备注', goods_remarks)

    def test_06_add_case(self):
        """自定义商品货号添加商品,添加初始库存，添加商品条码,添加备注，添加其他参数"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.type_must_field('测试商品6号', 100, 200, '均色', '均码',
                              19891021, 10, '20190918', '测试商品备注', 20, 50, '件', '棉', '春季', '长款', 'LV')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        other_parameter = goods.get_other_parameter()
        print(other_parameter)
        goods_num = goods.get_goods_num()
        goods_bar_code = goods.get_goods_barcode()
        sku_code = goods.get_sku_barcode()
        stock_num = goods.get_stock_num()
        ReadData().write_data('goods_bar_code', 'num', goods_num)
        ReadData().write_data('goods_single_barcode', 'num', sku_code)
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        goods_remarks = goods.select_data_from_db(self.sql1)[0]['remarks']
        self.assertEqual('测试商品6号', goods_name)
        self.assertEqual('添加新品成功', status)
        self.assertEqual('19891021-01', sku_code)
        self.assertEqual('10', stock_num)
        self.assertEqual('20190918', goods_bar_code)
        self.assertEqual('测试商品备注', goods_remarks)

    # 商品下架
    def test_07_obtained_case(self):
        """商品下架功能"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.goods_obtained_action()
        goods_name = goods.select_data_from_db(self.sql2)[0]['goods_name']
        status = goods.check_obtained_status()
        self.assertEqual('该商品已下架', status)
        self.assertEqual('测试商品6号', goods_name)

    # 商品上架
    def test_08_shelf_case(self):
        """商品上架"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.goods_shelf_action()
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        self.assertEqual('测试商品6号', goods_name)

    # 商品删除操作
    def test_09_delete_case(self):
        """删除商品"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.goods_delete_action()
        goods_name = goods.select_data_from_db(self.sql1)
        self.assertNotEqual('测试商品6号', goods_name)

    # 列表编辑
    def test_10_edit_case(self):
        """列表编辑商品"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.list_edit_action('测试商品7号')
        goods_name = goods.select_data_from_db(self.sql6)
        self.assertNotEqual('测试商品7号', goods_name)

    # 列表编辑
    def test_11_edit_case(self):
        """详情编辑商品"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.details_edit_action('测试商品8号')
        goods_name = goods.select_data_from_db(self.sql6)
        self.assertNotEqual('测试商品8号', goods_name)

    # 新增颜色规则组
    def test_12_add_color_group(self):
        """新增颜色规则组"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.add_color_rule_group('新增颜色规则组1')
        color_group_name = goods.select_data_from_db(self.sql4)[0]['propvaluegroup_name']
        self.assertEqual('新增颜色规则组1', color_group_name)

    # 编辑颜色规则组
    def test_13_edit_color_group(self):
        """编辑颜色规则组"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.edit_color_rule_group('新增颜色规则组2')
        color_group_name = goods.select_data_from_db(self.sql4)[0]['propvaluegroup_name']
        self.assertEqual('新增颜色规则组2', color_group_name)

    # 删除颜色规则组
    def test_14_delete_color_group(self):
        """删除颜色规则组"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.delete_color_rule_group()
        color_group_name = goods.select_data_from_db(self.sql3)
        self.assertNotEqual('新增尺码规则组2', color_group_name)

    # 新增尺码规则组
    def test_15_add_size_group(self):
        """新增尺码规则组"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.add_size_rule_group('新增尺码规则组1')
        size_group_name = goods.select_data_from_db(self.sql3)[0]['propvaluegroup_name']
        self.assertEqual('新增尺码规则组1', size_group_name)

    # 编辑尺码规则组
    def test_16_edit_size_group(self):
        """编辑尺码规则组"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.edit_size_rule_group('新增尺码规则组2')
        size_group_name = goods.select_data_from_db(self.sql3)[0]['propvaluegroup_name']
        self.assertEqual('新增尺码规则组2', size_group_name)

    # 删除尺码规则组
    def test_17_delete_size_group(self):
        """删除尺码规则组"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.delete_size_rule_group()
        size_group_name = goods.select_data_from_db(self.sql3)
        self.assertNotEqual('新增尺码规则组2', size_group_name)

    # 新增自定义类目
    def test_18_custom_classification(self):
        """新增自定义类目"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.add_custom_classification('自定义分组1')
        custom_classification_name = goods.select_data_from_db(self.sql5)[0]['goodscat_name']
        self.assertEqual('自定义分组1', custom_classification_name)

    # 编辑自定义类目
    def test_19_custom_classification(self):
        """编辑自定义类目"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.edit_custom_classification('自定义分组2')
        custom_classification_name = goods.select_data_from_db(self.sql5)[0]['goodscat_name']
        self.assertEqual('自定义分组2', custom_classification_name)

    # 删除自定义类目
    def test_20_custom_classification(self):
        """删除自定义类目"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.delete_custom_classification()
        custom_classification_name = goods.select_data_from_db(self.sql5)
        self.assertNotEqual('自定义分组2', custom_classification_name)

    # 新增颜色属性
    def test_21_add_color_prop(self):
        """新增颜色属性"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.add_color_prop('我的颜色1')

    # 编辑颜色属性
    def test_22_edit_color_prop(self):
        """编辑颜色属性"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.edit_color_prop('我的颜色1', '我的颜色2')

    # 删除颜色属性
    def test_23_delete_color_prop(self):
        """删除颜色属性"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.delete_color_prop('我的颜色2')

    # 新增错尺码属性
    def test_24_add_size_prop(self):
        """新增颜色属性"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.add_size_prop('我的尺码1')

    # 编辑颜色属性
    def test_25_edit_size_prop(self):
        """编辑颜色属性"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.edit_size_prop('我的尺码1', '我的尺码2')

    # 删除颜色属性
    def test_26_delete_size_prop(self):
        """删除颜色属性"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.delete_size_prop('我的尺码2')


