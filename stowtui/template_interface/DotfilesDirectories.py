import time
import os
import sys
import threading
from typing import List, Dict

import npyscreen
from stowtui.stowtui_core.stowtui_core import StowtuiCore
from stowtui.template_interface.help_ui import HelpForm


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
        except SystemExit:    # pragma: no cover
            os._exit(0)

    def create(self):

        self.add_handlers({'^Q': self.exit})
        self.add_handlers({'^T': self.on_cancel})
        self.add_handlers({'^S': self.help_form})

        self.add(npyscreen.Textfield,
                 value='NOTES:',
                 editable=False,
                 color='CONTROL')

        self.nextrely += 1

        self.add(npyscreen.Textfield,
                 value='Make Sure that the folders is your dotfiles config',
                 editable=False,
                 color='CONTROL')

        self.add(
            npyscreen.Textfield,
            value='An Exampale, your config is ~/dotfiles/zsh which contain, ',
            editable=False,
            color='CONTROL')

        self.add(npyscreen.Textfield,
                 value='-/zsh',
                 editable=False,
                 color='CONTROL')

        self.add(npyscreen.Textfield,
                 value='\t - .zshrc',
                 editable=False,
                 color='CONTROL')

        self.nextrely += 1

        self.add(npyscreen.Textfield,
                 value='IF Not you can switch to previous menu',
                 editable=False,
                 color='CONTROL')

        self.add(npyscreen.Textfield,
                 value='by pressing button cancel or use shortcut ^T',
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

        if StowtuiCore.getAllDir(self.settings['dotfiles_path']) is None:
            npyscreen.notify_confirm(
                'Target Dotfiles do not have any folders inside',
                title='ERROR Dotfiles folder is null',
                form_color='CRITICAL')
        else:
            self.res = self.add(npyscreen.TitleMultiSelect,
                                max_height=8,
                                name="List Directories Name",
                                values=StowtuiCore.getAllDir(
                                    self.settings['dotfiles_path']),
                                scroll_exit=True)
            self.nextrely += 1
            self.stow_op = self.add(
                npyscreen.TitleSelectOne,
                value=[
                    1,
                ],
                name="Choose Operation",
                values=["DELETE STOW", "CREATE STOW"],
                scroll_exit=True,
                width=10,
            )

    def on_cancel(self, *args, **kwargs):
        self.parentApp.switchFormPrevious()

    def on_ok(self, **kwargs):

        def popup(thrd, title, form_color):
            """
            Start the thread and display a popup of the plugin being cloned
            until the thread is finished
            """
            thrd.start()
            message_info = "loading..."
            npyscreen.notify_wait(message_info,
                                  title=title,
                                  form_color=form_color)
            while thrd.is_alive():
                time.sleep(1)
            return

        target_dir = self.settings['target_path']
        dotfiles_dir = self.settings['dotfiles_path']
        selectable_values = self.res.get_selected_objects()
        operation_values = self.stow_op.value

        if (selectable_values is None):
            npyscreen.notify_confirm(
                'Target Configs can not be null, please checklist at least one, or back to previous menu',
                title='ERROR Checklist is null',
                form_color='CRITICAL')

        # IF option to CREATE
        elif (operation_values == [1]):
            self.op_stow = npyscreen.notify_yes_no(
                'Do you want to create stow {}'.format(
                    str(selectable_values)[1:-1]),
                title='Stow Create Operation',
                form_color='CAUTION')

            if (self.op_stow == True):
                thrd = threading.Thread(target=StowtuiCore.stowExecuteCreate,
                                        kwargs={
                                            'dirs_name': selectable_values,
                                            'path_dir': target_dir,
                                            'path_dotfiles': dotfiles_dir
                                        })
                popup(thrd, 'Restoring dotfiles', 'STANDOUT')
                npyscreen.notify_confirm(
                    'Done restored dotfiles with folder {}'.format(
                        str(selectable_values)[1:-1]),
                    title='Restored Dotfiles')

            else:
                npyscreen.notify_confirm(
                    'Canceled Operation, Back to previous form, press OK',
                    title='Cancel Operation')

        # IF option to DELETE
        else:
            self.op_stow = npyscreen.notify_yes_no(
                'Delete operation test {}'.format(str(selectable_values)[1:-1]),
                title='Confirm Delete STOW CONFIG',
                form_color='DANGER')

            if (self.op_stow == True):
                thrd = threading.Thread(target=StowtuiCore.stowExecuteDelete,
                                        kwargs={
                                            'dirs_name': selectable_values,
                                            'path_dir': target_dir,
                                            'path_dotfiles': dotfiles_dir
                                        })

                popup(thrd, 'Deleting dotfiles', 'DANGER')

                npyscreen.notify_confirm(
                    'Done Deleted dotfiles with folder {}'.format(
                        str(selectable_values)[1:-1]),
                    title='Deleted Dotfiles')

            else:
                npyscreen.notify_confirm('Canceled Delete Dotfiles',
                                         title='False',
                                         form_color='CONTROL')

    def help_form(self, *args, **keywords):
        """ Toggles to help """
        self.parentApp.addForm('HELP',
                               HelpForm,
                               name='Help\t\t\t\t\t\t\t\t^T to toggle previous',
                               color='CAUTION')
        self.parentApp.switchForm('HELP')