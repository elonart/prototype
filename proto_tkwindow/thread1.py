from threading import Thread
import time
import queue

class Thread1(Thread):
    def __init__(self, sleep_time, cm):
        Thread.__init__(self)
        self.sleep_time = sleep_time
        self.cm = cm

    def run(self):
        working = True
        while(working):
            try:
                method = self.cm.wkque.get(0)
                if method == "shutter":
                    print("method in thread1:", method)
                    time.sleep(self.sleep_time)
                    self.cm.uique.put(('showmsg', "recieve shutter"))
            except queue.Empty:
                pass

            try:
                method = self.cm.stque.get(0)
                if method == "stop":
                    print("will stop thread1")
                    working = False
                elif method == "end":
                    print("will stop thread1")
                    self.cm.uique.put(('pg end', "end"))
                    working = False
            except queue.Empty:
                pass
