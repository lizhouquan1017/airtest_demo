# coding:utf-8
import logging
from baseView.baseView import BaseView
from tools.common import Common


class FindPwdView(BaseView):

    config = Common.read_config('/page/findpwdView.ini')
    findPwd_value = Common.get_content(config, "找回密码按钮", "value")
    phonenumInput_value = Common.get_content(config, "电话输入框", "value")
    codeInput_value = Common.get_content(config, "验证码输入框", "value")
    nextBtn_value = Common.get_content(config, "下一步", "value")
    firstPwdInput_value = Common.get_content(config, "第一次密码输入", "value")
    secondPwdInput_value = Common.get_content(config, "第二次密码输入", "value")
    submitBtn_value = Common.get_content(config, "提交按钮", "value")
    loginBtn_value = Common.get_content(config, "登录按钮", "value")

    # 找回密码界面公共方法
    def findpwd_action(self, phonenum, code):
        logging.info(r'进入找回密码界面')
        self.click(self.findPwd_value)
        logging.info(r'找回密码操作开始')
        logging.info('找回密码账号: %s ' % phonenum)
        self.type(self.phonenumInput_value, phonenum)
        logging.info('输入验证码: %s' % code)
        self.type(self.codeInput_value, code)
        logging.info(r'点击下一步操作')
        self.click(self.nextBtn_value)

    # 修改密码界面公共方法
    def modify_action(self, first, second):
        logging.info(r'进入修改密码界面')
        logging.info(r'第一次输入密码: %s' % first)
        self.type(self.firstPwdInput_value, first)
        logging.info(r'第二次输入密码: %s' % second)
        self.type(self.secondPwdInput_value, second)
        logging.info(r'点击提交')
        self.click(self.submitBtn_value)

    # 找回密码成功状态检查
    def check_find_pwd_success_status(self):
        flag = self.is_exists(self.loginBtn_value)
        return flag

    # 进入修改界面错误状态检查
    def check_find_pwd_fail_status(self):
        flag = self.is_exists(self.nextBtn_value)
        return flag

    # 修改密码界面状态检查
    def check_modify_pwd_fail_status(self):
        flag = self.is_exists(self.submitBtn_value)
        return flag
