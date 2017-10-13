"""
rosegraphics.py - a simple Graphics library for Python.
Its key feature is:
  -- USING this library provides a simple introduction to USING objects.

Other key features include:
  -- It has a rich set of classes, methods and instance variables.
       -- In addition to classes like Circles that are natural for
            students, it has other kinds of classes like RoseWindow
            and FortuneTeller to provide a richer set of examples
            than "just" a graphics library.
  -- It allows one to do a reasonable set of graphics operations
       with reasonable efficiency. The API mimics Java's Shape API
       for the most part.
  -- It is built on top of tkinter and its extension ttk
       (the standard graphics libraries that come with Python).
  -- Unlike tkinter, it is NOT event-driven and hence can be used
       before students see that paradigm.  (There is a behind-the-scenes
       facilty for listening for and responding to events,
       for those who want to do so.)
  -- It attempts to be as bullet-proof as possible, to make it easy
       for beginners to use it.  In particular, it attempts to provide
       reasonable error messages when a student misuses the API.
  -- It was inspired by zellegraphics but is a complete re-implemenation
       that attempts to:
       -- Be more bullet-proof.
       -- Provide a richer set of examples for using objects.
       -- Have an API that is more like Java's Shape API than tkinter's
            (older) API.
  -- While it can serve as an example for defining classes,
        it is NOT intended to do so for beginners.
        It is excellent for helping students learn to USE objects;
        it is NOT perfect for helping students learn to WRITE CLASSES.

See the MAIN function below for typical examples of its use.

Authors: David Mutchler, Mark Hays, Michael Wollowswki, Matt Boutell,
         Chandan Rupakheti, Claude Anderson and their colleagues,
         with thanks to John Zelle for inspiration and hints.
         First completed version: September 2014.
"""

# FIXME (things that have yet to be implemented):
#  -- Allow multiple canvasses.
#  -- Better close_on ... ala zellegraphics.
#  -- Keyboard.
#  -- Better Mouse.
#  -- Add type hints.
#  -- Catch all Exceptions and react appropriately.
#  -- Implement unimplemented classes.
#  -- Add and allow FortuneTellers and other non-canvas classes.

import tkinter
from tkinter import font as tkinter_font
import time

# ----------------------------------------------------------------------
# All the windows that are constructed during a run share the single
#    _master_Tk   (a tkinter.Tk object)
# as their common root.  The first construction of a RoseWindow
# sets this  _master_Tk to a Tkinter.Tk object.
# ----------------------------------------------------------------------
_master_Tk = None


# ----------------------------------------------------------------------
# At the risk of not being Pythonic, we provide a simple type-checking
# facility that attempts to provide meaningful error messages to
# students when they pass arguments that are not of the expected type.
# ----------------------------------------------------------------------
class WrongTypeException(Exception):
    """ Not yet implemented. """
    pass


def check_types(pairs):
    """ Not yet implemented fully. """
    for pair in pairs:
        value = pair[0]
        expected_type = pair[1]
        if not isinstance(value, expected_type):
            raise WrongTypeException(pair)


# ----------------------------------------------------------------------
# RoseWindow is the top-level object.
# It starts with a single RoseCanvas.
# ----------------------------------------------------------------------
class RoseWindow(object):
    """
    A RoseWindow is a window that pops up when constructed.
    It can have   RoseWidgets   on it and starts by default with
    a single  RoseCanvas   upon which one can draw shapes.

    Public data attributes: width, height, title, color, widgets.
    Public methods:
      close, update, render, wait_for_mouse_click, wait_for_key_press,
      check_for_mouse_click, check_for_key_press, close_on_mouse_click.
    """

    def __init__(self, width=400, height=300, title='Rose Graphics',
                 color='black', canvas_color=None,
                 make_initial_canvas=True):
        """
        Pops up a   tkinter.Toplevel   window with (by default)
        a   RoseCanvas  (and associated tkinter.Canvas) on it.

        Arguments are:
          -- width, height: dimensions of the window (in pixels).
          -- title:  title displayed on the windoww.
          -- color:  background color of the window
          -- canvas_color:  background color of the canvas
                            displayed on the window by default
          -- make_initial_canvas:
               -- If True, a default canvas is placed on the window.
               -- Otherwise, no default canvas is placed on the window.

        If this is the first RoseWindow constructed, then a
        hidden   Tk   object is constructed to control the event loop.

        Preconditions:
          :type width: int
          :type height: int
          :type title: str
          :type color: Color
          :type canvas_color: Color
          :type make_initial_canvas: bool
        """
