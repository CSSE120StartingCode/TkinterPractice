"""
Example showing for tkinter and ttk how to:
  -- Put an IMAGE on a Button (or anything else).
  -- Also have text if you want.

Note: The image file for tkinter/ttk must be a GIF (or one of several
      other unhelpful formats).  PIL -- Python Imaging Library --
      is the standard library for converting images in Python.
      An UNofficial port of PIL to Python 3 is available on the
      course web site (under the Graphics section) of Resources.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2013.
"""

import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    # The image file must be GIF (or one of several other unhelpful
    # formats). To convert a JPG or anything else, use an outside tool.
    # Note that the image file must be in the same folder as this
    # module, if you use this way to refer to the image file.
    photo = tkinter.PhotoImage(file='CreateImage.gif')

    button1 = ttk.Button(main_frame, image=photo)
    # The next line is necessary when your root.mainloop() call is outside the 
    # current method. Tkinter has a bug that makes it think the image is ready for 
    # garbage collection, which makes the image fully transparent. 
    # See: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
    button1.image = photo
    button1.grid()
    button1['command'] = lambda: print('hello')

    button2 = ttk.Button(main_frame, image=photo,
                        text='Image PLUS text', compound='top')
    #See note above for the reason the next line is needed.
    button2.image = photo
    button2.grid()
    button2['command'] = lambda: print('goodbye')

    root.mainloop()

    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
