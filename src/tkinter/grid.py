from tkinter import *

root = Tk()

username = Label(root,text = "Username")
password = Label(root,text = "Password")
entry1 = Entry(root)
entry2 = Entry(root)

username.grid(row=0,column=0 , sticky = E)
password.grid(row=1,column=0 , sticky = E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

check_button = Checkbutton(root,text = "Keep me logged in")
check_button.grid(columnspan=2)

root.mainloop()


