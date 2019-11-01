import threading
import queue
import time

class Producer(threading.Thread):
    def __init__(self, que, pool):
        threading.Thread.__init__(self)
        pool.append(self)
        self.que = que

    def run(self):
        num = 0
        while True:
            num = num + 1
            self.que.put("%i" % num)
            print("put: %i" % num)
            time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self, que, pool, flush_size = 5):
        threading.Thread.__init__(self)
        pool.append(self)
        self.que = que
        self.flush_size = flush_size

    def run(self):
        while True:
            size = que.qsize()
            print("queue size: %i"%size)
            if size >= self.flush_size:
                msgs = []
                for i in range(0, self.flush_size):
                    msg = self.que.get()
                    msgs.append(msg)
                print("flush %s" % " ".join(msgs))
            time.sleep(1)

if __name__ == "__main__":
    que = queue.Queue()
    threadPool = []
    producer = Producer(que, threadPool)
    consumer1 = Consumer(que, threadPool)
    consumer2 = Consumer(que, threadPool)
    
    for th in threadPool:
        th.start()
    