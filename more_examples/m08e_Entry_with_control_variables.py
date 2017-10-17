"""
Example showing for tkinter and ttk:
  -- ttk.Entry
  -- Using tkinter CONTROL VARIABLES -- StringVar, IntVar, DoubleVar --
     to get/set an Entry's information (as opposed to using the Entry's
     GET and SET methods as in a previous module)

     See a PREVIOUS module for a SIMPLER technique.
     This technique is sometimes more convenient,
     but is EASY TO GET WRONG, so USE IT CAREFULLY (if at all).

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk


class Data():
    def __init__(self):
        self.city = None
        self.temperature = None
        self.answer_for_Celsius = None


def main():
    data = Data()

    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    city_label = ttk.Label(main_frame, text='Enter the city:')
    city_label.grid()

    # The 3rd and 4th statement below link the StringVar CONTROL VARIABLE
    # whose name is   data.city   to the value in the above Entry box.
    # So changing one changes the other.  Note the   textvariable   key.
    city_entry = ttk.Entry(main_frame, width=10)
    city_entry.grid()
    data.city = tkinter.StringVar()
    city_entry['textvariable'] = data.city

    # Same idea for the Temperature Entry, but using an IntVar.
    temperature_entry = ttk.Entry(main_frame, width=5)
    temperature_entry.grid()
    data.temperature = tkinter.IntVar()  # Or use DoubleVar()
    temperature_entry['textvariable'] = data.temperature

    convert_button = ttk.Button(main_frame, text='Convert temperature')
    convert_button.grid()
    convert_button['command'] = lambda: convert(data)

    answer_for_Celsius = ttk.Label(main_frame, text='')
    answer_for_Celsius.grid()
    data.answer_for_Celsius = answer_for_Celsius

    root.mainloop()


def convert(data):
    # Note the   get   method that Control Variables have.  Also a  set.
    # You MUST use their   get   and    set   methods - the variable
    # itself is a CONTROL variable, so its value is not what you want.
    celsius = (5 / 9) * (data.temperature.get() - 32)
    city = data.city.get()
    new_text = 'Celsius temperature of {} is: {:0.2f}'.format(city, celsius)
    data.answer_for_Celsius['text'] = new_text

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
