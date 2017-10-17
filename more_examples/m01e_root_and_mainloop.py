"""
Example showing for tkinter and ttk:
  -- tkinter.Tk - the main (root) window
  -- The root window's mainloop - the Event Loop

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk  # Necessary in all but this trivial example.


def main():
    root = tkinter.Tk()
    root.mainloop()

    print('Done with the Event Loop')


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
