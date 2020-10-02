"""
Example showing for tkinter and ttk:
  -- ttk.Label
  -- ttk.Button
  -- ttk.Frame
  -- Associating a Button with a CALLBACK function

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""


from tkinter import *
from tkinter import ttk
import random


def main():
    # Root (main) window
    """try to make smaller your code"""
    root = .Tk()
    root.title('Hello!')

    # Frame
    frame1 = Frame(root)
    frame1.grid()

    # Label
    label = Label(frame1, text='This is a Label above a Button')
    label.grid()

    # Two buttons
    change_title_button = Button(frame1,
                                     text='Change the Title (above)')
    change_title_button.grid()
    change_title_button['command'] = lambda: change_title(root)

    quit_button = Button(frame1, text='Quit')
    quit_button.grid()
    quit_button['command'] = lambda: close_window(root)

    # Another Label, with its text set another way
    label2 = Label(frame1)
    label2['text'] = 'Later, we will put Labels BESIDE Buttons'
    label2.grid()

    root.mainloop()


def change_title(root):
    # Make a new 8-letter title chosen randomly from 'A' to 'Z'.
    new_title = ''
    for k in range(8):  # @UnusedVariable
        new_title = new_title + chr(ord('A') + random.randrange(26))

    root.title(new_title)


def close_window(root):
    root.destroy()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
