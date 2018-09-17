from toga import GROUP_BREAK, SECTION_BREAK
from travertino.layout import Viewport

from .libs import WPF, add_handler


class WPFViewport:
    def __init__(self, native):
        self.native = native
        self.dpi = 96  # FIXME This is almost certainly wrong...

    @property
    def width(self):
        return self.native.Width

    @property
    def height(self):
        return self.native.Height


class Window:
    def __init__(self, interface):
        self.interface = interface
        self.interface._impl = self
        self.create()

    def create(self):
        self.native = WPF.Window(self)
        self.native.Width, self.native.Height = self.interface._size
        self.native.Content = WPF.Controls.Canvas()
        self.native.Content.Background = WPF.Media.Brushes.LightSteelBlue
        self.native.SizeChanged += self.wpf_Resize
        self.toolbar_native = None
        self.toolbar_items = None

    def create_toolbar(self):
        pass

    def set_position(self, position):
        pass

    def set_size(self, size):
        self.native.Width, self.native.Height = self.interface._size
        self.native.Content.Width, self.native.Content.Height = self.interface._size

    def set_app(self, app):
        pass

    def set_content(self, widget):
        self.native.Content.Children.Add(widget.native)

        # Set the widget's viewport to be based on the window's content.
        widget.viewport = WPFViewport(self.native)

        # Add all children to the content widget.
        for child in widget.interface.children:
            child._impl.container = widget

    def set_title(self, title):
        self.native.Title = title

    def show(self):
        self.interface.content._impl.rehint()
        self.interface.content.style.layout(self.interface.content, Viewport(0, 0))
        self.native.MinWidth = int(self.interface.content.layout.width)
        self.native.MinHeight = int(self.interface.content.layout.height)

        self.interface.content.refresh()
        if self.interface is self.interface.app._main_window:
            self.native.Closing += self.wpf_Closing

        if self.interface is not self.interface.app._main_window:
            self.native.Show()

    def wpf_Closing(self, event, handler):
        if self.interface.app.on_exit:
            self.interface.app.on_exit(self.interface.app)

    def set_full_screen(self, is_full_screen):
        self.interface.factory.not_implemented('Window.set_full_screen()')

    def on_close(self):
        pass

    def close(self):
        self.native.Close()

    def wpf_Resize(self, sender, args):
        if self.interface.content:
            # Re-layout the content
            self.interface.content.refresh()
