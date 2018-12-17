import tkinter as tk
import os
from os import system

from tkinter import ttk as ttk

def submit():
	print("Honestly, knowing my coding skill, below this is an error message...")

	listName.append(output2.get())
	listDue.append(output3.get())
	listAmount.append(output4.get())
	#labelcal.config(text = "bleh"+star(average))
	print(listName)
	print(listDue)
	print(listAmount)

def remove():
	print("We're still figuring out how to clear a textbox.  Standby.  I mean you could always just like, delete this yourself though.")

	
listName = []
listDue = []
listAmount = []

#data will store the current row the you are entering the bill
data = [0]

root = tk.Tk()

root.config(background = "light blue")
root.title("PayYourBills™")

labInput1 = tk.Label(root, text = "Program Name", background = "gold", font = "Arial, 18")
labInput1.grid(row = 5, column = 1, columnspan = 2, sticky = "NESW")

labInput2 = tk.Label(root, text = "Bill Name: ")
labInput2.config(background = "navy", foreground = "white")
labInput2.grid(row = 0, column = 1, sticky = "NESW")

labInput3 = tk.Label(root, text = "Date Due: ")
labInput3.config(background = "navy", foreground = "white")
labInput3.grid(row = 1, column  = 1, sticky = "NESW")

labInput4 = tk.Label(root, text = "Amount: ")
labInput4.config(background = "navy", foreground = "white")
labInput4.grid(row = 2, column = 1, sticky = "NESW")

output2 = tk.Entry(root, width = 36, borderwidth = 1, relief = "solid")
output2.config(state = "normal")
output2.grid(row = 0, column = 2)

output3 = tk.Entry(root, width = 36, borderwidth = 1, relief = "solid")
output3.config(state = "normal")
output3.grid(row = 1, column = 2)

output4 = tk.Entry(root,width = 36, borderwidth = 1, relief = "solid")
output4.config(state = "normal")
output4.grid(row = 2, column = 2)

b = tk.Button(root, text = "Submit", command = submit)
b.config(state = "normal")
b.grid(row = 3, column = 2)

#stuff is below this

labInput5 = tk.Label(root, text = "Today's Date:  (01/01/19)", font = "Arial, 18")
labInput5.grid(row = 5, column = 3)

labInput8 = tk.Label(root, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
labInput8.config(background = "light blue", foreground = "white")
labInput8.grid(row = 6, column = 0, columnspan = 5)

labInput6 = tk.Label(root, text = "Bill Title", background = "light blue")
labInput6.grid(row = 7, column = 1)

labInput17 = tk.Label(root, text = "Amount Due", background = "light blue")
labInput17.grid(row = 7, column = 2)

labInput18 = tk.Label(root, text = "Date Due", background = "light blue")
labInput18.grid(row = 7, column = 3)

labInput19 = tk.Label(root, text = "Days Left to Complete")





#row 8

displayList = []

output3 = tk.Text(root, height=1, width = 18, borderwidth = 1, relief = "solid")
output3.grid(row = 8, column = 1)
displayList.append(output3)

output14 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output14.grid(row = 8, column = 2)

output23 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output23.grid(row = 8, column = 3)


#row 9

output4 = tk.Text(root, height=1, width = 18, borderwidth = 1, relief = "solid")
output4.grid(row = 9, column = 1)

output15 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output15.grid(row = 9, column = 2)

output24 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output24.grid(row = 9, column = 3)

#row 10

output5 = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output5.grid(row = 10, column = 1)

output16 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output16.grid(row = 10, column = 2)

output25 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output25.grid(row = 10, column = 3)

#row 11

output6 = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output6.grid(row = 11, column = 1)

output17 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output17.grid(row = 11, column = 2)

output26 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output26.grid(row = 11, column = 3)

#row 12

output7 = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output7.grid(row = 12, column = 1)

output18 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output18.grid(row = 12, column = 2)

output27 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output27.grid(row = 12, column = 3)

#row 13

output8 = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output8.grid(row = 13, column = 1)

output19 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output19.grid(row = 13, column = 2)

output28 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output28.grid(row = 13, column = 3)


#row 14

output9 = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output9.grid(row = 14, column = 1)

output20 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output20.grid(row = 14, column = 2)

output29 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output29.grid(row = 14, column = 3)


#row 15

output10 = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output10.grid(row = 15, column = 1)

output21 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output21.grid(row = 15, column = 2)

output30 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output30.grid(row = 15, column = 3)


#row 16

output11 = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output11.grid(row = 16, column = 1)

output22 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output22.grid(row = 16, column = 2)

output31 = tk.Text(root, height=1, width = 10, borderwidth = 1, relief = "solid")
output31.grid(row = 16, column = 3)

#labels

labInput7 = tk.Label(root, text = "Bill Number 1:", background = "light blue")
labInput7.grid(row = 8, column = 0)

labInput9 = tk.Label(root, text = "Bill Number 2:", background = "light blue")
labInput9.grid(row = 9, column = 0)

labInput10 = tk.Label(root, text = "Bill Number 3:", background = "light blue")
labInput10.grid(row = 10, column = 0)

labInput11 = tk.Label(root, text = "Bill Number 4:", background = "light blue")
labInput11.grid(row = 11, column = 0)

labInput12 = tk.Label(root, text = "Bill Number 5:", background = "light blue")
labInput12.grid(row = 12, column = 0)

labInput13 = tk.Label(root, text = "Bill Number 6:", background = "light blue")
labInput13.grid(row = 13, column = 0)

labInput14 = tk.Label(root, text = "Bill Number 7:", background = "light blue")
labInput14.grid(row = 14, column = 0)

labInput15 = tk.Label(root, text = "Bill Number 8:", background = "light blue")
labInput15.grid(row = 15, column = 0)

labInput16 = tk.Label(root, text = "Bill Number 9:", background = "light blue")
labInput16.grid(row = 16, column = 0)

#buttons

b2 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b2.config(state = "normal")
b2.grid(row = 8, column = 4)

b3 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b3.config(state = "normal")
b3.grid(row = 9, column = 4)

b4 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b4.config(state = "normal")
b4.grid(row = 10, column = 4)

b5 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b5.config(state = "normal")
b5.grid(row = 11, column = 4)

b6 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b6.config(state = "normal")
b6.grid(row = 12, column = 4)

b7 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b7.config(state = "normal")
b7.grid(row = 13, column = 4)

b8 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b8.config(state = "normal")
b8.grid(row = 14, column = 4)

b9 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b9.config(state = "normal")
b9.grid(row = 15, column = 4)

b10 = tk.Button(root, text = "Delete Task", command = remove, background = "light blue")
b10.config(state = "normal")
b10.grid(row = 16, column = 4)

root.mainloop()