# -*- coding: utf-8 -*-
import os, time, threading
import log


class Manager():
    def __init__(self, root, file):
        self.root = root
        self.file = file
        self.run_time = 0.0
        self.result = "ready"

    @property
    def root(self):
        return self.root

    @root.setter
    def root(self, root):
        self.root = root

    @property
    def file(self):
        return self.file

    @file.setter
    def file(self, file):
        self.file = file

    @property
    def result(self):
        return self.result

    @result.setter
    def result(self, result):
        self.result = result

    @property
    def run_time(self):
        return self.run_time

    @run_time.setter

    def run_time(self, time):
        self.run_time =  '%.8f sec' % time

class Run():
    def __init__(self):
        self.root = 'E:/project_XMD/testcase'
        self.test_cases = []
        self.test_case_error = 0
        self.test_case_success = 0

    def data(self):
        for root, dirs, files in os.walk(self.root):
            os.chdir(root)
            if len(files) != 0:
                for file in files:
                    file_name, file_type = os.path.splitext(file)
                    if file_type == '.py':
                        self.test_cases.append(Manager(root, file))

    def cmd(self,test_case, file):
            result = os.popen('python  %s' % file).read()
            test_case.result = result
            print result
            print test_case.result

    def run_test_case(self):
        self.data()
        time_start = time.time()
        for test_case in self.test_cases:
            os.chdir(test_case.root)
            time_s = time.time()
            file = test_case.file
            threading.Thread(target=self.cmd, args=(test_case, file)).start()
            time_e = time.time()
            test_case.run_time = time_e-time_s
            result = test_case.result
            if result == '':
                self.test_case_error += 1
            else:
                self.test_case_success += 1
            log.mylog(file, test_case.run_time, result)
        time_end = time.time()
        print 'test_case_success : %d \n' % self.test_case_success
        print 'test_case_error : %d \n' % self.test_case_error
        print 'run_time_sum : %.8f sec' % (time_end-time_start)


test = Run()
test.run_test_case()

