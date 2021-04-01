import npyscreen
import os
import sys
from typing import List, Dict
from stowtui_core import StowtuiCore


class DotfilesDirectoriesList(npyscreen.ActionForm):
    """
    ---------
    Dotfiles Directories List UI
    ---------

    Dotfiles Directories list module.

    ui Template for generated results from the list directories of
    Dotfiles Directory

    """
    resCheckbox: Dict[str, str] = {}

    def __init__(self, dotfiles_path=None, **kwargs):
        self.settings = locals()
        self.settings.update(kwargs)
        self.settings['dotfiles_path'] = dotfiles_path
        super(DotfilesDirectoriesList, self).__init__(**kwargs)

    @staticmethod
    def exit(**kwargs):
        os.system('reset')
        os.system('stty sane')
        try:
            sys.exit(0)
        except SystemExit:  # pragma: no cover
            os._exit(0)

    @staticmethod
    def _get_list_name(pathDir: str):
        """This is static method for get all list name on target directory

        Args:
            pathDir (str): path to directory location, exp: ~/mydotfiles

        Returns:
            (List[str]): [list directory name from target directory]"""

        dirsName: List[str] = StowtuiCore.getAllDir(pathDir)
        return dirsName

    def create(self):
        self.res = self.add(npyscreen.TitleMultiSelect,
                            max_height=-2,
                            name="List Directories Name",
                            values=self._get_list_name(
                                self.settings['dotfiles_path']),
                            scroll_exit=True)

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

    def on_ok(self):
        self.exit()
