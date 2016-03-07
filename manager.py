# -*- coding: utf-8 -*-
import os, time, threading
import log


class Manager():
    def __init__(self, root, file):
        self.root = root
        self.file = file
        self.run_time = 0.0
        self.result = "ready"


    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def set_file(self, file):
        self.file = file

    def get_file(self):
        return self.file

    def set_result(self, result):
        self.result = result

    def get_result(self):
        return self.result

    def set_run_time(self, time):
        self.run_time =  '%.8f sec' % time

    def get_run_time(self):
        return self.run_time

class Run():
    def __init__(self):
        self.root = 'E:/project_XMD/case'
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

    def run(self):
        self.data()
        def cmd(test_case, file):
            result = os.popen('python  %s' % file).read()
            test_case.set_result(result)
            print result
            print test_case.get_result()

        time_start = time.time()
        for test_case in self.test_cases:
            os.chdir(test_case.get_root())
            time_s = time.time()
            file = test_case.get_file()
            threading.Thread(target=cmd, args=(test_case, file)).start()
            time_e = time.time()
            test_case.set_run_time(time_e-time_s)
            result = test_case.get_result()
            if result == '':
                self.test_case_error += 1
            else:
                self.test_case_success += 1
            log.mylog(file, test_case.get_run_time(), result)
        time_end = time.time()
        print 'test_case_success : %d \n' % self.test_case_success
        print 'test_case_error : %d \n' % self.test_case_error
        print 'run_time_sum : %.8f sec' % (time_end-time_start)


test = Run()
test.run()

