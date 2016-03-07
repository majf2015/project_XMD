import multiprocessing
import time

def worker(i):
    print "%d worker" % i
    time.sleep(1)

if __name__=='__main__':
    ts = time.time()
    for i in range(3):
        t = multiprocessing.Process(target=worker, args= (i,))
        t.start()
    #worker()
    te = time.time()
    print te-ts