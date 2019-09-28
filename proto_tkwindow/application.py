import tkinter as tk
from compara import Compara
import screen1
import screen2

class App():
    def __init__(self):
        cm = Compara()
        while(True):
            if cm.class_id == 1:
                sc1 = screen1.Screen1(cm)
                sc1 = None
            elif cm.class_id == 2:
                sc2 = screen2.Screen2(cm)
                sc2 = None
            else:
                return


if __name__ == '__main__':
    s = App()
