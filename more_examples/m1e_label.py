"""
Example showing for tkinter and ttk:
  -- ttk.Label
  -- ttk.Button
  -- ttk.Frame
  -- Associating a Button with a CALLBACK function

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk
import random


def main():
    # Root (main) window
    root = tkinter.Tk()
    root.title('Hello!')
    root.geometry("300x200")

    # Frame
    frame1 = ttk.Frame(root)
    frame1.place(relx=0.1,rely=0.1,relheight=0.9,relwidth=0.9)

    # Label
    label = ttk.Label(frame1, text='This is a Label above a Button',anchor="nw",justify="center")
    label.place(relx=0.1,rely=0.02,relheight=0.1,relwidth=0.9)

    # Two buttons
    change_title_button = ttk.Button(frame1,
                                     text='Change the Title (above)')
    change_title_button.place(relx=0.1,rely=0.1,relheight=0.3,relwidth=0.7)
    change_title_button['command'] = lambda: change_title(root)

    quit_button = ttk.Button(frame1, text='Quit')
    quit_button.place(relx=0.2,rely=0.4,relheight=0.15,relwidth=0.4)
    quit_button['command'] = lambda: close_window(root)

    # Another Label, with its text set another way
    label2 = ttk.Label(frame1)
    label2['text'] = 'Later, we will put Labels BESIDE Buttons'
    label2.place(relx=0.1,rely=0.6,relheight=0.1,relwidth=0.7)

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
