import npyscreen
import os
import sys
import time
from pathlib import Path
from stowtui.template_interface.DotfilesDirectories import DotfilesDirectoriesList
from stowtui.stowtui_core.stowtui_core import StowtuiCore
from stowtui.helpers.meta import Version
from stowtui.helpers.meta import Author
from stowtui.helpers.meta import Email
from stowtui.helpers.meta import app_name


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
    USER_HOME = str(Path.home())
    CURRENT_DIR = os.getcwd()

    ABOUT_AUTHOR = Author()
    ABOUT_VERSION = Version()
    ABOUT_EMAIL = Email()
    ABOUT_NAME = app_name()
    ABOUT_MESSAGES = 'AUTHOR\t' + ABOUT_AUTHOR + '\nVERSION\t' \
                        + ABOUT_VERSION + '\nEMAIL\t' + ABOUT_EMAIL

    @staticmethod
    def exit(*args, **kwargs):
        os.system('reset')
        os.system('stty sane')
        try:
            sys.exit(0)
        except SystemExit:    # pragma: no cover
            os._exit(0)

    def about_form(self, *args, **kwargs):
        npyscreen.notify_confirm(self.ABOUT_MESSAGES,
                                 title='About ' + self.ABOUT_NAME)
        self.parentApp.setNextForm("MAIN")

    def create(self):
        self.add_handlers({'^A': self.about_form})
        self.add_handlers({'^Q': self.exit})
        self.add(npyscreen.Textfield,
                 value='NOTES:',
                 editable=False,
                 color='CONTROL')

        self.nextrely += 1

        self.add(
            npyscreen.Textfield,
            value=
            'Target Directory is target to DIR (default is parent of stow dir) <ex, /home/$USER>',
            editable=False,
            color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value=
            'Dotfiles Directory is Dotfiles config directory <ex, /home/$USER/dotfiles>',
            editable=False,
            color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value=
            'set Dotfiles Directory path returned list of all directories config <ex, /home/$USER/dotfiles/zsh>',
            editable=False,
            color='CONTROL')

        self.nextrely += 3

        self.target_directory = self.add(npyscreen.TitleFilename,
                                         name="Target Directory:",
                                         label=True,
                                         value=self.USER_HOME + '/')
        self.dotfiles_directory = self.add(npyscreen.TitleFilename,
                                           name="Dotfiles Directory:",
                                           Label=True,
                                           value=self.CURRENT_DIR + '/')

    def on_ok(self):
        prev_s = '\t' * 4 + '^W to back previous menu'
        quit_s = '\t' * 4 + '^Q to quit'
        treeDir = StowtuiCore.getAllDir(self.dotfiles_directory.value)
        result_args = {
            'dotfiles_path': self.dotfiles_directory.value,
            'target_path': self.target_directory.value
        }

        if self.dotfiles_directory.value is None:
            npyscreen.notify('Dotfiles Directory Cannot Be NUll', title='Error')
            time.sleep(1)
            self.parentApp.setNextForm("MAIN")

        elif not treeDir:
            npyscreen.notify_confirm('Directories Child Can not be Empty',
                                     title='Dotfiles Empty',
                                     form_color='DANGER')

            self.parentApp.setNextForm("MAIN")
        else:
            self.parentApp.addForm("directorieslist",
                                   DotfilesDirectoriesList,
                                   name="List of Directories" + quit_s + prev_s,
                                   **result_args)
            self.parentApp.switchForm("directorieslist")

    def on_cancel(self):
        self.exit()
