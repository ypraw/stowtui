#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from typing import List

from template_interface.FileManagerTui import FileManagerTUI


class StowApp(npyscreen.NPSAppManaged):

    def onStart(self):
        quit_s = '\t' * 4 + '^Q to quit'

        self.addForm(
            "MAIN",
            FileManagerTUI,
            name='Stow ' + quit_s,
        )


if __name__ == "__main__":
    npyscreen.wrapper(StowApp().run())
