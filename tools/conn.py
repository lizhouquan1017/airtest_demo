# coding:utf-8

import pymysql
import yaml

yaml.warnings({'YAMLLoadWarning': False})
with open('../config/db.yaml', 'r', encoding='gbk') as file:
    data = yaml.load(file)

    localhost = data['localhost']
    username = data['user']
    password = data['password']
    database = data['database']
    port = data['port']


class Database(object):

    def __init__(self):
        self._localhost = localhost
        self._username = username
        self._password = password
        self._database = database
        self._port = port
        self._conn = self.connmysql()
        if(self._conn):
            self._cursor = self._conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 连接数据库
    def connmysql(self):
        conn = False
        try:
            conn = pymysql.connect(host=self._localhost, user=self._username, password=self._password,
                                   database=self._database, port=self._port)
        except Exception:
            conn = False
        return conn

    # 获取查询结果
    def fetch_all(self, sql):
        res = ''
        if(self._conn):
            try:
                self._cursor.execute(sql)
                res =  self._cursor.fetchall()
            except Exception:
                res = False
        return res

    #  关闭数据库连接
    def close(self):
        if(self._conn):
            try:
                if(type(self._cursor)=='object'):
                    self._cursor.close()
                if(type(self._conn)=='object'):
                    self._conn.close()
            except Exception:
                pass

    # 执行sql文件
    def execute_sql_file(self):
        try:
            with open(u'../data/test.sql', 'r+') as f:
                sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
                sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]  # 将每段sql里的换行符改成空格
            ##执行sql语句，使用循环执行sql语句
            for sql_item in sql_list:
                if (self._conn):
                    try:
                        self._cursor.execute(sql_item)
                    except Exception as e:
                        print(e)
        except Exception as e1:
            print(e1)
        finally:
            self._cursor.close()
            self._conn.commit()
            self.close()


if __name__ == '__main__':
    d = Database()
    d.connmysql()
    d.execute_sql_file()
