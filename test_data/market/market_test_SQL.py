# -*- coding:UTF-8 -*-
import MySQLdb,ConfigParser, os, sys


class Mysqldb:
    def __init__(self):
        self.current_path = sys.path[0]
        self.project_path = os.path.dirname(os.path.dirname(self.current_path))
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(os.path.join(self.project_path,'config.conf'))
        self.debug = int(self.conf.get('Debug','debug'))
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(os.path.join(self.project_path,'test_data\market\market_test_data.conf'))
        self.db = dict(self.conf.items('DB'))
        self.account = dict(self.conf.items('ManagerAccount'))
        self.coupon_data = dict(self.test_data.items('Coupon'))
        self.conn = MySQLdb.Connection\
        (host = self.db['host'], port = int(self.db['port']), user = self.db['user'], passwd = self.db['passwd'], db = self.db['db'])
        self.cursor = self.conn.cursor()
        self.result = {}

    def run_main(self):
        self.db_paid_coupon()
        self.db_coupon()
        self.db_lucky_wheel()

        self.write_to_test_data()
        self.cursor.close()
        self.conn.close()

    def db_paid_coupon(self):
        sql_delete_paid_coupon = "DELETE FROM spa_preferential_activities WHERE  coupon_type = 'paid' " \
                           "and act_value = '50' and club_id =  %s " % self.account['clubid']
        try:
            self.cursor.execute(sql_delete_paid_coupon)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        if self.debug:
            print "db_paid_coupon"

    def db_coupon(self):
        sql_delete_coupon = "DELETE FROM spa_preferential_activities WHERE  coupon_type = 'redpack' " \
                           "and act_value = '118' and club_id =  %s " % self.account['clubid']
        try:
            self.cursor.execute(sql_delete_coupon)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        if self.debug:
            print "db_coupon"

    def db_lucky_wheel(self):
        sql_update_lucky_wheel = "UPDATE `spa_lucky_wheel_activity` set `status` = '2' WHERE  club_id = %s " \
                                 % self.account['clubid']
        try:
            self.cursor.execute(sql_update_lucky_wheel)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        if self.debug:
            print "db_lucky_wheel"

    def write_to_test_data(self):
        self.test_data.write(open(os.path.join(self.project_path,'test_data\market\market_test_data.conf'),'w'))



db = Mysqldb()
db.run_main()