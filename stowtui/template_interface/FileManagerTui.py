"""
---------
File Manager UI
---------

File Manager module.

UI Template for File Manager target directory and dotfiles directory.
This UI will be rendered the first time the program is run.
"""

import npyscreen


class FileManagerTUI(npyscreen.ActionFormMinimal):

    def __init__(self, *args, **keywords):
        super(FileManagerTUI, self).__init__(*args, **keywords)

    def activate(self):
        self.edit()
        self.parentApp.setNextForm("directory_list")

    def create(self):
        self.value = None
        self.target_directory = self.add(npyscreen.TitleFilenameCombo,
                                         name="Target Directory:",
                                         label=True)
        self.dotfiles_directory = self.add(npyscreen.TitleFilenameCombo,
                                           name="Dotfiles Directory:",
                                           Label=True)

    def on_ok(self):
        result_folder_form = self.parentApp.getForm("directory_list")
        result_folder_form.target_directory_result.value = self.target_directory.value
        result_folder_form.dotfiles_directory_result.value = self.dotfiles_directory.value
        self.parentApp.switchForm("directory_list")