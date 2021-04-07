import npyscreen
import time
import os
import sys
import threading
from typing import List, Dict
from stowtui.stowtui_core.stowtui_core import StowtuiCore


class DotfilesDirectoriesList(npyscreen.ActionForm):
    """
    ---------
    Dotfiles Directories List UI
    ---------

    Dotfiles Directories list module.

    ui Template for generated results from the list directories of
    Dotfiles Directory

    """
    CANCEL_BUTTON_TEXT = 'Previous Menu'

    resCheckbox: Dict[str, str] = {}

    def __init__(self, dotfiles_path=None, target_path=None, **kwargs):
        self.settings = locals()
        self.settings.update(kwargs)
        self.settings['dotfiles_path'] = dotfiles_path
        self.settings['target_path'] = target_path
        super(DotfilesDirectoriesList, self).__init__(**kwargs)

    @staticmethod
    def exit(*args, **kwargs):
        os.system('reset')
        os.system('stty sane')
        try:
            sys.exit(0)
        except SystemExit:  # pragma: no cover
            os._exit(0)

    def create(self):
        prev_s = '\t' * 4 + '^W to back previous menu'
        quit_s = '\t' * 4 + '^Q to quit'

        self.add_handlers({'^Q': self.exit})
        self.add_handlers({'^W': self.on_cancel})

        self.add(npyscreen.Textfield,
                 value='NOTES:',
                 editable=False,
                 color='CONTROL')

        self.nextrely += 1

        self.add(
            npyscreen.Textfield,
            value='Make Sure that the folders is your dotfiles config',
            editable=False,
            color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value='An Exampale, your config is ~/dotfiles/zsh which contain, ',
            editable=False,
            color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value='-/zsh',
            editable=False,
            color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value='\t - .zshrc',
            editable=False,
            color='CONTROL')

        self.nextrely += 1

        self.add(
            npyscreen.Textfield,
            value='IF Not you can switch to previous menu',
            editable=False,
            color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value='by pressing button cancel or use shortcut ^W',
            editable=False,
            color='CONTROL')

        self.nextrely += 3

        self.add(
            npyscreen.Textfield,
            value='Your Current Path : ',
            editable=False,
        )

        self.add(
            npyscreen.Textfield,
            value=self.settings['dotfiles_path'],
            editable=False,
        )
        self.add(
            npyscreen.Textfield,
            value='Your Target Path : ',
            editable=False,
        )

        self.add(
            npyscreen.Textfield,
            value=self.settings['target_path'],
            editable=False,
        )

        self.nextrely += 1

        self.res = self.add(npyscreen.TitleMultiSelect,
                            max_height=-2,
                            name="List Directories Name",
                            values=StowtuiCore.getAllDir(
                                self.settings['dotfiles_path']),
                            scroll_exit=True)

    def on_cancel(self, *args, **kwargs):
        self.parentApp.switchFormPrevious()

    def on_ok(self, **kwargs):
        def popup(thrd, title):
            """
            Start the thread and display a popup of the plugin being cloned
            until the thread is finished
            """
            thrd.start()
            message_info = "Restoring..."
            npyscreen.notify_wait(message_info, title=title)
            while thrd.is_alive():
                time.sleep(1)
            return

        target_dir = self.settings['target_path']
        dotfiles_dir = self.settings['dotfiles_path']
        selectable_values = self.res.get_selected_objects()

        if (selectable_values is None):
            npyscreen.notify_confirm('Target Configs can not be null, please checklist at least one, or back to previous menu',title='ERROR Checklist is null', form_color='CRITICAL')
        else:
            thrd = threading.Thread(
                target=StowtuiCore.stowExecute, kwargs={'dirs_name': selectable_values, 'path_dir': target_dir, 'path_dotfiles': dotfiles_dir})
            popup(thrd, 'Restoring dotfiles')
            npyscreen.notify_confirm('Done restored dotfiles with folder {}'.format(
                str(selectable_values)[1:-1]), title='Restored Dotfiles')
            self.parentApp.switchFormPrevious()
