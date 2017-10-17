"""
Example showing for tkinter and ttk:
  -- ttk.Checkbutton
  -- ttk.Radiobutton
  -- Using tkinter's StringVar, IntVar, DoubleVar to track changes

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk
import time


def main():
    # Thus usual root and main Frame.
    root = tkinter.Tk()
    mainframe = ttk.Frame(root, padding=20)
    mainframe.grid()

    # Checkbutton's and Radiobutton's have their own labels.
    checkbutton = ttk.Checkbutton(mainframe, text='Robots rule!')

    # Radiobutton's. We often put them onto a sub-frame,
    # to group them visually.  The 'value' identifies which is selected.
    radio_frame = ttk.Frame(mainframe, borderwidth=10, relief='groove')
    radio1 = ttk.Radiobutton(radio_frame, text='Peter Pevensie',
                             value='peter')
    radio2 = ttk.Radiobutton(radio_frame, text='Susan Pevensie',
                             value='susan')
    radio3 = ttk.Radiobutton(radio_frame, text='Edmund Pevensie',
                             value='edmund')
    radio4 = ttk.Radiobutton(radio_frame, text='Lucy Pevensie',
                             value='lucy')

    # This Button will show how it can interact with other widgets.
    button = ttk.Button(mainframe, text='Reset the other widgets')

    # Checkbutton's and Radiobutton's can have an "observer" variable
    # that is bound to the state of the Checkbutton / Radiobutton.
    checkbutton_observer = tkinter.StringVar()
    checkbutton['variable'] = checkbutton_observer

    radio_observer = tkinter.StringVar()
    for radio in [radio1, radio2, radio3, radio4]:
        radio['variable'] = radio_observer  # They all need the SAME observer

    # Bind callbacks using 'command' and lambda, as we have seen elsewhere.
    checkbutton['command'] = lambda: checkbutton_changed(checkbutton_observer)

    for radio in [radio1, radio2, radio3, radio4]:
        radio['command'] = lambda: radiobutton_changed(radio_observer)

    button['command'] = lambda: button_pressed(checkbutton_observer,
                                               radio_observer)

    # Layout the widgets (here, in a row with padding between them).
    # You can see more on layout in a subsequent example.
    c = 0
    for widget in [checkbutton, radio_frame, button]:
        widget.grid(row=0, column=c, padx=20)
        c = c + 1

    for radio in [radio1, radio2, radio3, radio4]:
        radio.grid(sticky='w')

    root.mainloop()


def checkbutton_changed(checkbutton_observer):
    print('The checkbutton changed to', checkbutton_observer.get())


def radiobutton_changed(radiobutton_observer):
    print('The radiobutton changed to', radiobutton_observer.get())


def button_pressed(checkbutton_observer, radiobutton_observer):
    print('After 2 seconds, I will toggle the Checkbutton')
    print('and reset the radiobutton to Peter\'s.')
    time.sleep(2)

    if checkbutton_observer.get() == '1':
        checkbutton_observer.set('0')
    else:
        checkbutton_observer.set('1')

    radiobutton_observer.set('peter')

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
