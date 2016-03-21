import threading
import time

class Threa:
    def worker(self,i):
        print "%d worker" % i
        time.sleep(1)

    def thread_worker(self,i):
        t = threading.Thread(target=self.worker, args= (i,))
        t.start()
        return t
    def no_thread_worker(self,i):
        self.worker(i)

t = Threa()
ts1 = time.time()
tjoin = []
for i in range(5):
    tjoin.append(t.thread_worker(i))

for j in tjoin:
    j.join()
te1 = time.time()
print "\nthread worker run time: %.8f sec" % (te1-ts1)

ts2 = time.time()
for i in range(5):
    t.no_thread_worker(i+10)
te2 = time.time()
print "\nno thread worker run time: %.8f sec" % (te2-ts2)


