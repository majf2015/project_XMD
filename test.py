import threading
import time

class Threa:
    def worker1(self):
        print "worker1"
        time.sleep(1)

    def worker2(self):
        print "worker2"
        time.sleep(1)

    def worker3(self):
        print "worker3"
        time.sleep(1)

    def worker4(self):
        print "worker4"
        time.sleep(1)

    def worker5(self):
        print "worker5"
        time.sleep(1)

    def thread_worker(self):
        ts = time.time()
        for i in range(5):
            t = threading.Thread(target=self.worker1)
            t.start()
        te = time.time()
        print "\nthread worker run time: %.8f sec" % (te-ts)

    def no_thread_worker(self):
        ts = time.time()
        self.worker1()
        self.worker2()
        self.worker3()
        self.worker4()
        self.worker5()
        te = time.time()
        print "\nno thread worker run time: %.8f sec" % (te-ts)

t = Threa()
t.thread_worker()
t.no_thread_worker()



