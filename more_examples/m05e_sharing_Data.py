"""
Example showing for tkinter and ttk:
  -- how Widgets can SHARE INFORMATION by using
     an OBJECT that is sent to the LAMBDA CALLBACK functions.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk
import random


class Label_Plus_Number(object):
    def __init__(self, initial_number):
        self.number_label = None
        self.number = initial_number
        self.digits_to_show = 1


def main():
    label1_plus = Label_Plus_Number(0)
    label2_plus = Label_Plus_Number(43)

    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    label1 = ttk.Label(frame)
    label1['text'] = 'First number is ' + str(label1_plus.number)
    label1.grid()
    label1_plus.number_label = label1

    label2 = ttk.Label(frame)
    label2['text'] = 'Second number is ' + str(label2_plus.number)
    label2.grid()
    label2_plus.number_label = label2

    increase_button = ttk.Button(frame, text='Increase first number')
    increase_button.grid()
    increase_button['command'] = lambda: increase_number(label1_plus, 1)

    decrease_button = ttk.Button(frame, text='Decrease first number')
    decrease_button.grid()
    decrease_button['command'] = lambda: increase_number(label1_plus, -1)

    zero_button = ttk.Button(frame, text='Reset first number to 0')
    zero_button.grid()
    zero_button['command'] = lambda: set_number_to_zero(label1_plus)

    multiply_button = ttk.Button(frame,
                                 text='Multiply second number by 10')
    multiply_button.grid()
    multiply_button['command'] = lambda: multiply_by_10(label2_plus)

    randomize_button = ttk.Button(frame, text='Randomize both numbers')
    randomize_button.grid()
    randomize_button['command'] = lambda: randomize(label1_plus,
                                                    label2_plus)

    root.mainloop()


def increase_number(label_plus_number, amount):
    """
    Increases the number in the given  Label_Plus_Number  object
    by the given amount.  Updates the Label in the given
    Label_Plus_Number  object that displays the number.
    """
    label_plus_number.number = label_plus_number.number + amount
    new_text = 'The number is ' + str(label_plus_number.number)
    label_plus_number.number_label['text'] = new_text


def set_number_to_zero(label_plus_number):
    """
    Sets the number in the given   Label_Plus_Number   object to zero.
    Does NOT update the Label in the given  Label_Plus_Number  object.
    """
    label_plus_number.number = 0


def multiply_by_10(label_plus_number):
    """
    Multiplies the number in the given  Label_Plus_Number  object by 10.
    Updates the Label accordingly in the given Label_Plus_Number object.
    """
    label_plus_number.number = label_plus_number.number * 10
    new_text = 'The number is ' + str(label_plus_number.number)
    label_plus_number.number_label['text'] = new_text


def randomize(label1_plus, label2_plus):
    """
    Randomizes the numbers in both  Label_Plus_Number  objects.
    Updates their displays.
    """
    label1_plus.number = random.randrange(100)
    label2_plus.number = random.randrange(100)

    label1_plus.number_label['text'] = str(label1_plus.number)
    label2_plus.number_label['text'] = str(label2_plus.number)

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
