import npyscreen


class HelpForm(npyscreen.ActionFormMinimal):
    """ Help form for the Stowtui """

    def create(self):
        """ Override method for creating FormBaseNew form """

        PAGE_MENU_HELP = """
        Menu interactions on Path Selector are simple! Here is a quick guide to get you familiar.

        Navigation of a page: Up, Down, Left, Right. Note that
        TAB on Target Directory or Dotfiles Directory can be used to autocomplete paths!

        Editing a page: Simply navigating to an editable field and

        CTRL+T: To switch previous menu.

        CTRL+Q: Will exit the application.

        CTRL+X: Can be used to open up menus on certain pages."""

        self.add_handlers({'^W': self.change_forms, '^Q': self.exit})

        self.addfield = self.add(npyscreen.TitleFixedText,
                                 name='Stowtui',
                                 labelColor='DEFAULT',
                                 editable=False)
        self.multifield1 = self.add(npyscreen.MultiLineEdit,
                                    editable=False,
                                    value="""
            Menu interactions on are simple! Here is a quick guide to get you familiar.

            Navigation of a page: Up, Down, Left, Right. Note that
            TAB on Target Directory or Dotfiles Directory can be used to autocomplete paths!

            CTRL+T: To switch previous menu.

            CTRL+Q: Will exit the application.

            X: Can be used to mark or unmark selected Config folders.""")

    def exit(self, *args, **keywords):
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.exit()

    def on_ok(self):
        self.change_forms()

    def change_forms(self, *args, **keywords):
        """
        Checks which form is currently displayed and toggles to the other one
        """
        # Returns to previous Form in history if there is a previous Form
        try:
            self.parentApp.switchFormPrevious()
        except Exception as e:    # pragma: no cover
            self.parentApp.switchForm('MAIN')