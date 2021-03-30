# from prompt_toolkit.shortcuts import checkboxlist_dialog
from prompt_toolkit.styles import Style
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, Layout, VSplit, FormattedTextControl, Window
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button, Label, Checkbox

from stowtui_core import StowtuiCore
from typing import Sequence

# # print(getAllDir(path_DIR))
# path_DIR = '/home/ypraw/Programming/linux/configDotfiles'
# results: Sequence[str] = checkboxlist_dialog(
#     title="Stow TUI",
#     text="What would you like to create symlink ?",
#     values=StowtuiCore.getAllDir(path_DIR),
#     style=Style.from_dict({
#         'dialog': 'bg:#cdbbb3',
#         'button': 'bg:#bf99a4',
#         'checkbox': '#e8612c',
#         'dialog.body': 'bg:#a9cfd0',
#         'dialog shadow': 'bg:#c98982',
#         'frame.label': '#93645f',
#         'dialog.body label': '#93645f',
#     })).run()

# # print(type(results))
# print(results)

# class StowUserInterface:

#     # def __init__(self):
#     #     self.StowtuiCore = StowtuiCore(self)
#     #     self._create_ui()

#     @staticmethod
#     def _exit_clicked(_=None):
#         get_app().exit()

#     def _create_ui(self):
#         btn_save = Button("Save", hendler=self.StowtuiCore.stowExecute(results))
#         btn_exit = Button("Exit", handler=self._exit_clicked)
#         list_directory_checkbox = Checkbox(
#             title="Stow TUI",
#             text="What would you like to create symlink ?",
#             values=StowtuiCore.getAllDir(path_DIR),
#             style=Style.from_dict({
#                 'dialog': 'bg:#cdbbb3',
#                 'button': 'bg:#bf99a4',
#                 'checkbox': '#e8612c',
#                 'dialog.body': 'bg:#a9cfd0',
#                 'dialog shadow': 'bg:#c98982',
#                 'frame.label': '#93645f',
#                 'dialog.body label': '#93645f'
#             }))
#         root_container = Box(
#             HSplit([
#                 Label(text="Press `Tab` to move the focus."),
#                 HSplit([
#                     VSplit(
#                         [btn_save, btn_exit],
#                         padding=1,
#                         style="bg:#cccccc",
#                     ),
#                     Frame(
#                         title="Checkbox list",
#                         body=HSplit([checkbox1, checkbox2]),
#                     ),
#                 ]),
#             ]))
#         layout = Layout(container=root_container, focused_element=btn_save)
#         self.application = Application(
#             layout=layout,
#             # key_bindings=self.kb,
#             #    style=style,
#             full_screen=True)

#     def run(self):
#         # self._draw()
#         # threading.Thread(target=lambda: every(0.4, self._draw),
#         #                  daemon=True).start()
#         self.application.run()


def _exit_clicked(_=None):
    get_app().exit()


def _create_ui():
    btn_save = Button("Save", hendler=self.StowtuiCore.stowExecute(results))
    btn_exit = Button("Exit", handler=self._exit_clicked)
    list_directory_checkbox = Checkbox(
        title="Stow TUI",
        text="What would you like to create symlink ?",
        values=StowtuiCore.getAllDir(path_DIR),
        style=Style.from_dict({
            'dialog': 'bg:#cdbbb3',
            'button': 'bg:#bf99a4',
            'checkbox': '#e8612c',
            'dialog.body': 'bg:#a9cfd0',
            'dialog shadow': 'bg:#c98982',
            'frame.label': '#93645f',
            'dialog.body label': '#93645f'
        }))
    root_container = Box(
        HSplit([
            Label(text="Press `Tab` to move the focus."),
            HSplit([
                VSplit(
                    [btn_save, btn_exit],
                    padding=1,
                    style="bg:#cccccc",
                ),
                Frame(
                    title="Checkbox list",
                    body=HSplit([checkbox1, checkbox2]),
                ),
            ]),
        ]))
    layout = Layout(container=root_container, focused_element=btn_save)
    self.application = Application(
        layout=layout,
        # key_bindings=self.kb,
        #    style=style,
        full_screen=True)


def run():
    # self._draw()
    # threading.Thread(target=lambda: every(0.4, self._draw),
    #                  daemon=True).start()
    application.run()


def main():
    # result = application.run()
    # StowUserInterface.run()
    # StowUserInterface.run()
    # print("You said: %r" % result)

    # if __name__ == "__main__":
    #     # main()

run()