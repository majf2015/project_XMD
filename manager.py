# -*- coding: utf-8 -*-
import os, time, threading, subprocess


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
        self.no_thread_run_time_sum = 0
        self.thread_all_run_time_sum = 0
        self.test_case_success = 0
        self.test_case_error = 0
        self.error_test_case = []

    def data(self):
        for root, dirs, files in os.walk(self.root):
            os.chdir(root)
            if len(files) != 0:
                for file in files:
                    file_name, file_type = os.path.splitext(file)
                    if file_type == '.py':
                        self.test_cases.append(Manager(root, file))
                    elif  file_type == '.log':
                        with open('run.log', 'ab') as file:
                            file.truncate()

    def test_case_log(self,**kwargs):
        string = '\n\n' + time.strftime( '%Y-%m-%d %X', time.localtime(time.time())) + '\n'
        for k, v in kwargs.iteritems():
            if type(v) == list:
                string +=  '%s : ' % k +'\n'
                for error_test_case in  v:
                    string +=' %s : %s ' % (error_test_case.root, error_test_case.file )+'\n'
            else:
                string +=  '%s : %s' % (k, v) +'\n'
        with open('run.log', 'ab') as file:
            file.write(string)

    def runlog(self):
        self.test_case_error = 0
        self.test_case_success = 0
        for test_case in self.test_cases:
            os.chdir(test_case.root)
            self.test_case_log(name = test_case.file,
                               run_time = test_case.run_time,
                               result = test_case.result)
            if test_case.result == '' or test_case.result == None  :
                self.test_case_error += 1
                self.error_test_case.append(test_case)
            else:
                self.test_case_success += 1
        os.chdir(self.root)
        self.test_case_log(thread_time = self.thread_all_run_time_sum,
                           success = self.test_case_success,
                           error = self.test_case_error,
                           error_test_cases = self.error_test_case)
                           #no_thread_time = self.no_thread_run_time_sum)

    def thread_all(self, test_cases):
        for test_case in test_cases:
            time_s = time.time()
            cmd = "python %s/%s" % (test_case.root, test_case.file)
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            test_case.result = result.stdout.read()
            time_e = time.time()
            test_case.run_time = time_e-time_s

    def run_thread_test_case(self):
        time_start = time.time()
        thread1 = threading.Thread(target=self.thread_all, args=(self.test_cases[: len(self.test_cases)/2],))
        thread1.start()
        thread2 = threading.Thread(target=self.thread_all, args=(self.test_cases[len(self.test_cases)/2 :],))
        thread2.start()
        thread1.join()
        thread2.join()
        time_end = time.time()
        self.thread_all_run_time_sum = time_end-time_start
        self.runlog()

    def nothread(self):
        for test_case in self.test_cases:
            time_s = time.time()
            cmd = "python %s/%s" % (test_case.root, test_case.file)
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            result.wait()
            test_case.result = result.stdout.read()
            time_e = time.time()
            test_case.run_time = time_e-time_s

    def run_no_thread_test_case(self):
        time_start1 = time.time()
        self.nothread()
        time_end1 = time.time()
        self.no_thread_run_time_sum = time_end1-time_start1
        self.runlog()


test = Run()
test.data()
test.run_thread_test_case()
#test.run_no_thread_test_case()

