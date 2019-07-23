# coding:utf-8

import logging, random
from baseView.baseView import BaseView
from tools.common import Common


class RegisterView(BaseView):

    # 注册页面元素
    config = Common.read_config('/page/registerView.ini')
    phoneNumInput_value = Common.get_content(config, '用户名输入框', 'value')
    codeInput_value = Common.get_content(config, '验证码输入框', 'value')
    pwdInput_value = Common.get_content(config, '密码输入框', 'value')
    nextBtn_value = Common.get_content(config, '下一步按钮', 'value')
    loginBack_value = Common.get_content(config, '返回按钮', 'value')
    MerchantBtn_value = Common.get_content(config, '商家按钮', 'value')
    staffBtn_value = Common.get_content(config, '员工按钮', 'value')
    companyNameInput_value = Common.get_content(config, '公司名称输入框', 'value')
    storeNameInput_value = Common.get_content(config, '门店输入框', 'value')
    cityInput_value = Common.get_content(config, '城市选择框', 'value')
    addressInput_value = Common.get_content(config, '详细地址', 'value')
    skipBtn_value = Common.get_content(config, '跳过按钮', 'value')
    startUseBtn_value = Common.get_content(config, '开始使用按钮', 'value')
    registeredBtn_value = Common.get_content(config, '注册按钮', 'value')
    cityConfirmBtn_value = Common.get_content(config, '城市确认按钮', 'value')

    # 首页页面元素
    config1 = Common.read_config('/page/loginView.ini')
    today_sales_value = Common.get_content(config1, "今日销售额", "value")

    # 随机数
    number = random.randint(0, 9999999)

    def register_action(self, register_username, register_code, register_password):
        logging.info('进入注册页面')
        self.click(self.registeredBtn_value)
        logging.info('输入注册手机号: %s' % register_username)
        self.type(self.phoneNumInput_value, register_username)
        logging.info('输入注册时验证码: %s' % register_code)
        self.type(self.codeInput_value, register_code)
        logging.info('输入注册时的密码: %s' % register_password)
        self.type(self.pwdInput_value, register_password)
        logging.info('点击下一步')
        self.click(self.nextBtn_value)
        logging.info('选择商家')
        self.click(self.MerchantBtn_value)
        logging.info('点击下一步')
        self.click(self.nextBtn_value)
        logging.info('输入公司名称')
        self.type(self.companyNameInput_value, '自动化测试公司' + str(self.number))
        logging.info('输入门店名称')
        self.type(self.storeNameInput_value, '自动化测试门店' + str(self.number))
        logging.info('输入省市县地址')
        self.click(self.cityInput_value)
        logging.info('点击确认，默认选择第一个城市')
        self.click(self.cityConfirmBtn_value)
        logging.info('输入详细地址')
        self.type(self.addressInput_value, r'李洲全详细地址' + str(self.number))
        logging.info('点击下一步')
        self.click(self.nextBtn_value)
        logging.info('点击跳过引导按钮')
        self.click(self.skipBtn_value)

    def register_common_action(self, register_username, register_code, register_password):
        logging.info('进入注册页面')
        self.click(self.registeredBtn_value)
        logging.info('输入注册手机号: %s' % register_username)
        self.type(self.phoneNumInput_value, register_username)
        logging.info('输入注册时验证码: %s' % register_code)
        self.type(self.codeInput_value, register_code)
        logging.info('输入注册时的密码: %s' % register_password)
        self.type(self.pwdInput_value, register_password)
        logging.info('点击下一步')
        self.click(self.nextBtn_value)

    def check_register_success_status(self):
        logging.info('==检查注册后登录状态==')
        flag = self.is_exists(self.today_sales_value)
        return flag

    # 获取toast信息
    def check_register_fail_status(self):
        logging.info(r'检查状态开始')
        flag = self.is_exists(self.nextBtn_value)
        return flag

