import pymysql as pymysql
from dbutils.pooled_db import PooledDB


class MysqlPool(object):
    """
    mysql 连接池
    使用时进行with操作
    with MysqlPool() as db:
        ......
        ......
    """

    def __init__(self):
        self.host = ''
        self.port = 3306
        self.admin = ''
        self.password = ''
        self.database = ''
        self.charset = 'utf8'
        self.configs = {
            'creator': pymysql,
            'host': self.host,
            'port': self.port,
            'user': self.admin,
            'password': self.password,
            'db': self.database,
            'charset': self.charset,
            'maxconnections': 0,
            'blocking': True,
            'ping': 7,
            'cursorclass': pymysql.cursors.DictCursor
        }
        self.pool = PooledDB(**self.configs)

    def __enter__(self):
        self.coon = self.pool.connection()
        self.cursor = self.coon.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.coon.close()
