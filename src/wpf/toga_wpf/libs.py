import clr

clr.AddReference(r"wpf\PresentationFramework")

import System.Windows as WPF
from System import Threading


def add_handler(cmd):
    action = cmd.action

    def handler(sender, event):
        return action(None)

    return handler
