# -*- coding:UTF-8 -*-
import MySQLdb
import ConfigParser
import MySQLdb.cursors



class Mysqldb:
    def __init__(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/config.conf")
        self.debug = int(self.conf.get('Debug','debug'))
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(r"E:/project_XMD/test_data/home/home_test_data.conf")
        self.db = dict(self.conf.items('DB'))
        self.account = dict(self.conf.items('ManagerAccount'))
        self.coupon_data = dict(self.test_data.items('Coupon'))
        self.conn = MySQLdb.Connection\
        (host = self.db['host'], port = int(self.db['port']), user = self.db['user'], passwd = self.db['passwd'],
         db = self.db['db'], cursorclass = MySQLdb.cursors.DictCursor)
        self.cursor = self.conn.cursor()
        self.result = {}

    def run_main(self):

        self.db_tech()
        self.db_busy_tech()
        self.db_free_tech()
        self.db_verify_coupon()
        self.db_verify_order()
        self.db_verify_prize()
        self.db_bill_reminder()

        self.db_bill_reminder_first_record()

        self.write_to_test_data()
        self.cursor.close()
        self.conn.close()

    def db_tech(self):
        sql_select_tech = "SELECT count(*) FROM spa_user WHERE user_type = 'tech' and club_id =  %s "  \
                          %  self.account['clubid']
        self.cursor.execute(sql_select_tech)
        self.result['tech'] = filter(str.isdigit,str(self.cursor.fetchall())) #str
        if self.debug:
            print self.result['tech']
            print "db_tech"

    def db_busy_tech(self):
        sql_select_tech = "SELECT count(*) FROM spa_user WHERE user_type = 'tech' and status = 'busy' and club_id =  %s " \
                          %  self.account['clubid']
        self.cursor.execute(sql_select_tech)
        self.result['busy_tech'] = filter(str.isdigit,str(self.cursor.fetchall())) #str
        if self.debug:
            print self.result['busy_tech']
            print "db_busy_tech"

    def db_free_tech(self):
        sql_select_tech = "SELECT count(*) FROM spa_user WHERE user_type = 'tech' and " \
                          "status = 'free' and club_id =  %s " %  self.account['clubid']
        self.cursor.execute(sql_select_tech)
        self.result['free_tech'] = filter(str.isdigit,str(self.cursor.fetchall())) #str
        if self.debug:
            print "db_free_tech"

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
                           "and order_no = %s" % self.test_data.get('Verify','order')
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
                           "and verify_code = %s" % self.test_data.get('Verify','prize')
        try:
            self.cursor.execute(sql_update_prize)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        if self.debug:
            print "db_verify_prize"

    def db_bill_reminder(self):
        sql_update_bill = "UPDATE  spa_fast_pay_order SET status = 'paid' WHERE club_id =  %s " % self.account['clubid']
        try:
            self.cursor.execute(sql_update_bill)
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        if self.debug:
            print "db_bill_reminder"

    def db_bill_reminder_first_record(self):
        sql_first_record = "SELECT o.create_time, o.user_name, o.telephone, t.tech_name, t.tech_no, o.pay_amount " \
                           "FROM spa_fast_pay_order o ,spa_fast_order_tech_detail t WHERE t.order_id = o.id  " \
                           "AND o.club_id =  %s AND o.id = (SELECT MAX(id) FROM spa_fast_pay_order  " \
                           "WHERE club_id =  %s)" % (self.account['clubid'], self.account['clubid'])
        self.cursor.execute(sql_first_record)
        results = self.cursor.fetchall() #str
        self.result['bill_reminder_first_record'] = str(results[0]['create_time']) + ' '\
              + results[0]['user_name'] + ' '\
              + results[0]['telephone'] + ' '\
              + results[0]['tech_name'] + ' '\
              + '[' +results[0]['tech_no'] + ']' +  ' '\
              + '%0.2f' % (float(results[0]['pay_amount']) / 100) + ' '\
              + '确认' + ' '+ '异常'
        if self.debug:
            print "db_bill_reminder_first_record"

    def write_to_test_data(self):
        self.test_data.set('Tech','tech',self.result['tech'])
        self.test_data.set('Tech','busy_tech',self.result['busy_tech'])
        self.test_data.set('Tech','free_tech',self.result['free_tech'])
        self.test_data.set('Bill','bill_reminder_first_record',self.result['bill_reminder_first_record'])
        self.test_data.write(open('E:/project_XMD/test_data/home/home_test_data.conf','w'))


db = Mysqldb()
db.run_main()