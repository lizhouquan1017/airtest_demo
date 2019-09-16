# coding:utf-8

from businessView.homeView import HomeViews
from businessView.loginView import LoginView
from tools.startend import StartEnd
from tools.TestCaase import TestCase_
from tools.readCfg import ReadData


class GoodsTest(StartEnd, TestCase_):

    # 登录操作
    def login_action(self):
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 首页搜索商品
    def test_01_home_search_goods(self):
        """首页搜索商品"""
        self.login_action()
        home = HomeViews()
        home.search_goods()
        goods_num = home.get_goods_barcode()
        goods_bar_code = ReadData().get_data('goods_bar_code', 'num')
        self.assertEqual(goods_num, goods_bar_code)
