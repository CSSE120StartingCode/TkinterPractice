from tkinter import *
root= Tk();
root.title("Test App")
root.minsize(width=300,height=300)
root.maxsize(width=600,height =600)

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)


button1 = Button(topFrame,text = "button 1" , fg="red" , bg = "black")
button2 = Button(topFrame,text = "button 2" , fg="green" , bg = "black")
button3 = Button(topFrame,text = "button 3" , fg="blue" , bg = "black")
label = Label(bottomFrame,text = "hello world!" , fg = "red");
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
label.pack()

root.mainloop()