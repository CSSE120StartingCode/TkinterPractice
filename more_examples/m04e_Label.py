"""
Example showing for tkinter and ttk:
  -- ttk.Label
  -- ttk.Button
  -- ttk.Frame
  -- Associating a Button with a CALLBACK function

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk
import random


def main():
    # Root (main) window
    root = tkinter.Tk()
    root.title('Hello!')

    # Frames
    frame1 = ttk.Frame(root, padding=10, relief='raised')
    frame1.grid()

    frame2 = ttk.Frame(root)
    frame2.grid()

    # Label
    label = ttk.Label(frame1, text='This is a Label \n above a Button')
    label.grid()

    # Two buttons
    change_title_button = ttk.Button(frame2,
                                     text='Change the Title (above)')
    change_title_button.grid()
    change_title_button['command'] = lambda: change_title(root)

    quit_button = ttk.Button(frame2, text='Quit')
    quit_button.grid()
    quit_button['command'] = lambda: close_window(root)

    # Another Label, with its text set another way
    label2 = ttk.Label(frame2)
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

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
