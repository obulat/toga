from travertino.size import at_least
from toga_wpf.libs import WPF
from .base import Widget


class Button(Widget):
    def create(self):
        self.native = WPF.Controls.Button()
        self.native.Click += self.wpf_on_click
        self.set_enabled(self.interface._enabled)

    def wpf_on_click(self, sender, event):
        if self.interface.on_press:
            self.interface.on_press(self.interface)

    def set_label(self, label):
        self.native.Content = self.interface.label
        self.rehint()

    def set_enabled(self, value):
        self.native.IsEnabled = self.interface._enabled

    def set_on_press(self, handler):
        # No special handling required
        pass

    def set_background_color(self, value):
        self.interface.factory.not_implemented('Button.set_background_color()')

    def rehint(self):

        if self.native and self.interface._window:
            wpf_size = WPF.Size(self.interface._window._size[0], self.interface._window._size[1])
            self.native.Measure(wpf_size)
            self.interface.intrinsic.height = int(self.native.DesiredSize.Height)
