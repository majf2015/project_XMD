# -*- coding:UTF-8 -*-
import MySQLdb
import ConfigParser


class Mysqldb:
    def __init__(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"test_data.conf")
        self.debug = self.conf.get('Debug','debug')
        self.db = dict(self.conf.items('DB'))
        self.account = dict(self.conf.items('ManagerAccount'))
        self.coupon_data = dict(self.conf.items('Coupon'))
        self.conn = MySQLdb.Connection\
        (host = self.db['host'], port = int(self.db['port']), user = self.db['user'], passwd = self.db['passwd'], db = self.db['db'])
        self.cursor = self.conn.cursor()
        self.result = {}

    def run_main(self):
        self.db_verify_coupon()
        self.db_registered()
        self.write_to_test_data()

        self.cursor.close()
        self.conn.close()

    def db_verify_coupon(self):
        sql_update_coupon = "UPDATE `spa_user_act` SET can_use_sum = 1 , coupon_settled = 'N' " \
                     "WHERE club_id = %s "  %  self.account['clubid'] + \
                    "and coupon_no in (%s, %s, %s, %s, %s, %s, %s)" % tuple(self.coupon_data.itervalues())
        try:
            self.cursor.execute(sql_update_coupon)
            self.conn.commit()
            if self.debug:
                print self.cursor.rowcount
        except Exception as e:
            print e
            self.conn.rollback()

    def db_registered(self):
        sql_select_register = "SELECT count(*) from spa_user_club uc inner join  spa_user u on uc.user_id = u.id WHERE uc.club_id = '773358894821941248' "
        self.cursor.execute(sql_select_register)
        self.result['register'] = filter(str.isdigit,str(self.cursor.fetchall())) #str

    def write_to_test_data(self):
        self.conf.set('DataAnalysis','register',self.result['register'])
        self.conf.write(open('test_data.conf','w'))


db = Mysqldb()
db.run_main()