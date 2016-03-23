import threading
import time

class Threa:
    def worker1(self, n):
        if n == 0:
            print "worker1"
        else:
            print "thread worker1"
        time.sleep(1)

    def worker2(self, n):
        if n == 0:
            print "worker2"
        else:
            print "thread worker2"
        time.sleep(1)

    def worker3(self, n):
        if n == 0:
            print "worker3"
        else:
            print "thread worker3"
        time.sleep(1)

    def worker4(self, n):
        if n == 0:
            print "worker4"
        else:
            print "thread worker4"
        time.sleep(1)

    def worker5(self, n):
        if n == 0:
            print "worker5"
        else:
            print "thread worker5"
        time.sleep(1)

    def thread1(self):
        self.worker1(1)
        self.worker2(1)
        self.worker3(1)

    def thread2(self):
        self.worker4(1)
        self.worker5(1)

    def thread_worker(self):
        ts = time.time()
        t0 = threading.Thread(target=self.thread1)
        t0.start()

        t1 = threading.Thread(target=self.thread2)
        t1.start()

        t0.join()
        t1.join()
        te = time.time()
        print "\nthread  run time: %.8f sec" % (te-ts)

    def no_thread_worker(self):
        ts = time.time()
        self.worker1(0)
        self.worker2(0)
        self.worker3(0)
        self.worker4(0)
        self.worker5(0)
        te = time.time()
        print "\nno thread  run time: %.8f sec" % (te-ts)

t = Threa()
t.thread_worker()
t.no_thread_worker()




