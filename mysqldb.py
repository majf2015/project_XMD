# -*- coding:UTF-8 -*-
import MySQLdb
import global_attributes


class Mysqldb:
    def __init__(self):
        self.db = global_attributes.db
        self.debug = global_attributes.debug
        self.coupon_data = global_attributes.coupon_data
        self.conn = MySQLdb.Connection\
        (host = self.db['host'], port = self.db['port'], user = self.db['user'], passwd = self.db['passwd'], db = self.db['db'])
        self.cursor = self.conn.cursor()

    def run_main(self):
        #self.db_verify_coupon()
        self.db_registered()

        self.cursor.close()
        self.conn.close()

    def db_verify_coupon(self):
        sql_update_coupon = "UPDATE `spa_user_act` SET can_use_sum = 1 , coupon_settled = 'N' " \
                     "WHERE club_id = %s "  % \
                     "and coupon_no in (%s, %s, %s, %s, %s, %s, %s)" % tuple(self.coupon_data.itervalues())
        try:
            self.cursor.execute(sql_update_coupon)
            self.conn.commit()
            result = self.cursor.fetchall()
            if self.debug :
                print self.cursor.rowcount
        except Exception as e:
            print e
            self.conn.rollback()

    def db_registered(self):
        sql_select_register = "SELECT count(*) from spa_user_club uc inner join  spa_user u on uc.user_id = u.id WHERE uc.club_id = '773358894821941248' "
        self.cursor.execute(sql_select_register)
        result = filter(str.isdigit,str(self.cursor.fetchall())) #str

db = Mysqldb()
db.run_main()