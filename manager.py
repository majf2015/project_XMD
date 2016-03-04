# -*- coding: utf-8 -*-
import os, time, threading
import log


class Manager():
    def __init__(self, root, file):
        self.root = root
        self.file = file
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
        for test_case in self.test_cases:
            file = test_case.get_file()
            os.chdir(test_case.get_root())
            time_start = time.time()
            test_case.set_result(os.popen('python  %s' % file).read())
            time_end = time.time()
            result = test_case.get_result()

            log.mylog(file, result, time_end-time_start)
            if result == '':
                self.test_case_error += 1
            else:
                self.test_case_success += 1
        print 'test_case_success : %d \n' % self.test_case_success
        print 'test_case_error : %d \n' % self.test_case_error


test = Run()
#thread = threading.Thread(target=test.run)
#thread.start()
test.run()

