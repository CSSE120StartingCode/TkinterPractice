"""
Example showing for tkinter and ttk(Object Oriented Approach) :
  -- ttk.Label
  -- ttk.Button
  -- ttk.Frame
  -- Associating a Button with a CALLBACK function
Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

from tkinter import *
import random
from tkinter import ttk


class Example(Tk):
    def __init__(self, width, height):
        super().__init__()
        # Initial Variable Declaration and Assignment

        self.width = width
        self.height = height
        self.wm_geometry(f'{self.width}x{self.height}')
        self.title('Hello!')
        self.new_title = ''

        # Widgets Creation and Placement

        # Main Frame
        self.frame_1 = ttk.Frame(self)
        self.frame_1.grid()

        # Label inside Frame
        self.label_1 = ttk.Label(self.frame_1, text='This is a Label above a Button')
        self.label_1.grid()

        # Buttons_Title_Change

        self.change_title_btn = ttk.Button(self.frame_1, text='Change the Title (above)',
                                           command=self.change_title)
        self.change_title_btn.grid()

        # Button_Quit
        self.quit_button = ttk.Button(self.frame_1, text='Quit', command=lambda: self.quit())
        self.quit_button.grid()

        # Another Label, with its text set another way
        self.label2 = ttk.Label(self.frame_1)
        self.label2['text'] = 'Later, we will put Labels BESIDE Buttons'
        self.label2.grid()

    # Functions
    def change_title(self):
        self.new_title = ''
        for K in range(8):
            self.new_title = self.new_title + chr(ord('A') + random.randrange(26))
        self.title(f'{self.new_title}')


if __name__ == '__main__':
    mainwin = Example(250, 120)

    mainwin.mainloop()

