import tkinter as tk
from compara import Compara
import screen1
import screen2

class App():
    def __init__(self):
        cm = Compara()
        sc1 = None
        sc2 = None
        while(True):
            if cm.class_id == 1:
                if sc1 is None:
                    sc2 = None
                    sc1 = screen1.Screen1(cm)
            elif cm.class_id == 2:
                if sc2 is None:
                    sc1 = None
                    sc2 = screen2.Screen2(cm)
            else:
                return


if __name__ == '__main__':
    s = App()
