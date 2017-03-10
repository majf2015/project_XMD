# -*- coding:UTF-8 -*-
import MySQLdb, ConfigParser, os, sys

class Mysqldb:
    def __init__(self):
        self.current_path = sys.path[0]
        self.project_path = os.path.dirname(os.path.dirname(self.current_path))
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(os.path.join(self.project_path,'config.conf'))
        self.debug = int(self.conf.get('Debug','debug'))
        self.test_data = ConfigParser.ConfigParser()
        self.test_data.read(os.path.join(self.project_path,'test_data\publicity\publicity_test_data.conf'))
        self.db = dict(self.conf.items('DB'))
        self.account = dict(self.conf.items('ManagerAccount'))
        self.conn = MySQLdb.Connection\
        (host = self.db['host'], port = int(self.db['port']), user = self.db['user'], passwd = self.db['passwd'], db = self.db['db'])
        self.cursor = self.conn.cursor()
        self.result = {}

    def run_main(self):
        self.write_to_test_data()
        self.cursor.close()
        self.conn.close()

    def write_to_test_data(self):
        self.test_data.write(open(os.path.join(self.project_path,'test_data\publicity\publicity_test_data.conf'),'w'))


db = Mysqldb()
db.run_main()