# -*- coding:UTF-8 -*-

import MySQLdb
import global_attributes
import json

class Data:
    def __init__(self):
        self.host = '192.168.1.100'
        self.port = 3306
        self.user = 'spa'
        self.passwd = 'spa'
        self.db = 'spa'
        self.debug = global_attributes.debug

    def test(self):
        conn = MySQLdb.Connection\
            (host = self.host, port = self.port, user = self.user, passwd = self.passwd, db = self.db)
        cursor = conn.cursor()
        cursor.execute\
            ("""SELECT * FROM `spa_user_act` WHERE act_id = '819732487256154112' and user_id = '745086393335681024'""")
        result = cursor.fetchall()
        if self.debug :
            count = 0
            for i  in result:
                print json.dumps(i,encoding='UTF-8',ensure_ascii=False)
                count += 1
            print count


db = Data()
db.test()