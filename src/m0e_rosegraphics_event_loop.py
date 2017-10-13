"""
This module demonstrates a simple EVENT LOOP
that uses POLLING (not an event queue) to get the events.

This is a RoseGraphics example, NOT a Tkinter example.

Functions:
  -- main: Contains the Event Loop
  -- mouse_handler: A handler for one kind of event
  -- key_handler: A handler for another kind of event
  -- make_window: Returns a window and rg.Text object for this example

Authors: David Mutchler, Mark Hays, and their colleagues
         at Rose-Hulman Institute of Technology. Summer 2016.
"""

import rosegraphics as rg


def main():
    """ Demonstrates a simple Event Loop that polls for events. """

    # ------------------------------------------------------------------
    # Make a window with messages on it.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(400, 400, 'Simple Event Loop')

    keyboard_text = rg.Text(rg.Point(140, 30), '')
    keyboard_text.attach_to(window)

    instructions = 'Click the mouse or press a key.\n Press q to quit.'
    instructions_text = rg.Text(rg.Point(200, 350), instructions)
    instructions_text.attach_to(window)

    while True:
        # --------------------------------------------------------------
        # Update the window's events.
        # --------------------------------------------------------------
        window.update()

        # --------------------------------------------------------------
        # Poll the devices (mouse and keyboard) to learn the events.
        # If an event has occurred, respond to it.
        # --------------------------------------------------------------
        if window.mouse.position is not None:
            mouse_event_callback(window, window.mouse.position)

        if window.keyboard.key_pressed is not None:
            key_event_callback(window, window.keyboard.key_pressed,
                               keyboard_text)

        # --------------------------------------------------------------
        # Render the window.  Then sleep a bit
        # to allow time for other threads/processes to run
        # --------------------------------------------------------------
        window.render(1.0)  # Purposely set way too big, thus "misses"
                            # events.  Try smaller for more responsive.

def mouse_event_callback(window, point):
    """
    This method should have been called by the system watching for
    "events" when a MOUSE event (in particular, a new mouse position)
    happens.  This method is the "callback" for that event.
    
    The method responds to the mouse event by drawing a small,
    blue-filled circle on the given window at the given point.

    Preconditions:
      :type window: rg.RoseWindow
      :type point: rg.Point
    """
    circle = rg.Circle(point, 10)
    circle.fill_color = 'blue'
    circle.attach_to(window)


def key_event_callback(window, key, textbox):
    """
    This method should have been called by the system watching for
    "events" when a KEY event (in particular, a key has been pressed)
    happens.  This method is the "callback" for that event.
    
    The method displays a message that indicates what key was pressed,
    putting the message in the given textbox in the given window.
    Also closes the window and exits the program if the key is 'q'.

    Preconditions:
      :type window: rg.RoseWindow
      :type key: str
      :type textbox: rg.Text
    """
    textbox.text = 'You pressed: ' + key
    window.render()

    if key == 'q':
        window.close()
        exit()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
