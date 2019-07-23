# coding:utf-8

import pymysql, yaml

yaml.warnings({'YAMLLoadWarning': False})
with open('../config/db.yaml', 'r', encoding='gbk') as file:
    data = yaml.load(file)

    localhost = data['localhost']
    username = data['user']
    password = data['password']
    database = data['database']


class Database(object):

    def __init__(self):
        self._localhost = localhost
        self._username = username
        self._password = password
        self._database = database
        self._conn = self.connmysql()
        if(self._conn):
            self._cursor = self._conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 连接数据库
    def connmysql(self):
        conn = False
        try:
            conn = pymysql.connect(host=self._localhost,user=self._username,password=self._password,database=self._database)
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


if __name__ == '__main__':
    # with open('../config/db.yaml', 'r', encoding='gbk') as file:
    #     data = yaml.load(file)
    #
    #     localhost = data['localhost']
    #     username = data['user']
    #     password = data['password']
    #     database = data['database']
    d = Database()
    d.connmysql()
    res = d.fetch_all('SELECT * from jxc_t_user where phone_num = 15927169432')
    d.close()
    print(res[0][r'id'])
