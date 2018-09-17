from toga_wpf.libs import WPF

from .base import Widget


class Box(Widget):
    def create(self):
        self.native = WPF.Controls.Canvas()
        self.native.interface = self.interface

    def set_bounds(self, x, y, width, height):
        if self.native:
            self.native.Width, self.native.Height = width, height
            if self.interface.parent and self.interface.parent._impl:
                self.interface.parent._impl.native.SetTop(self.native, y)
                self.interface.parent._impl.native.SetLeft(self.native, x)
