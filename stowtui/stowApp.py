#!/usr/bin/env python
# encoding: utf-8

from stowtui_core import StowtuiCore
import npyscreen


class StowApp(npyscreen.NPSApp):

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
                    values=["Option1", "Option2", "Option3"],
                    scroll_exit=True)

        # This lets the user play with the Form.
        F.edit()


if __name__ == "__main__":
    App = StowApp()
    App.run()
