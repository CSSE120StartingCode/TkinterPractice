from tkinter import *


root = Tk()

class calculator:
	def __init__(self,master):
		self.master = master
		self.label1 = Label(master,text = "Enter first number")
		self.entry1 = Entry(master)
		self.label2 = Label(master, text = "Enter second number")
		self.entry2 = Entry(master)
		
		self.label1.grid(row=0,columnspan=2, sticky = E ,padx=10, pady=10)
		self.entry1.grid(row=0,column=2,columnspan=2,padx=10, pady=10)
		self.label2.grid(row=1,columnspan=2, sticky = E,padx=10, pady=10)
		self.entry2.grid(row=1,column=2,columnspan=2,padx=10, pady=10)

		self.plus = Button(master,text="Add" ,command = self.add)
		self.minus = Button(master,text="Subtract" , command = self.subtract)
		self.into = Button(master,text="Multiply" , command = self.multiply)
		self.div = Button(master,text="Divide" , command = self.divide)

		self.plus.grid(row=2,column=0,padx=10, pady=10)
		self.minus.grid(row=2,column=1,padx=10, pady=10)
		self.into.grid(row=2,column=2,padx=10, pady=10)
		self.div.grid(row=2,column=3,padx=10, pady=10)

		self.label = Label(master)
		self.label.grid(row=3,column=1,columnspan=2,padx=10,pady=10)

	def add(self):
		x = int(self.entry1.get())
		y = int(self.entry2.get())
		self.label.config(text = "Result of Addition:- " + str(x + y) )
	
	def subtract(self):
		x = int(self.entry1.get())
		y = int(self.entry2.get())
		self.label.config(text = "Result of Subtraction:- " + str(x - y) )

	def multiply(self):
		x = int(self.entry1.get())
		y = int(self.entry2.get())
		self.label.config(text = "Result of Multiplication:- " + str(x * y) )
		
	def divide(self):
		x = int(self.entry1.get())
		y = int(self.entry2.get())
		self.label.config(text = "Result of Division:- " + str(x / y) )				

root.title("Calculator")
root.minsize(width=300,height=200)

obj = calculator(root);

root.mainloop()