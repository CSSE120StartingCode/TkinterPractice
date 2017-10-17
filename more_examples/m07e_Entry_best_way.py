"""
Example showing for tkinter and ttk:
  -- ttk.Entry
  -- Using its GET and SET methods to get/set an Entry's information
     (as opposed to using a CONTROL VARIABLE as in a subsequent module)

     This is the SIMPLER way to use an Entry box.
     See a subsequent module for a more complicated alternative that is
     sometimes more convenient than this way.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk


class Temperature():
    def __init__(self):
        self.entry_for_temperature = None
        self.label_for_temperature = None


def main():
    # Data object to hold information needed for callbacks.
    temperature = Temperature()

    # Root window and Frame on it.
    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    # The Entry box, into which the user can enter a temperature.
    # We store it in the Temperature object so that we can later
    # get its contents.
    entry = ttk.Entry(frame, width=8)
    entry.grid()
    temperature.entry_for_temperature = entry

    # A Label which will display the temperature corresponding to the
    # temperature that the user enters in the Entry box.
    # We store the label in the Temperature object so that we can later
    # put the computed temperature on it.
    label = ttk.Label(frame, text='Enter a temperature in the box')
    label.grid()
    temperature.label_for_temperature = label

    # Buttons that: get Entry value, compute and display temperature
    button1 = ttk.Button(frame, text='Compute Fahrenheit from Celsius')
    button1.grid()
    button1['command'] = lambda: fahrenheit_from_celsius(temperature)

    button2 = ttk.Button(frame, text='Compute Celsius from Fahrenheit')
    button2.grid()
    button2['command'] = lambda: celsius_from_fahrenheit(temperature)

    root.mainloop()


def celsius_from_fahrenheit(temperature):
    # Get the contents (as a STRING) from the Entry box.
    entry = temperature.entry_for_temperature
    contents_of_entry_box = entry.get()

    # Convert that STRING to a floating point NUMBER.
    # Use the number to compute the corresponding Celsius temperature.
    fahrenheit = float(contents_of_entry_box)
    celsius = (5 / 9) * (fahrenheit - 32)

    # Display the computed Celsius temperature in the Label
    # provided for it.
    format_string = '{:0.2f} Fahrenheit is {:0.2f} Celsius'
    answer = format_string.format(fahrenheit, celsius)
    temperature.label_for_temperature['text'] = answer


def fahrenheit_from_celsius(temperature):
    # Get the contents (as a STRING) from the Entry box.
    entry = temperature.entry_for_temperature
    contents_of_entry_box = entry.get()

    # Convert that STRING to a floating point NUMBER.
    # Use the number to compute corresponding Fahrenheit temperature.
    celsius = float(contents_of_entry_box)
    fahrenheit = (celsius * (9 / 5)) + 32

    # Display the computed Fahrenheit temperature in the Label
    # provided for it.
    format_string = '{:0.2f} Celsius is {:0.2f} Fahrenheit'
    answer = format_string.format(celsius, fahrenheit)
    temperature.label_for_temperature['text'] = answer

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
