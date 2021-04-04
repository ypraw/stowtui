import npyscreen
import os
import sys
import time
from .DotfilesDirectories import DotfilesDirectoriesList


class FileManagerTUI(npyscreen.ActionForm):
    """
    ---------
    File Manager UI
    ---------
    File Manager module.
    UI Template for File Manager target directory and dotfiles directory.
    This UI will be rendered the first time the program is run.
    """
    OK_BUTTON_TEXT = 'Process'
    CANCEL_BUTTON_TEXT = 'Exit'
    CANCEL_BUTTON_BR_OFFSET = (1, 15)
    OK_BUTTON_BR_OFFSET = (1, 6)

    @staticmethod
    def exit(*args, **kwargs):
        os.system('reset')
        os.system('stty sane')
        try:
            sys.exit(0)
        except SystemExit:  # pragma: no cover
            os._exit(0)

    def create(self):
        self.add_handlers({'^Q': FileManagerTUI.exit})
        self.add(npyscreen.Textfield,
                 value='NOTES:',
                 editable=False,
                 color='CONTROL')

        self.nextrely += 1

        self.add(
            npyscreen.Textfield,
            value='Target Directory is target to DIR (default is parent of stow dir) <ex, /home/$USER>',
            editable=False,
            color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value='Dotfiles Directory is Dotfiles config directory <ex, /home/$USER/dotfiles>',
            editable=False,
            color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value='set Dotfiles Directory path returned list of all directories config <ex, /home/$USER/dotfiles/zsh>',
            editable=False,
            color='CONTROL')

        self.nextrely += 3

        self.target_directory = self.add(npyscreen.TitleFilename,
                                         name="Target Directory:",
                                         label=True)
        self.dotfiles_directory = self.add(npyscreen.TitleFilename,
                                           name="Dotfiles Directory:",
                                           Label=True)

    def on_ok(self):
        prev_s = '\t' * 4 + '^W to back previous menu'
        quit_s = '\t' * 4 + '^Q to quit'
        if self.dotfiles_directory.value is None:
            npyscreen.notify(
                'Dotfiles Directory Cannot Be NUll', title='Error')
            time.sleep(1)
            self.parentApp.setNextForm("MAIN")

        else:
            result_args = {'dotfiles_path': self.dotfiles_directory.value}
            self.parentApp.addForm("directorieslist",
                                   DotfilesDirectoriesList,
                                   name="List of Directories" + quit_s + prev_s,
                                   **result_args)
            self.parentApp.switchForm("directorieslist")

    def on_cancel(self):
        self.exit()
