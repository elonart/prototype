import tkinter as tk

class Sub1(tk.Toplevel):
    winsub = None

    def __init__(self, cm):
        tk.Toplevel.__init__(self)
        self.cm = cm
        self.cm.closesub = False

        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.title("Sub 1")
        self.geometry("640x480+%d+%d" % (self.cm.subwinx, self.cm.subwiny))

        frame = tk.Frame(self)
        frame.grid(row=0, column=0)

        label = tk.Label(frame, text="Sub One!!!")
        label.grid(row=0, column=0)

        button = tk.Button(frame, text="End", command=self.btnend)
        button.grid(row=1, column=0)

        self.focus_set()

    def close_window(self):
        self.cm.closesub = True
        self.destroy()
        self = None

    def btnend(self):
        self.cm.closesub = True
        self.destroy()
        self = None
