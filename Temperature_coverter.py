from tkinter import *

root=Tk()
root.geometry("400x600")
root.title("Temperature converter")

def convert():
	c2f=int(e1.get())
	x=int(c2f*(9/5)+32)
	e3.insert(0,x)




label1=Label(root, text="Celcius")
label1.grid(row=1, column=0)
e1=Entry(root)
e1.grid(row=2, column=0)

label2=Label(root, text="Temperature Converter")
label2.grid(row=0, column=2)

label3=Label(root, text="Fahrenheit")
label3.grid(row=1, column=3)
e3=Entry(root)
e3.grid(row=2, column=3)

b1=Button(root, text="Convert", command = convert)
b1.grid(row=2,column=2)



mainloop()