#         check_types([(width, (int, float)),
#                      (height, (int, float)),
#                      (title, (Color, str)

        # --------------------------------------------------------------
        # The _master_Tk controls the mainloop for ALL the RoseWindows.
        # If this is the first RoseWindow constructed in this run,
        # then construct the _master_Tk object.
        # --------------------------------------------------------------
        global _master_Tk
        if not _master_Tk:
            _master_Tk = tkinter.Tk()
            _master_Tk.withdraw()
        else:
            time.sleep(0.1)  # Helps the window appear on TOP of Eclipse

        # --------------------------------------------------------------
        # Has a tkinter.Toplevel, and a tkinter.Canvas on the Toplevel.
        # --------------------------------------------------------------
        self.toplevel = tkinter.Toplevel(_master_Tk,
                                         background=color,
                                         width=width, height=height)
        self.toplevel.title(title)
        self._is_closed = False
        self.toplevel.protocol("WM_DELETE_WINDOW", self.close)

        # FIXME: The next two need to be properties to have
        # setting happen correctly.  Really belongs to RoseCanvas.
        # See comments elsewhere on this.

        self.width = width
        self.height = height

        if make_initial_canvas:
            self.initial_canvas = RoseCanvas(self, width, height,
                                             canvas_color)
        else:
            self.initial_canvas = None

        self.widgets = [self.initial_canvas]

        # FIXME: Do any other tailoring of the toplevel as desired,
        #       e.g. borderwidth and style...

        # --------------------------------------------------------------
        # Catch mouse clicks and key presses.
        # --------------------------------------------------------------
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.toplevel.bind('<Button>', self._on_mouse_click)
        self.toplevel.bind('<KeyPress>', self._on_key_press)

        self.update()

    def close(self):
        """ Closes this RoseWindow. """
        if self.toplevel:
            self.toplevel.destroy()
            self.toplevel = None
        self.update()
        self._is_closed = True

    def update(self):
        """
        Checks for and handles events that has happened
        in this RoseWindow (e.g. mouse clicks, drawing shapes).
        """
        global _master_Tk
        _master_Tk.update()

    def render(self, seconds_to_pause=None):
        """
        Updates all the Shapes attached to RoseCanvas objects
        associated with this RoseWindow, then draws all those Shapes.
        After doing so, pauses the given number of seconds.

        Arguments:
          -- seconds_to_pause: the number of seconds to pause
        """
        for widget in self.widgets:
            if type(widget) == RoseCanvas:
                widget.render()

        self.update()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def close_on_mouse_click(self):
        message = 'To exit, click anywhere in this window'
        click_position = self.continue_on_mouse_click(message=message,
                                                      close_it=True)
        return click_position

    def continue_on_mouse_click(self,
                                message="""To continue,
                                    click anywhere in this window""",
                                x_position=None,
                                y_position=None,
                                close_it=False,
                                erase_it=True):
        """
        Displays a message at the bottom center of the window and
        waits for the user to click the mouse, then erases the message.

        Optional parameters let you:
          -- Display a different message
          -- Place the message at a different place in the window
               (xpos and ypos are as in Text)
          -- Close the window after the mouse is clicked
               (and ignore the GraphicsError that results if the user
               instead chooses to click the   X   in the window)
          -- NOT erase the message when done
        """
        if self._is_closed:
            return
        if x_position is None:
            x_position = self.width / 2
        if y_position is None:
            y_position = self.height - 20
        anchor_point = Point(x_position, y_position)
        text = Text(anchor_point, message)

        # FIXME: Really should do all this on a per-RoseCanvas basis.

        if self.initial_canvas:
            text.attach_to(self.initial_canvas)
            self.initial_canvas._renderShape(text, render_NOW=True)

        click_position = self.get_next_mouse_click()

        if erase_it and self.initial_canvas:
            text.detach_from(self.initial_canvas)

        if close_it:
            self.close()  # then close the window

        return click_position

    def get_next_mouse_click(self):
        # Mark: I don't like rendering here.
        # Students don't see the point of render.
        # self.render()  # update graphics and flush any prior clicks
        self.mouse.position = None
        while True:
            if self._is_closed:
                return None
            if self.mouse.position is not None:
                break
            self.update()
            time.sleep(.05)  # allow time for other events to be handled

        click_point = self.mouse.position
        self.mouse.position = None

        return click_point

    def _on_mouse_click(self, event):
        self.mouse._update(event)

    def _on_key_press(self, event):
        self.keyboard._update(event)

