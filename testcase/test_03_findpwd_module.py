# coding = utf-8
from businessView.findPwdView import FindPwdView
from tools.startend import StartEnd
import logging


class FindPwdTest(StartEnd):

    # 修改密码成功
    def test_01_modify_pwdSuccess(self):
        '''
        修改密码成功
        '''
        logging.info(r'==修改密码成功用例==')
        find = FindPwdView()
        data0 = find.get_csv_data('../data/loginView.csv', 1)
        data1 = find.get_csv_data('../data/pwd.csv', 10)
        find.findpwd_action(data1[0], data1[1])
        find.modify_action(data1[2], data1[3])
        self.assertTrue(find.check_find_pwd_success_status())
        find.update_csv_data('../data/loginView.csv', 1, '正式账号', data0[2], data1[3])

    # 手机号为空找回密码
    def test_02_findpwd_phoneNumEmpty(self):
        '''
        找回密码手机号为空
        '''
        logging.info(r'==找回密码手机号为空用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 1)
        find.findpwd_action(data[0], data[1])
        self.assertTrue(find.check_find_pwd_fail_status())

    # 手机号格式错误找回密码
    def test_03_findpwd_phoneNumError(self):
        '''
        找回密码手机号格式错误
        '''
        logging.info(r'==找回密码手机号格式错误用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 2)
        find.findpwd_action(data[0], data[1])
        self.assertTrue(find.check_find_pwd_fail_status())

    # 未注册手机号找回密码
    def test_04_findpwd_phoneNumUnregistered(self):
        '''
        未注册手机号找回密码
        '''
        logging.info(r'==未注册手机号找回密码用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 3)
        find.findpwd_action(data[0], data[1])
        self.assertTrue(find.check_find_pwd_fail_status())

    # 验证码为空找回密码
    def test_05_findpwd_codeEmpty(self):
        '''
        验证码为空找回密码
        '''
        logging.info(r'==验证码为空找回密码用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 4)
        find.findpwd_action(data[0], data[1])
        self.assertTrue(find.check_find_pwd_fail_status())

    # 验证码错误
    def test_06_findpwd_codeError(self):
        '''
        验证码错误找回密码
        '''
        logging.info(r'==验证码错误找回密码用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 5)
        find.findpwd_action(data[0], data[1])
        self.assertTrue(find.check_find_pwd_fail_status())

    # 修改密码密码为空
    def test_07_modify_pwdEmpty(self):
        '''
        修改密码密码为空
        '''
        logging.info(r'==修改密码密码为空用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 6)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码不符合长度
    def test_08_modify_pwdNomatchLength(self):
        '''
        修改密码不符合长度
        '''
        logging.info(r'==修改密码不符合长度用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 7)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码不符合规则
    def test_09_modify_pwdNomatchRules(self):
        '''
        修改密码不符合规则
        '''
        logging.info(r'==修改密码不符合规则用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 8)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码前后输入不一致
    def test_10_modify_pwdInconsistent(self):
        '''
        修改密码前后不一致
        '''
        logging.info(r'==修改密码输入前后不一致用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 9)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码新旧密码重复
    def test_11_modify_pwdRepeat(self):
        '''
        新旧密码不一致
        '''
        logging.info(r'==修改密码新旧密码重复用例==')
        find = FindPwdView()
        data = find.get_csv_data('../data/pwd.csv', 11)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        self.assertTrue(find.check_modify_pwd_fail_status())

