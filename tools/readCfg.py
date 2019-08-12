# coding = utf-8

import configparser
from os import path


parent_path = path.dirname(path.dirname(__file__))
final_path = path.join(parent_path, "data\data.ini")


class ReadData(object):
    """ 读取cfg.ini文件，返回各个参数值构成的字典"""
    def __init__(self):
        self.cof = configparser.ConfigParser()
        self.cof.read(final_path, encoding='utf-8')

    """data.ini文件写入/修改操作"""
    def write_data(self, section, key, value):
        self.cof.set(section, key, value)
        self.cof.write(open(final_path, "w"))

    """读取data.ini文件的数据"""
    def get_data(self, section, key):
        data = self.cof.get(section, key)
        return data




