import tkinter as tk

class Screen2():
    def __init__(self, cm):
        self.cm = cm

        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.window.title("Welcome win 2")
        self.window.geometry("480x320+%d+%d" % (self.cm.winx, self.cm.winy))

        frame = tk.Frame(self.window)
        frame.grid(row=0, column=0)

        label = tk.Label(frame, text="Screen Two!!!")
        label.grid(row=0, column=0)

        button = tk.Button(frame, text="Show screen 1", command=self.show1)
        button.grid(row=1, column=0)
        button = tk.Button(frame, text="End", command=self.btnend)
        button.grid(row=1, column=1)

        self.window.focus_set()
        self.window.mainloop()

    def close_window(self):
        self.cm.class_id = 0
        self.window.destroy()
        self.window = None

    def show1(self):
        self.cm.class_id = 1
        self.window.destroy()
        self.window = None

    def btnend(self):
        self.cm.class_id = 0
        self.window.destroy()
        self.window = None

