from travertino.size import at_least

from toga_wpf.libs import WPF

from .base import Widget


class Label(Widget):
    def create(self):
        self.native = WPF.Controls.Label()

    def set_alignment(self, value):
        self.interface.factory.not_implemented('Label.set_alignment()')

    def set_text(self, value):
        self.native.Content = self.interface._text

    def rehint(self):
        if self.native and self.interface._window:
            window_size = WPF.Size(self.interface._window._size[0], self.interface._window._size[1])
            self.native.Measure(window_size)
            self.interface.intrinsic.width = int(self.native.DesiredSize.Width)
            self.interface.intrinsic.height = int(self.native.DesiredSize.Height)
