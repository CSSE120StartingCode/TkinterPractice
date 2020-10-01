# TkinterPractice
Practicing with Tkinter for Graphical User Interfaces in Python

-----------------------------------BASICS------------------------------------------------ 
Python = is a Dynamically Typed, Object Oriented Programming Language
-----------------------------------------------------------------------------------------
Tkinter = Inbuilt Python module --> to create simple GUI apps
        = Standard Python interface to Tk GUI toolkit.
        
        Tkinter is the standard GUI library for Python. 
        Python when combined with Tkinter provides a fast and easy way to create GUI applications.

Tk = is the toolkit

mainloop() = Most important function while working with Tkinter. = You must call mainloop only one time. = It is an infinite loop.

-----------------------------BASIC Code for Tkinter----------------------------------

from tkinter import *
root = Tk()                          # 'root' is object of 'Tk' class 
                                     # creates a basic gui # basic default compoments present in GUI 
                                     # A base is created -> for GUI Development 
                                     # we can create button, menu bar,etc on this base

root.mainloop()                      # event loop -> called only once
-------------------------------------------------------------------------------------------
