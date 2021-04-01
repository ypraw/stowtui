#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from typing import List

from stowtui.template_interface.DotfilesDirectories import DotfilesDirectoriesList
from stowtui.template_interface.FileManagerTui import FileManagerTUI


class StowApp(npyscreen.NPSAppManaged):

    def onStart(self):
        self.addForm("MAIN", FileManagerTUI, name="Welcome to STOW TUI")
        self.addForm("directory_list",
                     DotfilesDirectoriesList,
                     name="List Of Dotfiles")


if __name__ == "__main__":
    # App = StowApp()
    # App.run()
    npyscreen.wrapper(StowApp().run())