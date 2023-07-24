import Operation as Op
import View as vw
from pynput.keyboard import Controller
import tkinter as tk

class Main:
    def __init__(self):
        print("Object created")


keyboardController = Controller()
root = tk.Tk()
root.title("Spam My Text")
app = vw.View(root,keyboardController)
root.mainloop()
#op = Op.Operation()
#op.autoType("hello check",keyboard)
