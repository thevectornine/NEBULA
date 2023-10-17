
import win32com.client as comclt
import time
import string
import random
import easygui
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
import time






desk = GetDC(0)
s = string
s.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

wsh = comclt.Dispatch("WScript.Shell")



def payloads():

    for i in range (5):

        #payload1
        for i in range(100):
            wsh.SendKeys(random.choice(s.ascii_letters))
            print(random.choice(s.ascii_letters))
            time.sleep(0.05)
            
            PatBlt(desk, 0, 0, 1500, 1000, PATINVERT)
            
        
        #run notepad then type nebula 10 times
        wsh.run("Notepad.exe")
        for i in range(10):
            wsh.SendKeys("nebula")
            print(random.choice(s.ascii_letters))
            time.sleep(1)
            
            

        #make bouncing square
        desk = GetDC(0)
        x = 0
        xv = 10
        y = 0
        yv = 10
        x_2 = 200
        y_2 = 200
        for i in range(2000):
            PatBlt(desk, x, y, x_2, y_2, PATINVERT)
                #time.sleep(0.01)
                #PatBlt(desk, x, y, x_2, y_2, PATINVERT)
            x += xv
            y += yv 

            if y > 800:
                yv = -10
            if x > 1500:
                xv = -10
            if  y < 0:
                yv = 10
            if x < 0:
                xv = 10
    
    #for i in range(10):
    #    wsh.Run ('Notepad.exe')
    #    time.sleep(1)
    for i in range (10):
        PatBlt(desk, 0, 0, 1500, 1000, PATINVERT)
        time.sleep(1)
    

    

 
if easygui.ynbox("abbccda is a program that is really annoying, do you want to run?" , "warning"):
    #wsh.run("Notepad.exe")
    t=open("open_me.txt", "w")
    t.write("your computer is being controlled by Nebula, you ran docile version, so enjoy ;)")
    payloads()


    




#payloads()
