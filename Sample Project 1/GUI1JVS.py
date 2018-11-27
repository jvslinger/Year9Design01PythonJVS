#This opens the tkinter "tool box" containing all support material to make GUI Elements
#By including as tk we are giving a short name to use.

import tkinter as tk

#Main Window

root = tk.Tk() #creates the window

#Three stages to build elements
#1. Construct the Object: Building and Configuring it
#2. Configure the Object: Specify behaviors and settings
#3. Pack the Object: Put it in the window
output = tk.Text(root,height=10,width=30) #Parameters are what we send in.
#ordered parameters: The order we send them matters.  (This is the common one, most languages ordered parameters matter)
#named parameters: JavaScript and Python specific.
output.config(state = "disabled",background = "orange")
output.grid(row = 0, column  = 0, rowspan = 5)

#******WIDGETS 2,3,4******

labInput1 = tk.Label(root,text = "Input 1",background = "red")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root,text = "Input 2",background = "white")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root,text = "Input 3",background = "blue")
labInput3.grid(row = 7, column = 0)

#******WIDGETS 5,6 (Checkboxes)******

var1=tk.IntVar()
var2=tk.IntVar()

cHC = tk.Checkbutton(root, text="Expand", variable=var1)
cHC.grid(row = 0, column = 1)

cLF = tk.Checkbutton(root, text="Expand", variable=var2)
cLF.grid(row = 1, column = 1)

#This is an event drive program
#Build the GUI
#Start it running
#Wait for "event"
root.mainloop() #starts the program



