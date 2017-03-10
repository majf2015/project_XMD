# -*- coding:UTF-8 -*-
import MySQLdb, ConfigParser, MySQLdb.cursors, os, sys



class Mysqldb:
    def __init__(self):
        self.current_path = sys.path[0]
        self.project_path = os.path.dirname(os.path.dirname(self.current_path))
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(os.path.join(self.project_path,'config.conf'))
        self.debug = int(self.conf.get('Debug','debug'))
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(os.path.join(self.project_path,'test_data\\tech\\tech_test_data.conf'))
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

    def write_to_test_data(self):
        self.test_data.set('Tech','tech',self.result['tech'])
        self.test_data.set('Tech','busy_tech',self.result['busy_tech'])
        self.test_data.set('Tech','free_tech',self.result['free_tech'])
        self.test_data.write(open(os.path.join(self.project_path,'test_data\\tech\\tech_test_data.conf'),'w'))


db = Mysqldb()
db.run_main()