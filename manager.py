# -*- coding: utf-8 -*-
import os, time, threading
import log


class Manager():
    def __init__(self):
        self.root = 'E:/project_XMD/case'
        self.test_case_error = 0
        self.test_case_success = 0


    def run(self):
        for root, dirs, files in os.walk(self.root):
            os.chdir(root)
            if len(files) != 0:
                for file in files:
                    file_name, file_type = os.path.splitext(file)
                    if file_type == '.py':
                        self.sub_thread(file_name)
        print 'test_case_success : %d \n' % self.test_case_success
        print 'test_case_error : %d \n' % self.test_case_error


    def sub_thread(self, file_name):
            try:
                time_start = time.time()
                result = os.popen('python  %s' % file).read()
                time_end = time.time()
                log.mylog(file_name, result, time_end-time_start)
                if result == '':
                    self.test_case_error += 1
                else:
                    self.test_case_success += 1
                print "sub_thread"
            except :
                print "error"

    def thread(self):
        sub_thread =  threading.Thread(target=self.thread)
        sub_thread.start()



test = Manager()
test.run()
test.thread()

