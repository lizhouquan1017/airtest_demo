from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import InvalidOperationException
from poco.exceptions import PocoNoSuchNodeException
from poco.exceptions import PocoTargetTimeout
from tools.conn import Database
import logging,csv


class BaseView(Database):

    # 初始化方法
    def __init__(self):
        self.poco = AndroidUiautomationPoco()
        super().__init__()

    # 点击方法
    def click(self, value):
        try:
            self.poco(value).click()
        except InvalidOperationException:
            logging.error('点击操作未完成！')

    # 无固定id元素点击
    def click_text(self, value):
        self.poco(text=value).click()

    # 获取元素方法
    def get_element(self, value):
        try:
            element = self.poco(value)
            return element
        except InvalidOperationException:
            logging.error('无法获取元素！')

    # 获取text属性值
    def get_text(self, value):
        try:
            text = self.poco(value).get_text()
            return text
        except PocoNoSuchNodeException:
            logging.error('无法获取元素属性！')

    # 判断元素是否存在
    def is_exists(self, value):
        try:
            flag = self.poco(value).exists()
            return flag
        except PocoNoSuchNodeException:
            logging.error('元素不存在！')

    # 滑动
    def swipe(self, value, flag):
        try:
            if flag == 'up':
                self.poco(value).swipe([0, -0.1])
                self.poco(value).swipe('up')
            elif flag == 'down':
                self.poco(value).swipe([0, -0.1])
                self.poco(value).swipe('down')
            elif flag == 'left':
                self.poco(value).swipe([-0.1, 0])
                self.poco(value).swipe('left')
            elif flag == 'right':
                self.poco(value).swipe([-0.1, 0])
                self.poco(value).swipe('right')
        except InvalidOperationException:
            logging.error('滑动操作未完成！')

    # 输入
    def type(self, value, text):
        try:
            self.poco(value).invalidate()
            self.poco(value).set_text(text)
        except InvalidOperationException:
            logging.error('输入操作未完成！')

    # 等待元素出现
    def wait_for_any(self, value):
        try:
            element = self.poco(text=value).wait_for_appearance()
            return element
        except PocoTargetTimeout:
            logging.error('元素超时未出现')

    # 获取元素坐标
    def get_element_pos(self, value):
        try:
            pos = self.poco(value).get_position()
            return pos
        except PocoNoSuchNodeException:
            logging.error(r'无法获取元素位子')

    # 从csv文件中获取数据
    def get_csv_data(self, csv_file, line):
        logging.info(r'获取输入数据')
        with open(csv_file, 'r', encoding='gbk') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    # 存数据导csv文件
    def save_csv_data(self, csv_file, datas):
        logging.info(r'存储数据到%s' % csv_file)
        with open(csv_file, 'w', encoding='gbk') as file:
            file.write(datas+'\n')
            logging.info(r'数据保存成功')

    # 更新数据导csv文件
    def update_csv_data(self, csv_file, index, flag, old, new):
        filereader = open(csv_file, 'r')
        rows = filereader.readlines()
        filewriter = open(csv_file, 'w')
        for line in rows:
            l = line.split(',')
            if l[index] == flag:
                filewriter.writelines(line.replace(old, new))
            else:
                filewriter.writelines(line)
        filewriter.close()
        filereader.close()

    # 数据库中查找数据
    def select_data_from_db(self, sql):
        self.connmysql()
        data = self.fetch_all(sql)
        self.close()
        return data
