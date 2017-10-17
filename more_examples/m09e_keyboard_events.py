"""
Example showing for tkinter and ttk how to:
  -- 1. BIND callback functions (event-handlers) to KEYBOARD EVENTs.
  -- 2. RESPOND to KEYBOARD events.

There is LOTS more you can do with Events beyond what is shown here.
See the next module for more, and for all (or at least most) of the
details, see Section 30 of:
  tkinterReference-NewMexicoTech.pdf

in the Graphics section of the Resources web page for this course.
That document is also available in html form at:
  http://infohost.nmt.edu/tcc/help/pubs/tkinter/events.html

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk


def main():
    # Make root, frame and 3 buttons with callbacks.
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    left_button = ttk.Button(main_frame, text='Left')
    left_button.grid()

    right_button = ttk.Button(main_frame, text='Right')
    right_button.grid()

    spin_button = ttk.Button(main_frame, text='Spin')
    spin_button.grid()

    left_button['command'] = lambda: go_left_button()
    right_button['command'] = lambda: go_right()
    spin_button['command'] = lambda: spin()

    #--------------------------------------------------------------------
    # For general-purpose keyboard events, use    root.bind_all(...).
    # This method "binds" (attaches) the given EVENT to the given
    # CALLBACK FUNCTION for ALL widgets on this root and its descendants.
    #
    # Note that the lambda function for bind_all requires a parameter.
    # When the lambda function is called by tkinter in its mainloop,
    # the actual event that fired is sent as the argument.  You can
    # use this to obtain details about the event.
    #
    # Try press, release, click and press-and-hold in the examples.
    #--------------------------------------------------------------------
    root.bind_all('<KeyPress>', lambda event: pressed_a_key(event))
    root.bind_all('<KeyRelease>', lambda event: released_a_key(event))

    #--------------------------------------------------------------------
    # To bind a particular key, simply specify the key (see below).
    #
    # WARNING: If you bind multiple functions to the same widget and
    # event, various things can happen (see your instructor or the link
    # in the comment at the top of this module if you need details).
    #
    # For an ordinary 102-key PC-style keyboard, the special keys are
    # Cancel (the Break key), BackSpace, Tab, Return(the Enter key),
    # Shift_L (any Shift key), Control_L (any Control key),
    # Alt_L (any Alt key), Pause, Caps_Lock, Escape, Prior (Page Up),
    # Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert,
    # Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12,
    # Num_Lock, and Scroll_Lock.
    # For other key names, see Section 30.5 in the document referenced
    # at the top of this module, and also perhaps Table 7.1 of
    #   www.pythonware.com/library/tkinter/introduction/events-and-bindings.htm
    #--------------------------------------------------------------------------
    root.bind_all('<Key-L>', lambda event: go_left(event))
    root.bind_all('<Key-R>', lambda event: go_right(event))
    root.bind_all('<Key-r>', lambda event: go_right(event))
    root.bind_all('<Key-space>', lambda event: spin(event))

    root.mainloop()


def pressed_a_key(event):
    # Notice how you can find out the key that was pressed.
    print('You pressed the', event.keysym, 'key')


def released_a_key(event):
    print('You released the', event.keysym, 'key')


def go_left(event):
    print('You pressed the ' + event.keysym + ' key: ', end='')
    print('Go left!')


def go_left_button():
    print('You clicked the Left button: ', end='')
    print('Go left!')


def go_right(event=None):
    # Fancier version that allows EITHER key OR button presses.
    # The former provides the event, the latter does not.
    # It is UN-likely that you will want this fancier version.
    # Instead, use the SIMPLER version per   go_left.
    if event == None:
        print('Button press: ', end='')
    else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
    print('Go right!')


def spin(event=None):
    # Fancier version, see comment in   go_right.
    if event == None:
        print('Button press: ', end='')
    else:
        print('You pressed the ' + event.keysym + ' key: ', end='')
    print('Spin!')

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
