# coding:utf-8
__author__ = "lzq"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import threading
import os
import yaml

yaml.warnings({'YAMLLoadWarning': False})
with open('../config/devices.yaml', 'r', encoding='gbk') as file:
    data = yaml.load(file)


def push_apk_to_devices(devicesname):
    packagename = data['package']
    apkpath = data['apkpath']
    try:
        install_thread = threading.Thread(target=app_install, args=(devicesname, apkpath, packagename,))
        # input_thread = threading.Thread(target=input_event, args=(devicesname,))
        install_thread.start()
        # input_thread.start()
        install_thread.join()
        # input_thread.join()
        return "Success"
    except Exception as e:
        return e
    pass


def app_install(devices, apkpath, package):
    """
    安装apk包
    :param devices:
    :param apkpath:
    :param package:
    :return:
    """
    try:
        if isinstalled(devices, package):
            uninstallcommand = "adb -s " + str(devices) + " uninstall " + package
            print("正在", devices, "上卸载", package)
            print("卸载结果：", os.system(uninstallcommand))
        installcommand = "adb -s " + str(devices) + " install -r " + apkpath
        os.popen(installcommand).read()
        print("正在", devices, "上安装", package)
        if isinstalled(devices, package):
            return "Install Success"
    except Exception as e:
        print(e)
        return "Install Fail"


# def input_event(devices):
#     # 获取andorid的poco代理对象，准备进行开启安装权限（例如各个品牌的自定义系统普遍要求的二次安装确认、vivo/oppo特别要求的输入手机账号密码等）的点击操作。
#     poco_android = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#     # 这里是针对不同机型进行不同控件的选取，需要用户根据自己的实际机型实际控件进行修改
#     n = 1
#     if devices == "127.0.0.1:62001":
#         count = 0
#         # 找n次或找到对象以后跳出，否则等5秒重试。
#         while True:
#             print(devices, "安装点击，循环第", count, "次")
#             if count >= n:
#                 break
#             if poco_android("vivo:id/vivo_adb_install_ok_button").exists():
#                 poco_android("vivo:id/vivo_adb_install_ok_button").click()
#                 break
#             else:
#                 time.sleep(5)
#             count += 1
#     elif devices == "127.0.0.1:62025":
#         count = 0
#         while True:
#             print(devices, "安装点击，循环第", count, "次")
#             if count >= n:
#                 break
#             if poco_android("com.android.packageinstaller:id/continue_button").exists():
#                 poco_android("com.android.packageinstaller:id/continue_button").click()
#             else:
#                 time.sleep(5)
#             count += 1


def isinstalled(devices, package):
    """
    判断是否安装apk包
    :param devices:
    :param package:
    :return:
    """
    command = "adb -s "+devices+" shell pm list packages"
    commandresult = os.popen(command)
    print("进入isinstalled方法，devices=", devices, "package=", package)
    for pkg in commandresult:
        if "package:"+package in pkg:
            print("在", devices, "上发现已安装：", package, "。")
            return True
    print("在", devices, "上没找到包：", package)
    return False


if __name__ == '__main__':
    push_apk_to_devices('CLB7N18403015180')
