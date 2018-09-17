class Widget:
    def __init__(self, interface):
        self.interface = interface
        self.interface._impl = self

        self._container = None
        self.native = None
        self.create()
        # self.interface.style.reapply()

    def set_app(self, app):
        pass

    def set_window(self, window):
        pass

    @property
    def container(self):
        return self._container

    @container.setter
    def container(self, container):
        self._container = container
        if self.native:
            self._container.native.Children.Add(self.native)

        for child in self.interface.children:
            child._impl.container = container
        self.rehint()

    def set_enabled(self, value):
        if self.native:
            self.native.IsEnabled = self.interface.enabled

    ### APPLICATOR

    def set_bounds(self, x, y, width, height):
        if self.native:
            self.native.Width, self.native.Height = width, height
            if self.interface.parent and self.interface.parent._impl:
                self.interface.parent._impl.native.SetTop(self.native, y)
                self.interface.parent._impl.native.SetLeft(self.native, x)

    def set_alignment(self, alignment):
        # By default, alignment can't be changed
        pass

    def set_hidden(self, hidden):
        if self.native:
            self.native.Visible = not hidden

    def set_font(self, font):
        # By default, font can't be changed
        pass

    def set_color(self, color):
        # By default, color can't be changed
        pass

    def set_background_color(self, color):
        # By default, background color can't be changed.
        pass

    ### INTERFACE

    def add_child(self, child):
        if self.container:
            child.container = self.container

    def rehint(self):
        pass
