import tkinter as tk
import math

def submit():
	print("Result Displayed on Interface")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+"units\nHeight:"+str(h)+"units\nThe Volume is:"+str(v)+"Units Cubed\n\n"

	output.delete(1.0,10000.0)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")


root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text = "Radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text = "Height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text = "Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()




root.mainloop()