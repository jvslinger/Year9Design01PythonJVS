import tkinter as tk 
from tkinter import ttk

class Display:

	def __init__(self):

		self.value = ""

		self.root = tk.Tk() #create instance of Tk
		self.root.title("GUI Tabs Class")

		self.tabControl = ttk.Notebook(self.root)

		self.tab1 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab1, text = "Tab 1")

		self.tab2 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab2, text = "Tab 2")
		

		self.tabControl.pack(expand=1, fill="both")

		self.ent1t1 = tk.Entry(self.tab1)
		self.ent1t1.bind("<Return>", self.returnHit)
		self.ent1t1.pack()

		self.btn1t2 = tk.Button(self.tab2, text = "Button Tab 2")
		self.btn1t2.pack()


		self.root.mainloop()

	def returnHit(self):
		self.value = self.ent1t1.get();
		print (self.value)


display = Display()

