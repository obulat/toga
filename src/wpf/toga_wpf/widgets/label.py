from travertino.size import at_least

from toga_wpf.libs import WPF

from .base import Widget


class Label(Widget):
    def create(self):
        self.native = WPF.Controls.Label()

    def set_alignment(self, value):
        pass

    def set_text(self, value):
        self.native.Content = self.interface._text

    def rehint(self):
        self.interface.intrinsic.width = at_least(20)
        self.interface.intrinsic.height = at_least(20)
