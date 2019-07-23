# -*- coding:utf-8 -*-
import configparser
import os


class Common(object):

    # 读取配置文件
    def read_config(configName):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + configName
        config.read(file_path)
        # config.read(file_path,encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误
        return config

    # 读取配置文件内容
    def get_content(config, type, typename):
        content = config.get(type, typename)
        return content
