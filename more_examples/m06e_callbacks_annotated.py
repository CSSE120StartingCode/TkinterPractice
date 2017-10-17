"""
Example of tkinter and ttk. It shows how to:

  -- 1. Make a widget respond to its EVENTs, via its CALLBACK function.

  -- 2. Send information to the widget when its CALLBACK function runs.

  -- 3a. Ask a widget for information that the widget knows about itself.
         That is, get information from the widget.

  -- 3b. Have two widgets be able to influence each other.

  -- 4. Share information between widgets.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk
import random


# A    Buttons_and_Song     object bundles buttons and a song
# into a single object.
# It is a convenience, not an essential feature, for this example.
class Buttons_and_Song():
    def __init__(self):
        self.root = None
        self.connect_button = None
        self.disconnect_button = None
        self.sing_button = None
        self.change_song_button = None
        self.quit_button = None
        self.song = 'Strawberry Fields'


def main():
    """ Demonstrates WIDGETs that respond to EVENTS using CALLBACKs. """

    # Makes an object that will hold data shared by the widgets
    buttons_and_song = Buttons_and_Song()

    # Makes the widgets, displays them and puts them
    # into a   Buttons_and_Song   object.
    root = make_widgets(buttons_and_song)

    # Associates callback functions with each button
    make_callbacks(buttons_and_song)
    make_more_callbacks(buttons_and_song)
    make_still_more_callbacks(buttons_and_song)

    # Enters tkinter's main loop.  EXECUTION STAYS HERE UNTIL QUIT.
    root.mainloop()


def make_widgets(buttons_and_song):
    """
    Makes the widgets to display -- root window, Frame and 3 Buttons.
    Displays them and stores them in the given Buttons_and_Song object.
    Returns the root window.
    """
    # Make the root and a ttk.Frame on it, as usual.
    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    # Construct and display some ttk.Button's in the usual way.
    connect_button = ttk.Button(frame, text='Connect')
    connect_button.grid()

    disconnect_button = ttk.Button(frame, text='Disconnect')
    disconnect_button.grid()

    sing_button = ttk.Button(frame, text='Sing')
    sing_button.grid()

    change_song_button = ttk.Button(frame, text='Change the song')
    change_song_button.grid()

    quit_button = ttk.Button(frame, text='Quit')
    quit_button.grid()

    # Store the root and buttons in the Data object.
    buttons_and_song.root = root
    buttons_and_song.connect_button = connect_button
    buttons_and_song.disconnect_button = disconnect_button
    buttons_and_song.sing_button = sing_button
    buttons_and_song.change_song_button = change_song_button
    buttons_and_song.quit_button = quit_button

    return root


def make_callbacks(buttons_and_song):
    """
    For the   Connect   and   Disconnect   ttk.Button's in the given
    Buttons_and_Song object, associates a CALLBACK function
    to call when the button is pressed.
    """
    #-------------------------------------------------------------------
    # Idea #1: Make a WIDGET respond to its EVENTs
    #          by associated a CALLBACK function with the widget.
    #
    #  -- A WIDGET is something that is on the GUI, like a button.
    #  -- An EVENT is something that happens in the GUI,
    #        like a button press.  Events are associated with widgets.
    #  -- A CALLBACK function is a function that we can associate with
    #        a widget.  The Event Loop will call the callback function
    #        when an event associated with the widget occurs.
    #
    #        For example, if a ttk.Button is clicked, the Event Loop
    #        notices the button-click and calls that ttk.Button's
    #        callback function.
    #
    #  -- Widgets are DICTIONARY-LIKE objects.  This means that they
    #        support the square bracket notation like sequences, e.g.
    #              x[5] = 'red'
    #        but the object inside the brackets is any immutable object,
    #        not necessarily a number.
    #        In particular, it can be a string, e.g.
    #              w['color'] = 'blue'
    #        For any object, the allowable things inside its brackets
    #        are called its KEYs.  So "color" is a KEY in the above
    #        example and the VALUE of that key for object w is 'blue'.
    #  -- Most widgets allow a "command" key whose value is the CALLBACK
    #        function, that is, the function that the Event Loop
    #        will call when an event associated with the widget happens.
    #        Note that this value is a FUNCTION, not a FUNCTION CALL.
    #
    #  -- The most useful way to define the callback function is to
    #        define it as a LAMBDA function, that is, an ANONYMOUS
    #        function defined IN-LINE, right inside an assignment.
    #        The notation for a lambda function is:
    #              -- the keyword     lambda
    #              -- then a colon
    #              -- then an EXPRESSION that is the code that runs
    #                 when the lambda function is called.
    #        In our case, the lambda function will be called by the
    #        Event Loop and its expression is typically a call to a
    #        function defined in the usual way.
    #
    # Choose sensible names for your callback functions!
    #-------------------------------------------------------------------

    # Extract two buttons from the given Data object (so note that they
    # must have been placed there before this function runs).
    # You do not have to use the same name for the local variables
    # as for the instance variables, but it is sensible to do so.
    connect_button = buttons_and_song.connect_button
    disconnect_button = buttons_and_song.disconnect_button

    # Associate the callbacks with the buttons.
    # Choose sensible names for the callbacks.
    connect_button['command'] = lambda: connect_to_robot()
    disconnect_button['command'] = lambda: print('hello')


def make_more_callbacks(buttons_and_song):
    """
    For the   Quit   and   Sing   ttk.Button's in the given
    Buttons_and_Song object, associates a CALLBACK function
    to call when the button is pressed.
    """
    #-------------------------------------------------------------------
    # Idea #2: SEND INFORMATION to a CALLBACK function when it runs.
    #
    # We send information to a callback function in the same way that
    # we send information to ANY function, namely, by calling the
    # function with ARGUMENTS (information) that are copied into the
    # PARAMETERS of the function when the function runs.
    #
    # The problem is that a callback is called by the Event Loop.
    # How can we make the Event Loop know what arguments to send?
    #
    # HERE IS THE TRICK: Since the callback function is defined INSIDE
    # another function (here, inside 'make_more_callbacks'), the body
    # of the callback function -- itself a function call -- can use as
    # arguments VARIABLES DEFINED IN THE ENCLOSING FUNCTION's NAMESPACE!
    #
    # For example, consider the Quit button.  It needs to tell the
    # Event Loop to stop looping.  To see how it might do so:
    #
    #   -- Recall that the Event Loop STARTED via the statement
    #             root.mainloop()
    #      where 'root' is the variable name of the tkinter.Tk object
    #      that we constructed at the beginning of the GUI creation.
    #
    #   -- So, to STOP the Event Loop, we have to tell that same
    #      tkinter.Tk object to 'destroy' itself
    #      (thus stopping the Event Loop).
    #
    #  -- So we MUST send the 'root' object to the callback function of
    #     the Quit button WHEN the callback is CALLED by the Event Loop.
    #
    #  -- And we CAN do so because the callback function is defined
    #     INSIDE a function that can reference the 'root' object.
    #     (In our case we stored the 'root' object in the
    #     Buttons_with_Song  object.)
    #-------------------------------------------------------------------

    # Extract the buttons and the root window from the given Data object.
    quit_button = buttons_and_song.quit_button
    sing_button = buttons_and_song.sing_button
    root = buttons_and_song.root

    # Associate the callbacks with the buttons.  Note arguments!
    quit_button['command'] = lambda: quit_gui(root)
    sing_button['command'] = lambda: sing(buttons_and_song.song)


def make_still_more_callbacks(buttons_and_song):
    #-------------------------------------------------------------------
    # Idea #3:
    #   -- 3a. Ask a widget for information that the widget knows about
    #          itself.  That is, get information from the widget.
    #   -- 3b. Have two widgets be able to influence each other.
    #   -- 3c. Share information between widgets
    #-------------------------------------------------------------------

    # Extract the button from the given Data object.
    change_song_button = buttons_and_song.change_song_button

    # Associate the callback with the button.  Note arguments!
    change_song_button['command'] = lambda: change_song(buttons_and_song)


def connect_to_robot():
    """ Connects to the robot (but not yet implemented) """
    print('\nConnecting to the robot.')
    print('[TODO: add robot code to this function!]')


def quit_gui(root):
    """ Quits the Event Loop """
    print('\nExiting the Event Loop.')
    root.destroy()


def sing(song):
    """ Sings the given song (just prints for now) """
    print(song)


def change_song(buttons_and_song):
    """
    Changes the song stored in the given  Buttons_and_Song   object.
    Also fools around with other buttons, just to show how one
    widget can change the appearance of other widgets.
    """
    newsong = ''
    for k in range(10):  # @UnusedVariable
        newsong = newsong + chr(random.randrange(40, 110))
    print(buttons_and_song.song, newsong)
    buttons_and_song.song = newsong

    connect_button = buttons_and_song.connect_button
    if connect_button['text'] == 'Connect':
        connect_button['text'] = 'Your Momma wears Army Boots'
    else:
        connect_button['text'] = 'Connect'

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
