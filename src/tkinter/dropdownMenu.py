from tkinter import *
 
root = Tk()
root.title("Tk dropdown example")
 
 
label = Label(root, text="Choose a dish")
label.grid(row = 1, column = 1)


tkvar = StringVar(root)
choices = ['Pizza','Lasagne','Fries','Fish','Potatoe']
 
popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.grid(row = 2, column =1)


tkvar.set('Pizza') # set the default option

 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
 
# link function to change dropdown
tkvar.trace('w', change_dropdown)
 
root.mainloop()