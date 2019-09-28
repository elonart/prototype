from time import sleep
import tkinter as tk
import queue
from thread1 import Thread1

class Screen1():
    stopuiq = False
    thread1 = None

    def __init__(self, cm):
        self.cm = cm
        if self.cm.uique is None:
            self.cm.uique = queue.Queue()
        if self.cm.wkque is None:
            self.cm.wkque = queue.Queue()
        if self.cm.stque is None:
            self.cm.stque = queue.Queue()

        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.window.title("Welcome win 1")
        self.window.geometry("480x320+%d+%d" % (self.cm.winx, self.cm.winy))
        frame = tk.Frame(self.window)
        frame.grid(row=0, column=0)

        label = tk.Label(frame, text="Page One!!!")
        label.grid(row=0, column=0)

        button1 = tk.Button(frame, text="Button1", command=self.show1)
        button1.grid(row=1, column=0)
        button2 = tk.Button(frame, text="End", command=self.btnend)
        button2.grid(row=1, column=1)
        button3 = tk.Button(frame, text="Start Thread shutter", command=self.start_thread_shutter)
        button3.grid(row=2, column=0, padx=5)
        button4 = tk.Button(frame, text="Stop Thread", command=self.stop_thread)
        button4.grid(row=2, column=2, padx=5)

        self.window.after(100, self.ui_loop)

        self.window.mainloop()

    def close_window(self):
        self.cm.uique.put(('thread stop and pg end', 'xx2'))

    def start_thread_shutter(self):
        if self.thread1 is None or not self.thread1.is_alive():
            self.thread1 = Thread1(3, self.cm)
            self.thread1.start()

        self.cm.wkque.put(("shutter"))

    def stop_thread(self):
        if self.thread1 is not None and self.thread1.is_alive():
            print("will stop thread")
            self.cm.stque.put(('stop'))

    def ui_loop(self):
        if self.stopuiq:
            return

        try:
            method, val = self.cm.uique.get(0)
            if method == 'showmsg':
                print("msg: ", val)
                # process for UI thread

            elif method == 'thread stop and pg end':
                if self.thread1 is not None and self.thread1.is_alive():
                    # call all threads
                    self.cm.stque.put(('end'))
                else:
                    print("will stop screen #1-1 and ui loop")
                    self.cm.class_id = 0
                    self.stopuiq = True
                    self.window.destroy()
                    self.window = None
                    return

            elif method == 'pg end':
                print("will stop screen #1-2 and ui loop")
                self.cm.class_id = 0
                self.stopuiq = True
                self.window.destroy()
                self.window = None
                return
        except queue.Empty:
            pass

        self.window.after(100, self.ui_loop)

    def show1(self):
        if self.thread1 is not None and self.thread1.is_alive():
            # call all threads
            self.cm.stque.put(('stop'))

        self.cm.class_id = 2
        self.cm.winx = self.window.winfo_x()
        self.cm.winy = self.window.winfo_y()
        self.stopuiq = True
        self.window.destroy()
        self.window = None

    def btnend(self):
        self.cm.uique.put(('thread stop and pg end', 'xx'))
