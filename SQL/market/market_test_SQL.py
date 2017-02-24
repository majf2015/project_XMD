# -*- coding:UTF-8 -*-
import MySQLdb
import ConfigParser


class Mysqldb:
    def __init__(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/config.conf")
        self.debug = int(self.conf.get('Debug','debug'))
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(r"E:/project_XMD/SQL/market/market_test_data.conf")
        self.db = dict(self.conf.items('DB'))
        self.account = dict(self.conf.items('ManagerAccount'))
        self.coupon_data = dict(self.test_data.items('Coupon'))
        self.conn = MySQLdb.Connection\
        (host = self.db['host'], port = int(self.db['port']), user = self.db['user'], passwd = self.db['passwd'], db = self.db['db'])
        self.cursor = self.conn.cursor()
        self.result = {}

    def run_main(self):
        self.db_paid_coupon()

        self.write_to_test_data()
        self.cursor.close()
        self.conn.close()

    def db_paid_coupon(self):
        pass

    def write_to_test_data(self):
        self.test_data.write(open('E:/project_XMD/SQL/market/market_test_data.conf','w'))


db = Mysqldb()
db.run_main()