import tkinter as tk
from sub1 import Sub1

class Screen1():
    winsub = None

    def __init__(self, cm):
        self.cm = cm

        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.window.title("Welcome win 1")
        self.window.geometry("480x320+%d+%d" % (self.cm.winx, self.cm.winy))

        frame = tk.Frame(self.window)
        frame.grid(row=0, column=0)

        label = tk.Label(frame, text="Screen One!!!")
        label.grid(row=0, column=0)

        self.button1 = tk.Button(frame, text="Show screen 2", command=self.show2)
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(frame, text="Show sub 1", command=self.showsub1)
        self.button2.grid(row=1, column=1)
        self.button3 = tk.Button(frame, text="End", command=self.btnend)
        self.button3.grid(row=1, column=2)

        self.window.focus_set()
        self.window.mainloop()

    def show2(self):
        self.cm.class_id = 2
        self.cm.closesub = True

        if self.winsub is not None:
            self.winsub.destroy()
            self.winsub = None
        self.window.destroy()
        self.window = None

    def showsub1(self):
        if not self.cm.closesub:
            return

        if self.winsub is not None:
            self.winsub.destroy()
            self.winsub = None

        self.winsub = Sub1(self.cm)

    def close_window(self):
        if self.winsub is not None:
            self.winsub.destroy()
            self.winsub = None
        self.cm.class_id = 0
        self.cm.closesub = True
        self.window.destroy()
        self.window = None

    def btnend(self):
        if self.winsub is not None:
            self.winsub.destroy()
            self.winsub = None
        self.cm.class_id = 0
        self.cm.closesub = True
        self.window.destroy()
        self.window = None