#      def add_canvas(self, width=None, height=None, background_color=0):
# FIXME: Set defaults based on the main canvas.
#         new_canvas = RoseCanvas(self, background_color='white')
#         self.widgets.append(new_canvas)
#
#         _root.update()


class RoseWidget():
    """
       A Widget is a thing that one can put on a Window,
       e.g. a Canvas, FortuneTeller, etc.
    """

    def __init__(self, window):
        self._window = window

    def get_window(self):
        return self._window


class RoseCanvas(RoseWidget):
    defaults = {'colors': [None, 'yellow', 'light blue', 'dark grey']}
    count = 0

    """
       A RoseCanvas is a RoseWidget (i.e., a thing on a RoseWindow)
       upon which one can draw shapes and other Drawable things.
    """
    def __init__(self, window, width=200, height=200,
                 background_color=0):
        super().__init__(window)

        RoseCanvas.count = RoseCanvas.count + 1

        # FIXME: Deal with default background colors.
        # FIXME: Store background color as a property
        #        so that modifying it changes the tkinter canvas.
        #        Ditto width and height.


#         if background_color == 0:
#             index = RoseCanvas.count % len(defaults['colors'])
#             self.background_color = defaults['colors'][index]
#         else:
#             self.background_color = background_color

        tk_canvas = tkinter.Canvas(window.toplevel,
                                   width=width, height=height,
                                   background=background_color)
        self._tkinter_canvas = tk_canvas

        # FIXME: Automate gridding better.
        self._tkinter_canvas.grid(padx=5, pady=5)
        self.shapes = []

    def render(self, seconds_to_pause=None):
        """Draws all attached shapes."""
        self._update_shapes()
        self._window.update()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def _renderShape(self, shape, render_NOW=False):
        """Renders a shape."""
        coordinates = shape._get_coordinates_for_drawing()
        options = shape._get_options_for_drawing()

        if shape.shape_id_by_canvas[self] is None:
            draw_method = shape._method_for_drawing(self._tkinter_canvas,
                                                    *coordinates)
            shape.shape_id_by_canvas[self] = draw_method

        try:
            self._tkinter_canvas.coords(shape.shape_id_by_canvas[self],
                                        *coordinates)
        except tkinter.TclError:
            message = "Could not place the shape on the given window.\n"
            message += "Did you accidentally render a closed window?\n"
            raise Exception(message) from None

        self._tkinter_canvas.itemconfigure(shape.shape_id_by_canvas[self],
                                           options)
        if render_NOW:
            # redraw NOW
            self._window.update()

    def _draw(self, shape):
        """Queues a shape for being drawn. Does NOT draw it just yet."""
        if shape not in self.shapes:
            shape.shape_id_by_canvas[self] = None
            self.shapes.append(shape)

    def _undraw(self, shape):
        if shape in self.shapes:
            for i in range(len(self.shapes)):
                if self.shapes[i] is shape:
                    self._tkinter_canvas.delete(shape.shape_id_by_canvas[self])
                    del self.shapes[i]
                    break

    def _update_shapes(self):
        for shape in self.shapes:
            self._renderShape(shape)


class Mouse(object):
    def __init__(self):
        self.position = None

    def _update(self, event):
        self.position = Point(event.x, event.y)


class Keyboard(object):
    def __init__(self):
        self.key_pressed = None

    def _update(self, event):
        self.key_pressed = event.keysym


class __FreezeClass__ (type):
    """Prevents class variable assignment."""
    def __setattr__(self, name, _ignored):  # last parameter is the value
        err = "You tried to set the instance variable '" + name + "'\n"
        err += "   on the CLASS '" + self.__name__ + "'"
        err += ", which is not an OBJECT.\n"
        err += "   Did you forget the () after the word "
        err += self.__name__ + ",\n"
        err += "   on the line where you constructed the object?"
        raise SyntaxError(err)


