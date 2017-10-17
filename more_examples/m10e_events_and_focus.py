"""
Example showing for tkinter and ttk how to:
  -- 1. BIND callback functions (event-handlers) to Events.
  -- 2. RESPOND to Events.
  -- 3. Associate a WIDGET with the EVENT (and its callback function).

In particular, this example shows how to bind the RETURN Event
to different Entry boxes.

There is LOTS more you can do with Events beyond what is shown here.
See the previous module for more, and for all (or at least most) of the
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


class Data():
    def __init__(self):
        self.number = 0
        self.entry_box1 = None
        self.entry_box2 = None
        self.number_label = None


def main():
    data = Data()

    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    intro = 'This example shows how keys can be associated\n' \
        + 'with widgets.  The widget must have the "focus"\n' \
        + 'for its event to fire.\n\n' \
        + 'In this example, the <Return> (Enter key) event\n' \
        + 'is associated with each of the 2 Entry boxes,\n' \
        + 'and the u and d keys and mouse press are associated\n' \
        + 'with the button.\n\n' \
        + 'Try the u and d keys, with and without the button having\n' \
        + 'the focus.  Try entering numbers in the Entry boxes\n' \
        + 'with and without pressing the Enter key.\n'
    intro_label = ttk.Label(main_frame, text=intro)
    intro_label.grid()

    number_text = 'The number is {}'.format(data.number)
    number_label = ttk.Label(main_frame, text=number_text)
    number_label.grid()
    data.number_label = number_label

    #--------------------------------------------------------------------
    # In the previous module, you saw   bind_all   which binds the Event
    # to ALL the widgets on the root.  If you want the callback to occur
    # only when a certain Widget has the "focus" (and the Event occurs),
    # use   bind   (not bind_all), per the following examples:
    #--------------------------------------------------------------------

    entry1 = ttk.Entry(main_frame, width=4)
    entry1.grid()
    entry1.bind('<Return>', lambda event: callback1(event, data))
    data.entry_box1 = entry1

    entry2 = ttk.Entry(main_frame, width=4)
    entry2.grid()
    entry2.bind('<Return>', lambda event: callback2(event, data))
    data.entry_box2 = entry2

    #--------------------------------------------------------------------
    # You can bind Events to Buttons (and any other Widget).  So the
    # first   button.bind   below shows an alternative to ['command'].
    #--------------------------------------------------------------------

    button_text = 'Use the TAB key to give me the "focus",'
    button_text = button_text + '\n then press the u or d key'
    button = ttk.Button(main_frame, text=button_text)
    button.grid()

    button.bind('<Button-1>', lambda event: callback3(event, data))
    button.bind('<Key-u>', lambda event: callback3(event, data))
    button.bind('<Key-d>', lambda event: callback3(event, data))

    root.mainloop()


def callback1(event, data):
    """
    Increases the number in the given Data object by the value
    of the Entry box bound to the given Event.
    """
    widget = event.widget
    number_in_entry_box = int(widget.get())
    print('This is callback1, which uses Widget: ' + str(widget))
    data.number = data.number + number_in_entry_box

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)


def callback2(event, data):
    """
    Decreases the number in the given Data object by the value
    of the Entry box bound to the given Event.
    """
    widget = event.widget
    number_in_entry_box = int(widget.get())
    print('This is callback2, which uses Widget: ' + str(widget))
    data.number = data.number - number_in_entry_box

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)


def callback3(event, data):
    """
    Increments or decrements the number in the given Data object
    depending on the given Event.
    """
    print('hello')
    if event.type == '2':  # 2 is the KEY type in Windows, it seems
        if event.keysym == 'u':
            print('u key was pressed while the button had focus')
            data.number = data.number + 1
        elif event.keysym == 'd':
            print('d key was pressed while the button had focus')
            data.number = data.number - 1
        else:
            print('Unexpected - key ' + event.keysym + ' was pressed.')
    elif event.type == '4':  # 4 is the BUTTON type in Windows, it seems
        print('button was pressed')
        data.number = data.number + 1  # So mouse press is same as u key.
    else:
        print('Unexpected - event type ' + event.type + ' occurred.')

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
