#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from stowtui_core import StowtuiCore
from typing import List


class FileManagerTUI(npyscreen.ActionForm):
    """
    ---------
    File Manager UI
    ---------

    File Manager module.

    UI Template for File Manager target directory and dotfiles directory.
    This UI will be rendered the first time the program is run.
    """

    @staticmethod
    def _get_list_name(pathDir: str):
        """This is static method for get all list name on target directory

        Args:
            pathDir (str): path to directory location, exp: ~/mydotfiles

        Returns:
            (List[str]): [list directory name from target directory]"""

        dirsName: List[str] = StowtuiCore.getAllDir(pathDir)
        return dirsName

    def activate(self):
        self.edit()
        self.parentApp.setNextForm("directory_list")

    def create(self):
        self.target_directory = self.add(
            npyscreen.TitleFileNameCombo,
            name="Target Directory:",
        )
        self.dotfiles_directory = self.add(
            npyscreen.TitleFileNameCombo,
            name="Dotfiles Directory:",
        )

    def on_ok(self):
        result_folder_form = self.parentApp.getForm("directory_list")
        result_folder_form.target_directory_result = self.target_directory
        result_folder_form.dotfiles_directory_result = self.dotfiles_directory
        self.parentApp.switchForm(directory_list)


class DotfilesDirectoriesList(npyscreen.ActionForm):
    """
    ---------
    Dotfiles Directories List UI
    ---------

    Dotfiles Directories list module.

    ui Template for generated results from the list directories of
    Dotfiles Directory

    """

    def activate(self):
        self.edit()

    def create(self):
        self.target_directory = self.add(
            npyscreen.TitleFileNameCombo,
            name="Target Directory:",
        )
        self.dotfiles_directory = self.add(
            npyscreen.TitleFileNameCombo,
            name="Dotfiles Directory:",
        )

    def on_ok(self):
        result_folder_form = self.parentApp.getForm("directory_list")
        result_folder_form.target_directory_result = self.target_directory
        result_folder_form.dotfiles_directory_result = self.dotfiles_directory
        self.parentApp.switchForm(directory_list)


class StowApp(npyscreen.NPSApp):

    @staticmethod
    def _get_list_name(pathDir: str):
        dirsName = StowtuiCore.getAllDir(pathDir)
        return dirsName

    def main(self):
        F = npyscreen.Form(name="Welcome to Stow TUI")

        fn = F.add(
            npyscreen.TitleFilenameCombo,
            name="Target Directory:",
        )
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Dotfiles Directory:")
        ms2 = F.add(npyscreen.TitleMultiSelect,
                    max_height=-2,
                    value=[
                        1,
                    ],
                    name="List Directories Name",
                    values=self._get_list_name(
                        '/home/ypraw/Programming/linux/configDotfiles'),
                    scroll_exit=True)

        # This lets the user play with the Form.
        F.edit()


if __name__ == "__main__":
    App = StowApp()
    App.run()