class _Shape(object, metaclass=__FreezeClass__):
    """
    A Shape is a thing that can be drawn on a RoseCanvas
    (which itself draws on a tkinter Canvas).

    Its constructor provides the tkinter method to be used to
    draw this Shape.

    This abstract type has concrete subclasses that include:
      Arc, Bitmap, Circle, Ellipse, Image, Line, Path, Polygon,
      Rectangle, RoundedRectangle, Square, Text and Window.

    Public data attributes:  None.
    Public methods: attach_to.
    """
    def __init__(self, method_for_drawing):
        """  Arguments:
          -- the tkinter method for drawing the Shape.
        """
        self._method_for_drawing = method_for_drawing
        self.shape_id_by_canvas = {}

    def __eq__(self, other):
        """
        Two Shape objects are equal (==) if all their attributes
        are equal to each other.
        """
        # check before we go deleting keys that may or may not exist
        if(not isinstance(other, self.__class__)):
            return False
        self_dict = self.__dict__.copy()
        other_dict = other.__dict__.copy()
        del self_dict["shape_id_by_canvas"]
        del other_dict["shape_id_by_canvas"]
        return (self_dict == other_dict)

    def __ne__(self, other):
        return not self.__eq__(other)

    def attach_to(self, rose_canvas):
        """
        Attach this Shape to the given RoseCanvas.
        When that RoseCanvas is rendered, this shape will appear
        on that RoseCanvas.
        """
        if type(rose_canvas) == RoseWindow:
            rose_canvas = rose_canvas.initial_canvas
        rose_canvas._draw(self)

    def detach_from(self, rose_canvas):
        """
        Detach this Shape to the given RoseCanvas.
        When that RoseCanvas is rendered, this shape no longer appear
        on that RoseCanvas.
        """
        if type(rose_canvas) == RoseWindow:
            rose_canvas = rose_canvas.initial_canvas
        rose_canvas._undraw(self)


class _ShapeWithOutline(object):
    """
    A Shape that has an interior (which can be filled with a color)
    and an outline (which has a color and thickness).

    This abstract type has concrete subclasses that include:
      Arc, Circle, Ellipse, Image, Line, Path,
      Polygon, Rectangle, Square, Text and Window.

    Public data attributes:  fill_color, outline_color, outline_thickness.
    Public methods:  initialize_options.
    """
    defaults = {'fill_color': None,
                'outline_color': 'black',
                'outline_thickness': 1}

    def initialize_options(self):
        self.fill_color = _ShapeWithOutline.defaults['fill_color']
        self.outline_color = _ShapeWithOutline.defaults['outline_color']
        self.outline_thickness = \
            _ShapeWithOutline.defaults['outline_thickness']

    def _get_options_for_drawing(self):
        options = {'fill': self.fill_color,
                   'outline': self.outline_color,
                   'width': self.outline_thickness}

        # If a color is None, that means transparent here:
        for option in ('fill', 'outline'):
            if not options[option]:
                options[option] = ''

        return options


class _ShapeWithThickness(object):
    """
    A Shape that can be (and almost always is) filled with a color
    and has a thickness but no outline.

    This abstract type has concrete subclasses that include:
      Line and Path.

    Public data attributes:  color, thickness.
    Public methods:  initialize_options.
    """
    defaults = {'color': 'black',
                'thickness': 1}

    def initialize_options(self):
        self.color = _ShapeWithThickness.defaults['color']
        self.thickness = _ShapeWithThickness.defaults['thickness']

    def _get_options_for_drawing(self):
        options = {'fill': self.color,
                   'width': self.thickness}

        # If a color is None, that means 'black' here:
        if options['fill'] is None:
            options['fill'] = 'black'

        return options


