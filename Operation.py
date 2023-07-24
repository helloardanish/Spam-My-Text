from pynput.keyboard import Key
import time
import random
from tkinter import *


class Operation:
    
    def autoType(self,keyControl,word,noOfTimes):
        for i in range(noOfTimes):
            if len(word)>=50:
                return False
            for i in word:
                if i==" ":
                    keyControl.press(' ')
                    time.sleep(0.009)
                    keyControl.release(' ')
                elif i == "\n":
                    keyControl.press(Key.enter)
                    time.sleep(0.011)
                    keyControl.release(Key.enter)
                else:
                    keyControl.press(i)
                    time.sleep(0.011)
                    keyControl.release(i)

        return True
