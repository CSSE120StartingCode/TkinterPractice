"""
Example showing for tkinter and ttk:
  -- How to construct and display a:
          ttk.Entry
       that allows the human user to enter information into it.

  -- How to associate a widget (here, a ttk.Button)
       with a CALLBACK function that is a LAMBDA (anonymous) function
       which TAKES the Entry as an ARGUMENT.

  -- How the callback function can use the Entry's GET and SET methods
       to get/set the Entry's information.
       
This is the SIMPLEST (and for you, BEST) way to use an Entry box.

See a subsequent module for a more complicated alternative
that uses a CONTROL VARIABLE.  The more complicated alternative
is sometimes more convenient but never necessary.

Authors: David Mutchler, Mark Hays, and their colleagues
         at Rose-Hulman Institute of Technology. Summer 2016.
"""

import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    print_entry_button = ttk.Button(frame1, text='Print entry')
    print_entry_button['command'] = (lambda:
                                     print_contents(my_entry_box))
    print_entry_button.grid()

    root.mainloop()


def print_contents(entry_box):
    """
    Prints onto the Console the contents of the given ttk.Entry.
    
    In this example, it is used as the function that is "CALLED BACK"
    when an event (namely, the pressing of a certain Button) occurs.
    
    Type hints:
      :type entry_box: ttk.Entry
    """
    contents_of_entry_box = entry_box.get()
    print(contents_of_entry_box)

########################################################################
#
# EXPLANATION of the above:
#
# This example is the same as the previous example except for:
#   -- There is an Entry box in which the human user can enter a string.
#   -- There is a function called   print_contents   that
#        takes an ARGUMENT that is expected to be a ttk.Entry.
#   -- The LAMBDA expression defines a function that calls
#        the   print_contents   function, sending it the Entry box
#        made a few lines above the lamda function as an argument.
#   -- Hence, the Button can do stuff with the CONTENTS of the Entry box.
#
# To make a Button respond to a button-press by doing things with
#   the CONTENTS of an ENTRY box:
#
#   1. Set a value to the Button's 'command' attribute,
#        as described in the previous module.  For example:
#
#           button1['command'] = ...
#
#   2. Use a LAMBDA expression to express WHAT the Button should do
#      when pressed, as described in the previous module.  For example:
#
#           button1['command'] = (lambda:
#                                 foo(...))
#
#   3. Construct and display a ttk.Entry prior to telling Button
#        what its command is:
#
#           entry1 = ttk.Entry(frame1)
#
#   4. Make the body of the lambda expression (that is, the function
#        that the lambda function calls when the lambda function
#        is executed) take the ttk.Entry as an ARGUMENT.  For example:
#
#           entry1 = ttk.Entry(frame1)
#           button1['command'] = (lambda:
#                                 foo(entry1))
#   5. The function that the lambda function calls when the lambda
#        function is executed can use the given Entry box to access
#        the CONTENTS of the Entry box using its  GET  method.
#        For example:
#
#            def foo(entry_box):
#                s = entry_box.get()
#
#
# Do not confuse the Entry box:
#    -- the ttk.Entry widget that is displayed and into which the human
#       user can type stuff
#
# with the CONTENTS of the Entry box:
#    -- which is accessed via the Entry box's   get   method, as in:
#          entry_box.get()
#
# Do not forget that   entry_box.get()   returns the contents of the
# Entry box
#    ** at the TIME that the   entry_box.get()   expression runs. **
#
# Do not forget that   entry_box.get()   returns a STRING.
#    -- If the string represents an INTEGER, then the   int  function
#       returns the INTEGER that the STRING REPRESENTS.  For example:
#
#                contents = entry_box.get()
#                n = int(contents)
#       makes   n   be an integer if the human typed an integer
#       into the Entry box.
#
#       Likewise, the   float   function returns the floating point
#       number that the string represents.
#
########################################################################

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
