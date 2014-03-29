#!/usr/bin/env python
#this script appends entry to a file called email but is not appending the entries to a pre existing file o desktop

import Tkinter
import tkMessageBox
import re

global entry 
entry = []

from Tkconstants import *

class myWindow:


    def __init__(self):

        self.mw = Tkinter.Tk()
        self.mw.option_add("*font", ("Arial", 15, "normal", ))
        self.mw.geometry("+5+5")
        self.mw.title("Guest Book")
        self.mw.bind(sequence = "<Control-q>", func = self.bindFunc)

        self.lab1 = Tkinter.Label(self.mw,
                                  text = 'Please sign in with your email address and hit "Return" .')
        self.lab1.pack(padx = 10, pady = 10)
        
        self.entr1 = Tkinter.Entry(self.mw)
        self.entr1.pack()
        self.entr1.bind(sequence = "<Return>", func = self.showEntry)
        self.entr1.focus()
        
        self.lab2 = Tkinter.Label(self.mw,
                                  text = 'Wait for green light on door to enter.')
        self.lab2.pack(side = RIGHT, pady = 20)

        self.mw.mainloop()

    def bindFunc(self, a):

        # self.mw.destroy() can't be called directly, because it can't
        # cope with the argument passed by ".bind()".

        self.mw.destroy()

    def showEntry(self, a):

        # Parameter "a" isn't used in this method, but it is needed,
        # to be able to deal with the argument passed by ".bind()".
        

        email = self.entr1.get()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.entr1.get()):
            print("error")
            tkMessageBox.showerror(title= "Input", message = "Not a valid email address::\n\n" + str(email) + "\n")
        else:
            print("Email address is valid") 
            entry.append(email)
            tkMessageBox.showinfo(title= "Input", message = "Thank you for signing the guest book:\n\n" + str(entry[-1]) + "\n")
            
#           dict(entry)
#           print("last entries: ", entry)
            
       	    text_file = open("TestConfig.txt", "a")
       	    text_file = open('/path/TestConfig.txt','a')
 #      	    
	    text_file.write(str(entry[-1]))
            text_file.write("\n")
            text_file.close()
            print ("Added " + str(entry[-1]) + " to the text file")
         


if __name__ == "__main__":
   app = myWindow()
   
   
