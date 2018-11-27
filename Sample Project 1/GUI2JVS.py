import tkinter as tk

from tkinter import ttk as ttk

root = tk.Tk()

def clicked(event):
	print("clicked")

output = tk.Text(root,height=20,width=40, borderwidth = 1, relief = "solid")
output.config(state="disabled")
output.grid(row = 0, column = 0, rowspan = 5)

labInput1 = tk.Label(root, text = "Program Name", background = "gold")
labInput1.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW")
labInput1.bind("<button-1>", clicked)

labInput2 = tk.Label(root, text = "Bill Name: ")
labInput2.grid(row = 0, column = 1, sticky = "NESW")

labInput3 = tk.Label(root, text = "Date Due: ")
labInput3.grid(row = 1, column  = 1)

labInput4 = tk.Label(root, text = "Amount: ")
labInput4.grid(row = 2, column = 1)

output = tk.Text(root,height = 1, width = 36, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 0, column = 2)

output = tk.Text(root,height = 1, width = 36, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 1, column = 2)

output = tk.Text(root,height = 1, width = 36, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 2, column = 2)

b = tk.Button(root, text = "Submit")
b.config(state = "normal")
b.grid(row = 3, column = 2)

labInput5 = tk.Label(root, text = "Today's Date:  (11/21/18)")
labInput5.grid(row = 5, column = 2)

labInput6 = tk.Label(root, text = "Do you have any *Buffalo* Bills?")
labInput6.grid(row = 6, column = 1)

output = tk.Text(root, height=1, width = 18, borderwidth = 1, relief = "solid")
output.grid(row = 7, column = 1)

output = tk.Text(root, height=1, width = 18, borderwidth = 1, relief = "solid")
output.grid(row = 8, column = 1)

output = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output.grid(row = 9, column = 1)

output = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output.grid(row = 10, column = 1)

output = tk.Text(root, height = 1, width = 18, borderwidth = 1, relief = "solid")
output.grid(row = 11, column = 1)

root.mainloop()
