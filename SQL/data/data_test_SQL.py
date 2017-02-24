# -*- coding:UTF-8 -*-
import MySQLdb
import ConfigParser


class Mysqldb:
    def __init__(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(r"E:/project_XMD/config.conf")
        self.debug = int(self.conf.get('Debug','debug'))
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(r"E:/project_XMD/SQL/data/data_test_data.conf")
        self.db = dict(self.conf.items('DB'))
        self.account = dict(self.conf.items('ManagerAccount'))
        self.conn = MySQLdb.Connection\
        (host = self.db['host'], port = int(self.db['port']), user = self.db['user'], passwd = self.db['passwd'], db = self.db['db'])
        self.cursor = self.conn.cursor()
        self.result = {}

    def run_main(self):
        self.db_registered()
        self.db_phone_registered()

        self.write_to_test_data()
        self.cursor.close()
        self.conn.close()


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
        self.test_data.set('DataAnalysis','register',self.result['register'])
        self.test_data.set('DataAnalysis','phone_register',self.result['phone_register'])
        self.test_data.write(open('E:/project_XMD/SQL/data/data_test_data.conf','w'))


db = Mysqldb()
db.run_main()