class _ShapeWithText(object):
    """
    A Shape that has text and a font for displaying that text.

    This abstract type has concrete subclasses that include:
      Text.

    Public data attributes:  font_family, font_size,
      is_bold, is_italic, is_underline, is_overstrike.

    Public methods:  initialize_options.
    """
    # FIXME: Add more to the above docstring.

    defaults = {'font_family': 'helvetica',
                'font_size': 14,
                'weight':  'normal',
                'slant':  'roman',
                'underline':  0,
                'overstrike':  0,
                'justify': tkinter.CENTER,
                'text_box_width': None,
                'text_color': 'black',
                'text': ''}

    def initialize_options(self):
        self.font_family = _ShapeWithText.defaults['font_family']
        self.font_size = _ShapeWithText.defaults['font_size']
        self.is_bold = _ShapeWithText.defaults['weight'] == 'bold'
        self.is_italic = _ShapeWithText.defaults['slant'] == 'italic'
        self.is_underline = _ShapeWithText.defaults['underline'] == 1
        self.is_overstrike = _ShapeWithText.defaults['overstrike'] == 1

        self.justify = _ShapeWithText.defaults['justify']
        self.text_box_width = _ShapeWithText.defaults['text_box_width']
        self.text_color = _ShapeWithText.defaults['text_color']
        self.text = _ShapeWithText.defaults['text']

    def _get_options_for_drawing(self):
        weight = 'bold' if self.is_bold else 'normal'
        slant = 'italic' if self.is_italic else 'roman'
        underline = 1 if self.is_underline else 0
        overstrike = 1 if self.is_overstrike else 0
        font = tkinter_font.Font(family=self.font_family,
                                 size=self.font_size,
                                 weight=weight,
                                 slant=slant,
                                 underline=underline,
                                 overstrike=overstrike)

        options = {'font': font,
                   'justify': self.justify,
                   'fill': self.text_color,
                   'text': self.text}
        if self.text_box_width:
            options['width'] = self.text_box_width

        return options


class _ShapeWithCenter(_Shape):
    """
    A Shape that has a center (and for which moving its center
    moves the entire Shape).  Its constructor provides the center
    of the Shape along with its method for drawing this Shape.

    This abstract type has concrete subclasses that include:
      Arc, Bitmap, Circle, Ellipse, Image,
      Rectangle, RoundedRectangle, Square, Text and Window.

    Public data attributes: center.
    Public methods: move_by, move_center_to.
    """
    def __init__(self, center, method_for_drawing):
        """
        Arguments:
          -- the Point that is the center of the Shape
               (the Shape stores a CLONE of that Point)
          -- the tkinter method for drawing the Shape.
        """
        # Clone the   center   argument, so that if the caller
        # mutates the argument, it does NOT affect this Shape.
        super().__init__(method_for_drawing)
        self.center = center.clone()

    def move_by(self, dx, dy):
        """
        Moves this Shape dx units in the x-direction and dy units in
        the y-direction,
        """
        self.center.move_by(dx, dy)

    def move_center_to(self, x, y):
        """
        Moves this Shape's center to position (x, y), thus translating
        the entire Shape by however much its center moved.
        """
        self.center.move_to(x, y)


class _RectangularShape(_ShapeWithCenter):
    """
    A Shape determined by its rectangular bounding box
    (plus possibly other information).
    Its constructor provides the opposite corners of the Shape,
    from which the bounding box can be determined.
    Its constructor also provides the method for drawing this Shape.

    This abstract type has concrete subclasses that include:
      Arc, Ellipse, Rectangle and RoundedRectangle.

    Public methods: clone, get_bounding_box.
    """
    def __init__(self, corner_1, corner_2, method_for_drawing):
        super().__init__(Point((corner_2.x + corner_1.x) / 2,
                               (corner_2.y + corner_1.y) / 2),
                         method_for_drawing)

        self.corner_1 = corner_1.clone()
        self.corner_2 = corner_2.clone()

        self._update_corners()

    def __repr__(self):
        string = '{} with corners at ({}, {}), ({}, {})'
        return string.format(self.__class__.__name__,
                             self.corner_1.x,
                             self.corner_1.y,
                             self.corner_2.x,
                             self.corner_2.y)

    def move_by(self, dx, dy):
        self.corner_1.x += dx
        self.corner_1.y += dy
        self.corner_2.x += dx
        self.corner_2.y += dy

    def get_upper_left_corner(self):
        self._update_corners()
        return self._upper_left_corner

    def move_center_to(self, x, y):
        """
        Moves this Shape's center to position (x, y), thus translating
        the entire Shape by however much its center moved.
        """
        width = self.corner_2.x - self.corner_1.x
        height = self.corner_2.y - self.corner_1.y

        self.corner_1.x = x - (width / 2)
        self.corner_1.y = y - (height / 2)
        self.corner_2.x = x + (width / 2)
        self.corner_2.y = y + (height / 2)


#     @upper_left_corner.setter
#     def upper_left_corner(self, point):
#         self.center = Point(point.x + self.width / 2,
#                             point.y + self.height / 2)
#         self._update_corners()

    def get_upper_right_corner(self):
        self._update_corners()
        return self._upper_right_corner

