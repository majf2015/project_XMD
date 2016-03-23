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
    def run_time(self, run_time):
        self.run_time =  '%.8f sec' % run_time

class Run():
    def __init__(self):
        self.root = 'E:/project_XMD/testcase'
        self.test_cases = []
        self.test_case_error = 0
        self.test_case_success = 0
        self.no_thread_run_time_sum = 0
        self.thread_all_run_time_sum = 0

    def data(self):
        for root, dirs, files in os.walk(self.root):
            os.chdir(root)
            if len(files) != 0:
                for file in files:
                    file_name, file_type = os.path.splitext(file)
                    if file_type == '.py':
                        self.test_cases.append(Manager(root, file))

    def runlog(self):
        for test_case in self.test_cases:
            os.chdir(test_case.root)
            log.mylog(test_case.file, test_case.run_time, test_case.result)
            if test_case.result == '':
                self.test_case_error += 1
            else:
                self.test_case_success += 1

            print test_case.root, test_case.file, test_case.run_time, test_case.result
        print 'test_case_success : %d \n' % self.test_case_success
        print 'test_case_error : %d \n' % self.test_case_error
        print 'no_thread_run_time_sum : %.8f sec' % self.no_thread_run_time_sum
        print 'thread_all_run_time_sum : %.8f sec' % self.thread_all_run_time_sum

    def thread_all(self, test_cases):
        for thread1_test_case in test_cases:
            time_s = time.time()
            result = os.popen('python  %s' % thread1_test_case.file)
            thread1_test_case.result = result.read()
            time_e = time.time()
            thread1_test_case.run_time = time_e-time_s
            print "thread_all_test_case : %s" % thread1_test_case.result

    def nothread(self):
        for test_case in self.test_cases:
            time_s = time.time()
            test_case.result = os.popen('python  %s' % test_case.file).read()
            time_e = time.time()
            test_case.run_time = time_e-time_s
            print "no_thread_test_case : %s" % test_case.result

    def run_test_case(self):
        self.data()
        time_start = time.time()
        thread1 = threading.Thread(target=self.thread_all, args=(self.test_cases[: len(self.test_cases)/2],))
        thread1.start()
        thread2 = threading.Thread(target=self.thread_all, args=(self.test_cases[len(self.test_cases)/2:],))
        thread2.start()
        thread1.join()
        thread2.join()
        time_end = time.time()
        self.thread_all_run_time_sum = time_end-time_start
        self.runlog()

        time_start1 = time.time()
        self.nothread()
        time_end1 = time.time()
        self.no_thread_run_time_sum = time_end1-time_start1
        self.runlog()





test = Run()
test.run_test_case()

