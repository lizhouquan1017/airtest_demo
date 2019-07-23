# coding:utf-8
from businessView.loginView import LoginView
from tools.startend import StartEnd
import logging


class LoginTest(StartEnd):

    def test_01_user_login(self):
        '''
            正常登录用例
        '''
        logging.info('==正常账号成功登录用例==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 1)
        login.login_action(data[0], data[2])
        self.assertTrue(login.check_login_success_status())

    def test_02_user_login_pwderr(self):
        '''
            密码错误登录用例
        '''
        logging.info('==正确账号密码错误登录=')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 2)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

    def test_03_user_login_pwdempty(self):
        '''
           密码为空登录
        '''
        logging.info('==正常账号密码为空登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 3)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

    def test_04_user_login_phonenumerror(self):
        '''
            手机号为错误登录
        '''
        logging.info('==手机号格式错误登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 4)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

    def test_05_user_login_unregistered(self):
        '''
        未注册账号登录
        '''
        logging.info('==未注册账号登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 5)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

    def test_06_user_login_phonenumEmpty(self):
        '''
        手机号为空登录
        '''
        logging.info('==手机号为空登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 6)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

    def test_07_user_login_RestrictedAccounts(self):
        '''
        限制账号登录
        '''
        logging.info('==限制账号登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 7)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

    def test_08_user_login_DeactivatedAccount(self):
        '''
           停用账号登录
        '''
        logging.info('==停用账号登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 8)
        login.login_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

    def test_09_user_login_VerificationCode(self):
        '''
        验证码登录
        '''
        logging.info('==验证码登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 9)
        login.login_code_action(data[0], data[1])
        self.assertTrue(login.check_login_success_status())

    def test_10_user_login_ExperienceAccount(self):
        '''
        体验账号登录
        '''
        logging.info('==体验账号登录==')
        login = LoginView()
        login.login_experience_account_action()
        self.assertTrue(login.check_login_success_status())

    def test_11_user_login_VerificationCodeEmpty(self):
        '''
        验证码为空登录
        '''
        logging.info('==验证码为空登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 10)
        login.login_code_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

    def test_12_user_login_VerificationCodeError(self):
        '''
        验证码错误登录
        '''
        logging.info('==验证码错误登录==')
        login = LoginView()
        data = login.get_csv_data('../data/loginView.csv', 11)
        login.login_code_action(data[0], data[1])
        self.assertTrue(login.check_login_fail_status())

