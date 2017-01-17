# -*- coding: utf-8 -*-
import os, time, threading, subprocess,global_attributes


class Manager():
    def __init__(self, root, file):
        self.root = root
        self.file = file
        self.run_time = 0.0
        self.result = "ready"


    #把一些方法变成可读写属性来调用
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
        self.debug = global_attributes.debug

    #收集项目中的test_case文件，如果需要顺便清空日志文件
    def data(self):
        for root, dirs, files in os.walk(self.root):
            os.chdir(root)
            if len(files) != 0:
                for file in files:
                    file_name, file_type = os.path.splitext(file)
                    if file_type == '.py':
                        self.test_cases.append(Manager(root, file))
                    #清空日志文件
                    elif self.debug and file_type == '.log':
                        with open('run.log', 'ab') as file:
                            file.truncate()

    #对测试用例执行结果进行整合，最后写入对应日志文件
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

    #做一些简单的统计，把执行结果提交给对应方法进行整合
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
        #所有测试用例的执行成功与失败统计，日志文件在test_case根目录下的run.log文件中
        os.chdir(self.root)
        self.test_case_log(thread_time = self.thread_all_run_time_sum,
                           success = self.test_case_success,
                           error = self.test_case_error,
                           error_test_cases = self.error_test_case)
                           #no_thread_time = self.no_thread_run_time_sum)

    #先将所有测试用例装入管道，设置一些需要的统计，获取结果参数，以便执行时取得对应的值
    def thread_all(self, test_cases):
        for test_case in test_cases:
            time_s = time.time()
            cmd = "python %s/%s" % (test_case.root, test_case.file)
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            test_case.result = result.stdout.read()
            time_e = time.time()
            test_case.run_time = time_e-time_s

    #创建两个来分批执行测试用例，并将执行结果重新收集到管道中，计算整个项目测试用例执行时间
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

    #以下代码是对比在执行测试用例时不使用线程同步批量执行所需要的执行时间
    '''def nothread(self):
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
        self.runlog()'''


test = Run()
test.data()
test.run_thread_test_case()
#test.run_no_thread_test_case()

