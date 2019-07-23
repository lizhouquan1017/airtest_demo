# coding:utf-8
import logging
from selenium.common.exceptions import NoSuchElementException
from baseView.baseView import BaseView
from tools.common import Common
from airtest.core.api import *


class LoginView(BaseView):

    # 登录页面元素
    config = Common.read_config('/page/loginView.ini')
    username_value = Common.get_content(config, "用户名输入框", "value")
    password_value = Common.get_content(config, "密码输入框", "value")
    loginBtn_value = Common.get_content(config, "登录按钮", "value")
    changeLoginBtn_value = Common.get_content(config, "验证码登录", "value")
    code_value = Common.get_content(config, "验证码输入框", "value")
    experienceBtn_value = Common.get_content(config, "体验按钮", "value")
    today_sales_value = Common.get_content(config, "今日销售额", "value")

    # 登录成功
    def login_action(self, username, password):
        try:
            logging.info(r'==登录操作开始==')
            logging.info('输入用户名:%s' % username)
            self.type(self.username_value, username)
            logging.info('输入密码:%s' % password)
            self.type(self.password_value, password)
            logging.info('点击登录按钮')
            self.click(self.loginBtn_value)
            logging.info('登录完成')
        except NoSuchElementException:
            snapshot('元素未出现')

    # 验证码登录
    def login_code_action(self, username, code):
        try:
            logging.info('==验证码登录用例开始==')
            self.click(self.changeLoginBtn_value)
            logging.info('输入用户名:%s' % username)
            self.type(self.username_value, username)
            logging.info('输入验证码:%s' % code)
            self.type(self.code_value, code)
            logging.info('点击登录按钮')
            self.click(self.loginBtn_value)
            logging.info('==检查验证码登录状态==')
        except NoSuchElementException:
            snapshot('元素未出现')

    # 体验账号登录
    def login_experience_account_action(self):
        logging.info('==体验账号登录==')
        self.click(self.experienceBtn_value)
        logging.info(r'体验账号登录状态验证开始')

    # 检查登录成功状态
    def check_login_success_status(self):
        logging.info('==检查登录成功状态==')
        flag = self.is_exists(self.today_sales_value)
        logging.info(flag)
        if flag:
            logging.info('验证状态成功！用例成功！')
            return True
        else:
            return False

    # 检查登录失败状态
    def check_login_fail_status(self):
        logging.info('==检查登录失败状态')
        flag = self.is_exists(self.loginBtn_value)
        logging.info(flag)
        if flag:
            logging.info('验证状态成功！用例成功！')
            return True
        else:
            return False

