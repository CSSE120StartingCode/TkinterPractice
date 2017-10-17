"""
Example showing for tkinter and ttk:
  -- How to use Tk and Toplevel to construct new windows.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2013.
"""

import tkinter
from tkinter import ttk


class WindowsAndNumber():
    def __init__(self):
        self.number = None
        self.label = None
        self.windows = []


def main():
    """ Constructs and runs the GUI """
    root = tkinter.Tk()
    windows_and_number = WindowsAndNumber()

    gui(root, windows_and_number)

    root.mainloop()


def gui(root, windows_and_number):
    """ Puts widgets on the GUI """
    put_stuff_on_main_window(root, windows_and_number)
    put_stuff_on_window2(windows_and_number)
    put_stuff_on_window3(windows_and_number)


def put_stuff_on_main_window(root, windows):
    """ Puts Buttons on the main window. """
    window1_frame = ttk.Frame(root, padding=20)
    window1_frame.grid()

    increase_button = ttk.Button(window1_frame,
                                 text='Increase the number')
    increase_button.grid()
    increase_button['command'] = lambda: change_number(windows, 1)

    destroy_button = ttk.Button(window1_frame,
                                text='Destroy some windows')
    destroy_button.grid()
    destroy_button['command'] = lambda: destroy_windows(windows)


def put_stuff_on_window2(windows_and_number):
    """ Puts Buttons on a secondary window. """
    root2 = tkinter.Toplevel()  # Note Toplevel, NOT Tk.

    window2_frame = ttk.Frame(root2, padding=20)
    window2_frame.grid()

    decrease_button = ttk.Button(window2_frame,
                                 text='Decrease the number')
    decrease_button.grid()
    decrease_button['command'] = lambda: change_number(windows_and_number, -1)

    button_text = 'Pop up a new window with the number'
    pop_up_button = ttk.Button(window2_frame, text=button_text)
    pop_up_button.grid()
    pop_up_button['command'] = lambda: pop_up(windows_and_number)


def put_stuff_on_window3(windows_and_number):
    """ Puts a Label on a secondary window. """
    root3 = tkinter.Toplevel()  # Note Toplevel, NOT Tk.

    window3_frame = ttk.Frame(root3, padding=20)
    window3_frame.grid()

    number_label = ttk.Label(window3_frame, text='The number is: 0')
    number_label.grid()

    windows_and_number.number = 0
    windows_and_number.label = number_label


def change_number(windows_and_number, delta):
    """
    Changes the number in the data by the given delta,
    then displays the changed value in its Label.
    """
    windows_and_number.number = windows_and_number.number + delta
    msg = 'The number is: {}'.format(windows_and_number.number)
    windows_and_number.label['text'] = msg


def pop_up(windows_and_number):
    """ Pops up a window, with a Label that shows some info. """
    window = tkinter.Toplevel()  # Note Toplevel, NOT Tk.
    msg = 'The number is: \n {}'.format(windows_and_number.number)
    label = ttk.Label(window, text=msg)
    label.grid()

    windows_and_number.windows.append(window)


def destroy_windows(data):
    """ Destroys all the windows stored in the given Data object. """
    for k in range(len(data.windows)):
        data.windows[k].destroy()

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
