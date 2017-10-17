"""
Example showing for tkinter and ttk:
  -- How to CONSTRUCT and DISPLAY a WIDGET
       (in this case, a ttk.Button)

  -- How to associate a widget (here, a ttk.Button)
       with a CALLBACK function

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk
import random


def main():
    root = tkinter.Tk()
    root.title('Hello!')

    main_frame = ttk.Frame(root, padding=30, relief='raised')
    main_frame.grid()

    change_title_button = ttk.Button(main_frame,
                                     text='Change the Title (above)')
    change_title_button.grid()
    change_title_button['command'] = lambda: change_title(root)

    root.mainloop()


def change_title(root):
    # Make a new 8-letter title chosen randomly from 'A' to 'Z'.
    new_title = ''
    for k in range(8):  # @UnusedVariable
        new_title = new_title + chr(ord('A') + random.randrange(26))

    root.title(new_title)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
