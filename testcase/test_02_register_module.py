# coding:utf-8
from businessView.registerView import RegisterView
from tools.startend import StartEnd
from tools.TestCaase import TestCase_

import logging


class RegisterTest(StartEnd, TestCase_):

    # 正常注册
    def test_01_user_register(self):
        """正常注册"""
        logging.info('=用户正常注册成功=')
        register = RegisterView()
        data = register.get_csv_data('../data/register.csv', 1)
        register.register_action(data[0], data[2], data[3])
        newdata = str(int(data[0])+1)
        self.assertTrue(register.check_register_success_status())
        register.update_csv_data('../data/register.csv', 1, '用户正常注册', data[0], newdata)

    # 注册手机号为空
    def test_02_register_phonenumEmpty(self):
        """注册手机号为空"""
        logging.info('=用户注册手机号码为空=')
        register = RegisterView()
        data = register.get_csv_data('../data/register.csv', 2)
        register.register_common_action(data[0], data[1], data[2])
        self.assertTrue(register.check_register_fail_status())

    # 注册手机号格式不正确
    def test_03_register_phonenumError(self):
        """注册手机号格式不正确"""
        logging.info('=用户注册手机号格式错误=')
        register = RegisterView()
        data = register.get_csv_data('../data/register.csv', 3)
        register.register_common_action(data[0], data[1], data[2])
        self.assertTrue(register.check_register_fail_status())

    # 注册手机号已注册
    def test_04_registered(self):
        """注册手机号已注册"""
        logging.info('=用户手机号已注册=')
        register = RegisterView()
        data = register.get_csv_data('../data/register.csv', 4)
        register.register_common_action(data[0], data[1], data[2])
        self.assertTrue(register.check_register_fail_status())