#     @upper_right_corner.setter
#     def upper_right_corner(self, point):
#         self.center = Point(point.x - self.width / 2,
#                             point.y + self.height / 2)
#         self._update_corners()

    def get_lower_left_corner(self):
        self._update_corners()
        return self._lower_left_corner

#     @lower_left_corner.setter
#     def lower_left_corner(self, point):
#         self.center = Point(point.x + self.width / 2,
#                             point.y - self.height / 2)
#         self._update_corners()

    def get_lower_right_corner(self):
        self._update_corners()
        return self._lower_right_corner

#     @lower_right_corner.setter
#     def lower_right_corner(self, point):
#         self.center = Point(point.x - self.width / 2,
#                             point.y - self.height / 2)
#         self._update_corners()

    def _update_corners(self):
        min_x = min(self.corner_1.x, self.corner_2.x)
        min_y = min(self.corner_1.y, self.corner_2.y)
        max_x = max(self.corner_1.x, self.corner_2.x)
        max_y = max(self.corner_1.y, self.corner_2.y)

        self._upper_left_corner = Point(min_x, min_y)
        self._upper_right_corner = Point(max_x, min_y)
        self._lower_left_corner = Point(min_x, max_y)
        self._lower_right_corner = Point(max_x, max_y)

    def clone(self):
        return self.__class__(self.corner_1.clone(), self.corner_2.clone())

    def get_bounding_box(self):
        return self.clone()

    def _get_coordinates_for_drawing(self):
        return [self.get_upper_left_corner().x,
                self.get_upper_left_corner().y,
                self.get_lower_right_corner().x,
                self.get_lower_right_corner().y]


class Arc(_RectangularShape, _ShapeWithOutline):
    """ Not yet implemented. """


class Bitmap(_Shape):
    """ Not yet implemented. """


class Circle(_ShapeWithCenter, _ShapeWithOutline):
    """
    A Shape that is a Circle.
    Its constructor specifies its center and radius,
    as well as the method for drawing this Shape.

    Public data attributes: center, radius, fill_color,
                            outline_color, outline_thickness.
    Public methods: attach_to, move_by, move_center_to,
                    clone, get_bounding_box.
    """
    def __init__(self, center, radius):
        super().__init__(center, tkinter.Canvas.create_oval)
        super().initialize_options()

        self.radius = radius

    def __repr__(self):
        string = 'Circle with center at ({}, {}) and radius {})'
        return string.format(self.center.x, self.center.y,
                             self.radius)

    def clone(self):
        return Circle(self.center, self.radius)

    def get_bounding_box(self):
        c1 = Point(self.center.x - self.radius, self.center.y - self.radius)
        c2 = Point(self.center.x + self.radius, self.center.y + self.radius)
        return Rectangle(c1, c2)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box()._get_coordinates_for_drawing()


class Ellipse(_RectangularShape, _ShapeWithOutline):
    """
    A Shape that is an Ellipse (aka oval).  Its constructor
    specifies the opposite corners
    of its bounding box, as well as the method for drawing this Shape.

    Public data attributes: corner_1, corner_2, fill_color,
                            outline_color, outline_thickness.
    Public methods: attach_to, move_by, move_center_to,
                    get_bounding_box.
    """
    def __init__(self, corner_1, corner_2):
        super().__init__(corner_1, corner_2,
                         tkinter.Canvas.create_oval)
        super().initialize_options()


