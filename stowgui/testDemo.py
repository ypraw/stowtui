#!/usr/bin/env python
"""
DEMO TEST
"""
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import checkboxlist_dialog, message_dialog
from prompt_toolkit.styles import Style
from stowtui_core import StowtuiCore
from typing import Sequence

path_DIR = '/home/ypraw/Programming/linux/configDotfiles'

results: Sequence[str] = checkboxlist_dialog(
    title="CheckboxList dialog",
    text="What would you like in your breakfast ?",
    values=StowtuiCore.getAllDir(path_DIR),
    style=Style.from_dict({
        "dialog": "bg:#cdbbb3",
        "button": "bg:#bf99a4",
        "checkbox": "#e8612c",
        "dialog.body": "bg:#a9cfd0",
        "dialog shadow": "bg:#c98982",
        "frame.label": "#fcaca3",
        "dialog.body label": "#fd8bb6",
    }),
).run()

if results:
    print(results)
    StowtuiCore.stowExecute(results, path_DIR)
    message_dialog(
        title="Restore stow",
        text="You selected: %s\nfor restored !" % ",".join(results),
    ).run()
else:
    message_dialog("*starves*").run()
