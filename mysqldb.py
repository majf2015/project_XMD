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
        self.db_tech()
        self.db_verify_coupon()
        self.db_verify_order()
        self.db_registered()
        self.db_phone_registered()

        self.write_to_test_data()
        self.cursor.close()
        self.conn.close()

    def db_tech(self):
        sql_select_tech = "SELECT count(*) FROM spa_user WHERE user_type = 'tech' and club_id =  %s "  %  self.account['clubid']
        self.cursor.execute(sql_select_tech)
        self.result['tech'] = filter(str.isdigit,str(self.cursor.fetchall())) #str
        if self.debug:
            print "db_tech"

    def db_verify_coupon(self):
        sql_update_coupon = "UPDATE `spa_user_act` SET can_use_sum = 1 , coupon_settled = 'N' " \
                     "WHERE club_id = %s "  %  self.account['clubid'] + \
                    "and coupon_no in (%s, %s, %s, %s, %s, %s, %s)" % tuple(self.coupon_data.itervalues())
        try:
            self.cursor.execute(sql_update_coupon)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        if self.debug:
            print "db_verify_coupon"

    def db_verify_order(self):
        sql_update_order = "UPDATE `spa_order` set `status` = 'accept' WHERE club_id = %s " % self.account['clubid'] + \
                           "and order_no = %s" % self.conf.get('Verify','order')
        try:
            self.cursor.execute(sql_update_order)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        if self.debug:
            print "db_verify_order"

    def db_verify_prize(self):
        sql_update_prize = "UPDATE `spa_lucky_wheel_record` set `status` = 0  " \
                           "WHERE club_id = %s " % self.account['clubid'] + \
                           "and verify_code = %s" % self.conf.get('Verify','prize')
        try:
            self.cursor.execute(sql_update_prize)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        if self.debug:
            print "db_verify_order"

    def db_registered(self):
        sql_select_register = "SELECT count(*) from spa_user_club uc inner join  spa_user u on uc.user_id = u.id " \
                              "WHERE uc.club_id = %s "  %  self.account['clubid']
        self.cursor.execute(sql_select_register)
        self.result['register'] = filter(str.isdigit,str(self.cursor.fetchall())) #str
        if self.debug:
            print "db_registered"

    def db_phone_registered(self):
        sql_select_phone_register = "SELECT count(*) from spa_user_club uc inner join  spa_user u on uc.user_id = u.id " \
                                    "WHERE uc.club_id =  %s "  %  self.account['clubid'] + \
                                    "and (u.user_type='user' " \
                                    "or (u.user_type='weixin' and (u.phone_num is null or u.phone_num = '')))"
        self.cursor.execute(sql_select_phone_register)
        self.result['phone_register'] = filter(str.isdigit,str(self.cursor.fetchall())) #str
        if self.debug:
            print "db_phone_registered"

    def write_to_test_data(self):
        self.conf.set('Tech','tech',self.result['tech'])
        self.conf.set('DataAnalysis','register',self.result['register'])
        self.conf.set('DataAnalysis','phone_register',self.result['phone_register'])
        self.conf.write(open('test_data.conf','w'))


db = Mysqldb()
db.run_main()