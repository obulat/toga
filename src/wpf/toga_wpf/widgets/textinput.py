from toga_wpf.libs import WPF
from travertino.size import at_least

from .base import Widget


class TextInput(Widget):
    def create(self):
        self.native = WPF.Controls.TextBox()
        self.native.TextChanged += self.wpf_on_change

    def set_readonly(self, value):
        self.native.IsReadOnly = value

    def set_placeholder(self, value):
        self.native.Text = self.interface.placeholder

    def get_value(self):
        return self.native.Text

    def set_value(self, value):
        self.native.Text = value

    def set_alignment(self, value):
        self.interface.factory.not_implemented('TextInput.set_alignment()')

    def set_font(self, value):
        self.interface.factory.not_implemented('TextInput.set_font()')

    def rehint(self):
        self.interface.intrinsic.width = at_least(self.interface.MIN_WIDTH)
        self.interface.intrinsic.height = at_least(20)

    def set_on_change(self, handler):
        pass

    def wpf_on_change(self, sender, event):
        if self.interface._on_change:
            self.interface.on_change(self.interface)
