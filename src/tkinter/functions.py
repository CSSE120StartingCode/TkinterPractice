from tkinter import *

root = Tk()

def press():
	print("button pressed")
	label1 = Label(root,text="hurrah!! it worked")
	label1.pack()


def left(event):
	label = Label(root,text = "left press")
	label.pack()

def right(event):
	label = Label(root,text = "right press")
	label.pack()	


button1 = Button(root , text="button1" , command = press)
button2 = Button(root , text="button2")

button2.bind('<Button-1>' , left)
button2.bind('<Button-3>' , right)

button1.bind()

button1.pack()
button2.pack()

root.mainloop()