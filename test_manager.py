# -*- coding: utf-8 -*-
import os, unittest, time
import log


class Test_Manager(unittest.TestCase):
    def setUp(self):
        self.test_case_sum = 0


    def test_run(self):
        for root, dirs, files in os.walk('E:/test_project_XMD/test_case'):
            os.chdir(root)
            if len(files) != 0:
                for file in files:
                    file_name, file_type = os.path.splitext(file)
                    if file_type == '.py':
                        result = os.popen('python  %s' % file).read()

                        log.mylog(file_name, result)
                        #log.log(file_name)
                        self.test_case_sum += 1
        print 'test_case_sum : %d \n' % self.test_case_sum

