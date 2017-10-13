"""
Example showing for tkinter and ttk:
  -- How to CONSTRUCT and DISPLAY a WIDGET, in this case:
  -- ttk.Frame - a container for other Widgets
  -- ttk.Button - a button in the ttk style

Authors: David Mutchler, Mark Hays, and their colleagues
         at Rose-Hulman Institute of Technology. Summer 2016.
"""

import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    connect_button = ttk.Button(frame1, text='Connect')
    connect_button.grid()

    root.mainloop()

########################################################################
#
# EXPLANATION of the above:
#
# The 6 statements in main (above) do the following, respectively:
#
#   1. Constructs a tkinter.Tk.
#        This is the top-level window, traditionally called 'root'.
#
#   2. Constructs a widget (here, a ttk.Frame) on the root,
#        naming the Frame  frame1  for use in subsequent statements.
#
#        Use Frame objects to group other items.  Best practice is
#        to make a Frame and put all other widgets on the Frame.
#
#        This Frame has a "padding" of 10 pixels on each side.
#        Try removing the    padding=10    to see the effect of padding.
#
#   3. Displays the ttk.Frame, using a layout called 'grid'.
#         -- We'll learn more about controlling the layout later.
#         -- For now, simply apply the   grid   method to ANY widget
#            to make it appear on the screen.
#
#   4. Constructs a widget (here, a ttk.Button) on the Frame.
#         Set its text to 'Connect'.
#
#   5. Displays the ttk.Button, again using the 'grid' layout.
#
#   6. Runs the Event Loop.  tkinter maintains that loop.
#         This is a LOOP -- the code STAYS in here until the root window
#         is closed (by the user, or by the program itself).
#
# When you run the program, note that:
#   -- A window appears.
#   -- The window has the usual minimize, maximize and close buttons
#        in the window's title bar.
#   -- Those buttons work as expected.
#   -- There is also a button inside the window whose label is: Connect.
#   -- Pressing the Connect button causes visual feedback in the usual
#        way, but nothing else happens.  That's because we haven't told
#        tkinter/ttk what to do when the Connect button is pressed.
#        You'll see how to do that in the next examples.
########################################################################

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
