"""
Example showing for tkinter and ttk:
  -- How to lay out windows using just a few ideas:
       1. Organize by using frames within frames (within frames...)
       2. Use grid(row=XX, col=YY) to organize the frames/widgets
          in an organized grid.
       3. Use -ipadx, ipady, sticky=...

There is LOTS more you can do with layout,
but the above will take you a long way.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2013.
"""

import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=5)
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid(ipadx=50, ipady=30)

    main_frame.columnconfigure(0, weight=5)
    main_frame.columnconfigure(1, weight=1)

    # Subframe 1.
    sub_frame1 = ttk.Frame(main_frame, padding=20, relief='groove')
    sub_frame1.grid(row=0, column=0)

    msg = '      Widget A \n in row 0, column 0'
    buttonA = ttk.Button(sub_frame1, text=msg)
    buttonA.grid(row=0, column=0)

    msg = '      Widget B \n in row 0, column 1'
    buttonB = ttk.Button(sub_frame1, text=msg)
    buttonB.grid(row=0, column=1)

    msg = '      Widget C \n in row 0, column 2, '
    msg += '\n with ipadx 100, ipady 20'
    buttonC = ttk.Button(sub_frame1, text=msg)
    buttonC.grid(row=0, column=2, ipadx=100, ipady=20)

    msg = 'Widget D \n in row 1, \n column 0, '
    msg += '\n centered in \n its column \n (default)'
    buttonD = ttk.Button(sub_frame1, text=msg)
    buttonD.grid(row=1, column=0)

    msg = 'Widget E \n in row 1, column 1'
    buttonE = ttk.Button(sub_frame1, text=msg)
    buttonE.grid(row=1, column=1)

    msg = 'Widget FFFFFFFFF \n in row 2, column 0, '
    msg += '\n spans 2 columns \n and 3 rows'
    buttonF = ttk.Button(sub_frame1, text=msg)
    buttonF.grid(row=2, column=0, columnspan=2, rowspan=3, ipady=100)

    msg = 'Widget G \n in row 1, column 2 \n sticky = w'
    buttonG = ttk.Button(sub_frame1, text=msg)
    buttonG.grid(row=1, column=2, sticky='w')  # n, s, e, w

    msg = 'Widget H \n in row 2, column 2 \n sticky = e'
    buttonG = ttk.Button(sub_frame1, text=msg)
    buttonG.grid(row=2, column=2, sticky='e')  # n, s, e, w

    msg = 'Widget I \n in row 3, column 2 \n sticky = ne'
    buttonG = ttk.Button(sub_frame1, text=msg)
    buttonG.grid(row=3, column=2, sticky='ne')  # n, s, e, w

    msg = 'Widget J \n in row 4, column 2 \n sticky = sw'
    buttonG = ttk.Button(sub_frame1, text=msg)
    buttonG.grid(row=4, column=2, sticky='sw')  # n, s, e, w

    # Subframe 2.
    sub_frame2 = ttk.Frame(main_frame, padding=10, relief='raised')
    sub_frame2.grid(row=0, column=1, ipadx=100, ipady=100)

    buttonAA = ttk.Button(sub_frame2, text='Widget AA')
    buttonAA.grid(row=0, column=0)

    buttonBB = ttk.Button(sub_frame2, text='Widget BB')
    buttonBB.grid(row=1, column=0)

    buttonCC = ttk.Button(sub_frame2, text='Widget CC')
    buttonCC.grid(row=0, column=1, rowspan=2)

    # Subframe 3.
    sub_frame3 = ttk.Frame(main_frame, padding=10, relief='sunken')
    sub_frame3.grid(row=1, column=0)

    msg = 'Widget AAA \n in row 0, column 0 \n '
    msg += 'but will be \n overwritten \n accidentally'
    buttonAA = ttk.Button(sub_frame3, text=msg)
    buttonAA.grid(row=0, column=0)

    msg = 'Widget BBB \n in row 0, column 1'
    buttonBB = ttk.Button(sub_frame3, text=msg)
    buttonBB.grid(row=0, column=1)

    msg = 'Widget CCC \n in row 0, column 0 (oops)'
    buttonCC = ttk.Button(sub_frame3, text=msg)
    # The next line is a purposeful error, to show what happens
    buttonCC.grid(row=0, column=0)

    root.mainloop()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
