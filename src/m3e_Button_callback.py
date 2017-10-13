"""
Example showing for tkinter and ttk:
  -- How to CONSTRUCT and DISPLAY a WIDGET
       (in this case, a ttk.Button)

  -- How to associate a widget (here, a ttk.Button)
       with a CALLBACK function that is a LAMBDA (anonymous) function.

Authors: David Mutchler, Mark Hays, and their colleagues
         at Rose-Hulman Institute of Technology. Summer 2016.
"""

import tkinter
from tkinter import ttk
import random


def main():
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    print_stuff_button = ttk.Button(frame1, text='Print stuff')
    print_stuff_button['command'] = (lambda:
                                     do_stuff())
    print_stuff_button.grid()

    root.mainloop()


def do_stuff():
    """
    Print onto the Console a random 10-letter string.
    
    In this example, it is used as the function that is "CALLED BACK"
    when an event (namely, the pressing of a certain Button) occurs.
    """
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z')
    random_word = ''
    for _ in range(10):
        letter = letters[random.randrange(26)]
        random_word = random_word + letter

    print(random_word)

########################################################################
#
# EXPLANATION of the above:
#
# This example is the same as the previous example except for:
#   -- There is a function called   do_stuff   that prints random stuff.
#   -- The Button responds to a button-press
#        by calling the  do_stuff   function.
#
# To make a Button respond to a button-press:
#
#   1. Setting a value to the Button's 'command' attribute
#      tells the Button to respond to a button press.  For example:
#
#           button1['command'] = ...
#
#      tells the Button named  button1  to do the   ...   stuff
#      when the button is pressed.
#
#      This is called "dictionary-like" notation.  Tkinter knows that
#      when you put the special string    'command'    inside the
#      square brackets, then you are telling the Button what to do
#      when the Button is pressed.
#
#   2. To express WHAT the Button should do when pressed,
#      use a  LAMBDA  expression, like this:
#
#           button1['command'] = (lambda:
#                                 foo())
#
#      The LEFT-hand-side of the assignment tells the Button that
#      it should execute the function defined by the RIGHT-hand-side
#      of the assignment, when the Button is pressed.
#
#      The right-hand-side of the assignment DEFINES a function,
#      just like a DEF expression DEFINES a function.  The difference
#      is that a function defined by a DEF has a name, e.g.
#           def blah():
#               ...
#               ...
#      and can contain multiple statements, but a LAMBDA function
#      is ANONYMOUS -- it has no name -- and (in Python) can contain
#      only a single statement as its body.  So the expression:
#              lambda: foo()
#      defines an anonymous (no-name) function that, when executed,
#      simply calls the function named  foo  that is defined elsewhere.
#
#      Note that a lamda expression DEFINES a function that is EXECUTED
#      LATER (here, when the Button is pressed).  It serves as a way
#      to DEFINE a function INSIDE an assignment statement.
#
#      You don't have to break a lambda expression over two lines.
#      For example:
#           button1['command'] = lambda: foo()
#
#      is equivalent to:
#           button1['command'] = (lambda:
#                                 foo())
#
#      We choose to use the two-line form because it makes it look
#      more like a DEF and gives a bit more space on a line
#      for the body of the lambda expression.
#
########################################################################

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
