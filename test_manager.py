# -*- coding: utf-8 -*-
import os, unittest, time
import log


class Test_Manager(unittest.TestCase):
    def setUp(self):
        self.root = 'E:/test_project_XMD/test_case'
        self.test_case_error = 0
        self.test_case_success = 0
        self.result = ''
        self.run_time = 0


    def test_run(self):
        for root, dirs, files in os.walk(self.root):
            os.chdir(root)
            if len(files) != 0:
                for file in files:
                    file_name, file_type = os.path.splitext(file)
                    if file_type == '.py':
                        try:
                            time_start = time.time()
                            self.result = os.popen('python  %s' % file).read()
                            time_end = time.time()
                            self.run_time = time_end - time_start

                            if self.result == '':
                                self.test_case_success += 1
                            else:
                                self.test_case_error += 1

                        except IOError,e:
                            pass

                        log.mylog(file_name, self.result, self.run_time)
        print 'self.test_case_success : %d \n' % self.test_case_success
        print 'self.test_case_error : %d \n' % self.test_case_error

