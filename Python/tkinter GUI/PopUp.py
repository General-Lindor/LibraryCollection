import tkinter
from tkinter import ttk

import os
import re

def getPath(filename):
    base = os.path.abspath(__file__)
    base = re.split("\\\\", base)
    base.pop(len(base) - 1)
    result = ""
    for partialString in base:
        if partialString != "":
            result += partialString + "/"
    result += filename
    return result

class App(tkinter.Frame):
    def __init__(self, master, text, JaNein):
        
        #SETUP
        
        super().__init__(master)
        self.grid(row = 0, column = 0, padx = '5', pady = '5', sticky = 'nsw')
        self.root = master
        self.returnValue = False
        
        #FRAMES
        
        self.FrameTop = tkinter.Frame(self.root, bg = "black", width=1280, height=208, border = "0")
        self.FrameTop.grid(row = 0, column = 0, padx = '5', pady = '5', sticky = 'nsw')
        
        self.FrameBot = tkinter.Frame(self.root, bg = "black", width=1280, height=208, border = "0")
        self.FrameBot.grid(row = 1, column = 0, padx = '5', pady = '5', sticky = 'nsw')

        #IMAGES

        #self.buttonBlue = tkinter.PhotoImage(file = getPath("img/ButtonBlueMedium.png"))
        #self.buttonOrange = tkinter.PhotoImage(file = getPath("img/ButtonOrangeMedium.png"))
        self.buttonPurple = tkinter.PhotoImage(file = getPath("img/ButtonPurpleMedium.png"), master = self.FrameBot)
        #self.buttonRed = tkinter.PhotoImage(file = getPath("img/ButtonRedMedium.png"))
        #self.consoleTop = tkinter.PhotoImage(file = getPath("img/ConsoleTopNoNumbers.png"))
        #self.consoleBottom = tkinter.PhotoImage(file = getPath("img/ConsoleBottomNoNumbers.png"))
        #self.BorgCube = tkinter.PhotoImage(file = getPath("img/BorgCubeSmallNoBackground.png"))
        #self.Enterprise = tkinter.PhotoImage(file = getPath("img/ENT_350.png"))
        
        #LABEL
        
        self.Label = tkinter.Label(self.FrameTop, text = text, border = "0", bg = "black", fg = "white")
        self.Label.grid(row = 0, column = 0, padx = '5', pady = '5', sticky = 'nsw')
        
        #BUTTONS
        
        if JaNein:
            self.ButtonJa = tkinter.Button(self.FrameBot, text = "Ja", image = self.buttonPurple, compound = "center", command = self.returnJa, bg = "black", fg = "black", border = "0", activebackground = "black")
            self.ButtonJa.grid(row = 0, column = 0, padx = '5', pady = '5', sticky = 'nsw')
            self.ButtonNein = tkinter.Button(self.FrameBot, text = "Nein", image = self.buttonPurple, compound = "center", command = self.returnNein, bg = "black", fg = "black", border = "0", activebackground = "black")
            self.ButtonNein.grid(row = 0, column = 1, padx = '5', pady = '5', sticky = 'nsw')
        else:
            self.ButtonOK = tkinter.Button(self.FrameBot, text = "OK", image = self.buttonPurple, compound = "center", command = self.returnJa, bg = "black", fg = "black", border = "0", activebackground = "black")
            self.ButtonOK.grid(row = 0, column = 0, padx = '5', pady = '5', sticky = 'nsw')
        
        #DIMENSIONS
        
        self.FrameTop.update()
        self.FrameBot.update()
        self.root.geometry(str(max(self.FrameTop.winfo_width(), self.FrameBot.winfo_width()) + 10) + "x" + str(self.FrameTop.winfo_height() + self.FrameBot.winfo_height() + 20))
    
    def returnJa(self):
        self.returnValue = True
        self.root.destroy()
        self.root.quit()
    
    def returnNein(self):
        self.returnValue = False
        self.root.destroy()
        self.root.quit()

def makePopUp(text, JaNein, topLevel = True):
    root = None
    if topLevel:
        root = tkinter.Toplevel()
    else:
        root = tkinter.Tk()
    root.configure(background = "black")
    root.title("PopUp")
    root.resizable(height = False, width = False)
    root.grab_set()
    myapp = App(root, text, JaNein)
    root.mainloop()
    #print(myapp.returnValue)
    return myapp.returnValue

#SYNTAX BEI FRAGEN:
#makePopUp("Bist Du schön?", True)

#SYNTAX BEI AUSSAGEN:
#makePopUp("Du bist schön!", False)