class Line(_Shape, _ShapeWithThickness):
    """
    A Shape that is a Line (more precisely, a line segment).
    Its constructor specifies its start and end points,
    as well as the method for drawing this Shape.

    Public data attributes: arrow, start, end, color, thickness.
    Public methods: attach_to, clone, move_by, get_midpoint.
    """

    defaults = {'arrow': None}

    def __init__(self, start, end):
        super().__init__(tkinter.Canvas.create_line)
        self.initialize_options()

        self.start = start.clone()
        self.end = end.clone()

    def initialize_options(self):
        super().initialize_options()
        self._arrow = Line.defaults['arrow']

    def _get_options_for_drawing(self):
        options = super()._get_options_for_drawing()
        if self._arrow is not None:
            options["arrow"] = self._arrow
        return options

    def __repr__(self):
        string = 'Line from ({}, {}) to ({}, {}))'
        return string.format(self.start.x, self.start.y,
                             self.end.x, self.end.y)

    def clone(self):
        return Line(self.start, self.end)

    def move_by(self, delta_x, delta_y):
        self.start.move_by(delta_x, delta_y)
        self.end.move_by(delta_x, delta_y)

    def get_midpoint(self):
        return Point((self.start.x + self.end.x) // 2,
                     (self.start.y + self.end.y) // 2)

    # Begin arrow definition.

    # Mark: you MUST use this form to declare properties to get Eclipse
    # to treat it like a variable.  It appears that if you use
    # the decorators (@ property and @ arrow.setter),
    # Eclipse will INCORRECTLY think it is a method and autocomplete
    # it with () at the end.  Maybe PyDev/Eclipse will fix this someday.

    def __get_arrow(self):
        """ Use .arrow= instead. """
        return self._arrow

    def __set_arrow(self, value):
        """ Use .arrow= instead. """
        self._arrow = value

    def __del_arrow(self):
        """ Use delete var.arrow instead. """
        del self._arrow

    arrow = property(__get_arrow, __set_arrow, __del_arrow, """
    This PROPERTY gets or sets the arrow head on the line.
    Valid options include:
        -- None
        -- "first"
        -- "last"
        -- "both"
        """)
    # End arrow.

    def _get_coordinates_for_drawing(self):
        return [self.start.x,
                self.start.y,
                self.end.x,
                self.end.y]


class Path(_Shape, _ShapeWithThickness):
    """ Not yet implemented. """


class Point(_Shape, _ShapeWithOutline):
    """
    A Shape that describes a coordinate in two-dimensional space.
    Its constructor specifies its x and y.

    Public data attributes: x, y.
    Public methods: clone, move_by, move_to.
    """
    defaults = {'width_for_drawing': 10,
                'height_for_drawing': 10,
                'fill_color': 'red'}

    def __init__(self, x, y):
        super().__init__(tkinter.Canvas.create_oval)
        super().initialize_options()

        self.x = x
        self.y = y

        self.width_for_drawing = Point.defaults['width_for_drawing']
        self.height_for_drawing = Point.defaults['height_for_drawing']
        self.fill_color = Point.defaults['fill_color']

    def __repr__(self):
        return 'Point at ({}, {})'.format(self.x, self.y)

    def clone(self):
        return Point(self.x, self.y)

    def move_by(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def get_bounding_box(self):
        c1 = Point(self.x - self.width_for_drawing / 2,
                   self.y - self.width_for_drawing / 2)
        c2 = Point(self.x + self.height_for_drawing / 2,
                   self.y + self.height_for_drawing / 2)
        return Rectangle(c1, c2)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box()._get_coordinates_for_drawing()


class Polygon(_Shape, _ShapeWithOutline):
    """ Not yet implemented. """


class Rectangle(_RectangularShape, _ShapeWithOutline):
    """
    A Shape that is a Rectangle.  Its constructor specifies
    the opposite corners of the rectangle.

    Public data attributes: corner_1, corner_2, fill_color,
                            outline_color, outline_thickness.
    Public methods: attach_to, clone,
                    move_by, move_center_to,
                    get_bounding_box,
                    get_upper_left_corner,
                    get_upper_right_corner,
                    get_lower_left_corner,
                    get_lower_right_corner.
    """
    def __init__(self, corner_1, corner_2):
        super().__init__(corner_1, corner_2,
                         tkinter.Canvas.create_rectangle)
        super().initialize_options()

    def get_bounding_box(self):
        return self.clone()


class RoundedRectangle(_RectangularShape, _ShapeWithOutline):
    """ Not yet implemented. """


class Square(_ShapeWithCenter, _ShapeWithOutline):
    """
    A Shape that is a Square.
    Its constructor specifies its center and the length of each side,
    as well as the method for drawing this Shape.

    Public data attributes: center, length_of_each_side, fill_color,
                            outline_color, outline_thickness.
    Public methods: attach_to, move_by, move_center_to,
                    clone, get_bounding_box.
    """
    def __init__(self, center, length_of_each_side):
        super().__init__(center, tkinter.Canvas.create_rectangle)
        super().initialize_options()

        self.length_of_each_side = length_of_each_side

    def __repr__(self):
        string = 'Square with center at ({}, {}) and length of each side {})'
        return string.format(self.center.x, self.center.y,
                             self.length_of_each_side)

    def clone(self):
        return Square(self.center, self.length_of_each_side)

    def get_bounding_box(self):
        c1 = Point(self.center.x - self.length_of_each_side / 2,
                   self.center.y - self.length_of_each_side / 2)
        c2 = Point(self.center.x + self.length_of_each_side / 2,
                   self.center.y + self.length_of_each_side / 2)
        return Rectangle(c1, c2)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box()._get_coordinates_for_drawing()


class Text(_ShapeWithCenter, _ShapeWithText):
    """
    A Shape that has a string of text on it, displayed horizontally.

    Its constructor specifies the rg.Point at which the text
    is centered and the string that is to be displayed.

    Public data attributes: center (an rg.Point),
      font_size (an integer, 5 to 80 or so are reasonable values),
      is_bold (True if the text is to be displayed in BOLD, else False),
      is_italic (True or False),
      is_underline (True or False),
      is _overstrike (True or False),
      text_color (color used to display the text, default is 'black')
      text (the string to be displayed).
    Public methods: attach_to, move_by, move_center_to.
    """
    def __init__(self, center, text):
        """
        The first argument must be a rg.Point.
        The second argument must be a string.

        When this Text object is rendered on a window,
        the string (2nd argument) is drawn horizontally on the window,
        centered at the rg.Point that is the 1st argument.

        Preconditions:
           :type center: rg.Point
           :type text str
        """
        super().__init__(center, tkinter.Canvas.create_text)
        super().initialize_options()

        self.text = text

        # FIXME: Allow __init__ to set the options.

    def __repr__(self):
        return "Text displaying '{}' at position {}".format(self.text,
                                                            self.center)

    # FIXME: Have repr include characteristics??
    # FIXME: Do a clone?

#     def clone(self):
#         return Square(self.center, self.length_of_each_side)

#     def get_bounding_box(self):
#         return Rectangle(self.center,
#                          2 * self.length_of_each_side,
#                          2 * self.length_of_each_side)

# FIXME: Implement bounding_box using the tkinter function for it.

    def _get_coordinates_for_drawing(self):
        return [self.center.x, self.center.y]

# Mark: Window/RoseWindow naming collision is causing mass confusion.
# class Window(_Shape):
#    """ Not yet implemented. """
#    default_options = {}


# CONSIDER: Are these right for here?
class Button(_Shape):
    """ Not yet implemented. """
    default_options = {}


class Entry(_Shape):
    """ Not yet implemented. """
    default_options = {}


class Color(object):
    """
    A Color represents a  fill or outline color created from
    custom amounts of red, green, and blue light. The arguments are:
      - The RED component (0-255),
      - the GREEN component (0-255),
      - the BLUE component (0-255).

    This Color can be passed to RoseGraphics colors
    such as fill_color and outline_color.
    """

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return "#{:02x}{:02x}{:02x}".format(self.red,
                                            self.green,
                                            self.blue)


def main():
    # Test whether Point.x gives an error.
    #   print("Point.x=5 should give an error")
    #   Point.x = 5

    """ Demonstrates some of the features of this module. """
    w = RoseWindow(500, 300, 'hello')
    w.close_on_mouse_click()
    window1 = RoseWindow(title='An empty window',
                         make_initial_canvas=False)

    window1.close_on_mouse_click()

    window2 = RoseWindow(500, 300, 'Blue window with yellow canvas',
                         # Mark: I assume most students won't use this.
                         # window_color='blue',
                         canvas_color='yellow')

    center = Point(300, 100)
    circle = Circle(center, 40)
    circle.attach_to(window2.initial_canvas)
    circle.fill_color = 'red'
    window2.render(1)
    circle.fill_color = ''
    print("Emptied the fill color.")
    print(window2.width, window2.height)
    window2.render()
    window2.get_next_mouse_click()

    center.move_by(-200, -50)
    circle = Circle(center, 70)
    circle.attach_to(window2.initial_canvas)
    circle.fill_color = None

    print(window2.width, window2.height)
    window2.render()
    window2.get_next_mouse_click()
    # return

    window3 = RoseWindow()

    p1 = Point(100, 50)
    p2 = Point(200, 90)

    rect = Rectangle(p1, p2)
    rect.attach_to(window2.initial_canvas)
    rect.attach_to(window3.initial_canvas)

    window2.render(1)
    window3.render(1)

    rect.fill_color = 'red'
    center.attach_to(window3.initial_canvas)

    window2.render(1)
    window3.render(1)

    center.move_by(50, 0)
    window3.render(1)

    window2.close_on_mouse_click()
    window3.close_on_mouse_click()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
