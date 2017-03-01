# -*- coding: utf-8 -*-
import sys,os, time, threading, subprocess,ConfigParser


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
        self.project_url = sys.path[0]
        self.root = os.path.join(self.project_url,'test_data')
        self.sql = []
        self.no_thread_run_time_sum = 0
        self.thread_all_run_time_sum = 0
        self.sql_success = 0
        self.sql_error = 0
        self.error_sql = []
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(os.path.join(self.project_url,'config.conf'))
        self.debug = int(self.conf.get('Debug','debug'))

    #收集项目中的sql文件，如果需要顺便清空日志文件
    def data(self):
        for root, dirs, files in os.walk(self.root):
            os.chdir(root)
            if len(files) != 0:
                for file in files:
                    file_name, file_type = os.path.splitext(file)
                    if file_type == '.py'and  file_name != '__init__':
                        self.sql.append(Manager(root, file))
                    #清空日志文件
                    elif self.debug and file_type == '.log':
                        with open('run.log', 'ab') as file:
                            file.truncate()

    #对测试用例执行结果进行整合，最后写入对应日志文件
    def sql_log(self,**kwargs):
        string = '\n\n' + time.strftime( '%Y-%m-%d %X', time.localtime(time.time())) + '\n'
        for k, v in kwargs.iteritems():
            if type(v) == list:
                string +=  '%s : ' % k +'\n'
                for error_sql in  v:
                    string +=' %s : %s ' % (error_sql.root, error_sql.file )+'\n'
            else:
                string +=  '%s : %s' % (k, v) +'\n'
        with open('run.log', 'ab') as file:
            file.write(string)

    #做一些简单的统计，把执行结果提交给对应方法进行整合
    def runlog(self):
        self.sql_error = 0
        self.sql_success = 0
        for sql in self.sql:
            os.chdir(sql.root)
            self.sql_log(name = sql.file,
                               run_time = sql.run_time,
                               result = sql.result)
            if sql.result == '' or sql.result == None  :
                self.sql_error += 1
                self.error_sql.append(sql)
            else:
                self.sql_success += 1
        #所有测试用例的执行成功与失败统计，日志文件在sql根目录下的run.log文件中
        os.chdir(self.root)
        self.sql_log(thread_time = self.thread_all_run_time_sum,
                           success = self.sql_success,
                           error = self.sql_error,
                           error_sql = self.error_sql)
                           #no_thread_time = self.no_thread_run_time_sum)

    #先将所有测试用例装入管道，设置一些需要的统计，获取结果参数，以便执行时取得对应的值
    def thread_all(self, sql):
        for sql in sql:
            time_s = time.time()
            cmd = "python %s/%s" % (sql.root, sql.file)
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            sql.result = result.stdout.read()
            time_e = time.time()
            sql.run_time = time_e-time_s

    #创建两个来分批执行测试用例，并将执行结果重新收集到管道中，计算整个项目测试用例执行时间
    def run_thread_sql(self):
        time_start = time.time()
        thread1 = threading.Thread(target=self.thread_all, args=(self.sql[: len(self.sql)/2],))
        thread1.start()
        thread2 = threading.Thread(target=self.thread_all, args=(self.sql[len(self.sql)/2 :],))
        thread2.start()
        thread1.join()
        thread2.join()
        time_end = time.time()
        self.thread_all_run_time_sum = time_end-time_start
        self.runlog()

    #以下代码是对比在执行测试用例时不使用线程同步批量执行所需要的执行时间
    '''def nothread(self):
        for sql in self.sql:
            time_s = time.time()
            cmd = "python %s/%s" % (sql.root, sql.file)
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            result.wait()
            sql.result = result.stdout.read()
            time_e = time.time()
            sql.run_time = time_e-time_s

    def run_no_thread_sql(self):
        time_start1 = time.time()
        self.nothread()
        time_end1 = time.time()
        self.no_thread_run_time_sum = time_end1-time_start1
        self.runlog()'''

    def write_to_test_data(self):
        self.conf.set('Url','project_url',self.project_url)
        self.conf.write(open(os.path.join(self.project_url,'test_data/config.conf','w')))

test = Run()
test.data()
test.run_thread_sql()
#test.run_no_thread_sql()

