# -*- coding:UTF-8 -*-
import MySQLdb
import global_attributes


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
        sql_update = "UPDATE `spa_lucky_wheel_record` set `status` = 0 WHERE club_id = '773358894821941248' and verify_code = '176567404992'"
        #sql_select = "SELECT * FROM `spa_user_act` WHERE act_id = '819732487256154112' and user_id = '745086393335681024'"
        try:
            cursor.execute(sql_update)
            conn.commit()
            result = cursor.fetchall()
            if self.debug :
                print cursor.rowcount
        except Exception as e:
            print e
            conn.rollback()

        cursor.close()
        conn.close()


db = Data()
db.test()