import sys

import toga

from .libs import Threading, WPF, add_handler
from .window import Window


class MainWindow(Window):
    def on_close(self):
        pass


class App:
    _MAIN_WINDOW_CLASS = MainWindow

    def __init__(self, interface):
        self.interface = interface
        self.interface._impl = self

    def create(self):
        self.native = WPF.Application()

        # Call user code to populate the main window
        self.interface.startup()

    def create_menus(self):
        self.interface.factory.not_implemented("[WPF] Create menus")

    def open_document(self, fileURL):
        '''Add a new document to this app.'''
        print("STUB: If you want to handle opening documents, implement App.open_document(fileURL)")

    def run_app(self):
        self.create()
        self.native.Run(self.interface.main_window._impl.native)

    def main_loop(self):
        thread = Threading.Thread(Threading.ThreadStart(self.run_app))
        thread.SetApartmentState(Threading.ApartmentState.STA)
        thread.Start()
        thread.Join()

    def exit(self):
        self.native.Exit()

    def set_on_exit(self, value):
        pass
