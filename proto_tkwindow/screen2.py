import tkinter as tk

class Screen2():
    def __init__(self, cm):
        self.cm = cm
        self.window2 = tk.Tk()
        self.window2.protocol("WM_DELETE_WINDOW", self.close_window)
        self.window2.title("Welcome win 2")
        self.window2.geometry("480x320+%d+%d" % (self.cm.winx, self.cm.winy))
        frame = tk.Frame(self.window2)
        frame.grid(row=0, column=0)

        label = tk.Label(frame, text="Page Two!!!")
        label.grid(row=0, column=0)

        button = tk.Button(frame, text="Button2", command=self.show2)
        button.grid(row=1, column=0)
        button = tk.Button(frame, text="End", command=self.show4)
        button.grid(row=1, column=1)

        self.window2.mainloop()
        self.window2 = None

    def close_window(self):
        self.cm.class_id = 0
        self.window2.destroy()

    def show2(self):
        self.cm.class_id = 1
        self.cm.winx = self.window2.winfo_x()
        self.cm.winy = self.window2.winfo_y()
        self.window2.destroy()

    def show4(self):
        self.cm.class_id = 0
        self.window2.destroy()

