import npyscreen
from typing import List
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

    def create(self):
        self.dotfiles_directory = self.add(
            npyscreen.TitleMultiSelect,
            max_height=-2,
            value=[
                1,
            ],
            name="List Directories Name",
            # values=self._get_list_name(self.dotfiles_directory_result.value),
            scroll_exit=True)

    def on_ok(self):
        # result_folder_form = self.parentApp.getForm("directory_list")
        # result_folder_form.target_directory_result = self.target_directory
        # result_folder_form.dotfiles_directory_result = self.dotfiles_directory
        # # self.parentApp.switchForm(directory_list)
        self.exit()
