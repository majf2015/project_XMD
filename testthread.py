import threading
import time


def worker(i):
    print "%d worker" % i
    time.sleep(1)


ts = time.time()
for i in range(3):
    t = threading.Thread(target=worker, args= (i,))
    t.start()
    #worker()

te = time.time()

print te-ts


