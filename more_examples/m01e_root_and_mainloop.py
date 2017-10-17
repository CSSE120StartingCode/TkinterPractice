"""
Example showing for tkinter and ttk:
  -- tkinter.Tk - the main (root) window
  -- The root window's mainloop - the Event Loop

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. October 2012.
"""

import tkinter
from tkinter import ttk  # Necessary in all but this trivial example.


def main():
    root = tkinter.Tk()
    root.mainloop()

    print('Done with the Event Loop')

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
