# coding:utf-8

from businessView.goodsView import GoodsViews
from businessView.loginView import LoginView
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.common import Common


class GoodsTest(StartEnd, TestCase_):
    config = Common.read_config('/db/goodsSQL.ini')
    sql1 = Common.get_content(config, "新增商品查询", "sql")
    sql2 = Common.get_content(config, "下架商品查询", "sql")

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 正常添加商品
    def test_01_add_case(self):
        """正常添加商品"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.add_goods('测试商品1号', 100, 200)
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        status = goods.check_success_status()
        self.assertEqual('测试商品1号', goods_name)
        self.assertEqual('添加新品成功', status)

    # 商品下架
    def test_02_obtained_case(self):
        """商品下架功能"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.goods_obtained_action()
        goods_name = goods.select_data_from_db(self.sql2)[0]['goods_name']
        status = goods.check_obtained_status()
        self.assertEqual('该商品已下架', status)
        self.assertEqual('测试商品1号', goods_name)

    # 商品上架
    def test_03_shelf_case(self):
        """商品上架"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.goods_shelf_action()
        goods_name = goods.select_data_from_db(self.sql1)[0]['goods_name']
        self.assertEqual('测试商品1号', goods_name)

    # 商品删除操作
    def test_04_delete_case(self):
        """删除商品"""
        self.login_action()
        goods = GoodsViews()
        goods.enter_goods_list()
        goods.goods_delete_action()
        goods_name = goods.select_data_from_db(self.sql1)
        self.assertNotEqual('测试商品1号', goods_name)

