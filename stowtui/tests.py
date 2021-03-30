from prompt_toolkit.application import Application, get_app
from prompt_toolkit.formatted_text import HTML, merge_formatted_text
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import (
    AnyContainer,
    Dimension,
    FormattedTextControl,
    HSplit,
    Layout,
    VSplit,
    Window,
)
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import (
    Box,
    Button,
    Checkbox,
    Dialog,
    Label,
    RadioList,
    TextArea,
)


def create_title(text: str, dont_extend_width: bool = False) -> Label:
    return Label(text, style="fg:ansiblue", dont_extend_width=dont_extend_width)


def indented(container: AnyContainer, amount: int = 2) -> AnyContainer:
    return VSplit([Label("", width=amount), container])


class PartitionSelector:

    def __init__(self):
        self.entries = [
            HTML(
                "<bold>sda1</bold>                         ext3fs         15.29 GiB"
            ),
            HTML("<bold>sda2</bold>                         -extended-"),
            HTML(
                "<bold>sda5</bold>                         swap (v1)      721.64MiB"
            ),
        ]
        self.selected_line = 1
        self.container = Window(
            content=FormattedTextControl(
                text=self._get_formatted_text,
                focusable=True,
                key_bindings=self._get_key_bindings(),
            ),
            style="class:select-box",
            height=Dimension(preferred=5, max=5),
            cursorline=True,
            right_margins=[
                ScrollbarMargin(display_arrows=True),
            ],
        )

    def _get_formatted_text(self):
        result = []
        for i, entry in enumerate(self.entries):
            if i == self.selected_line:
                result.append([("[SetCursorPosition]", "")])
            result.append(entry)
            result.append("\n")

        return merge_formatted_text(result)

    def _get_key_bindings(self):
        kb = KeyBindings()

        @kb.add("up")
        def _go_up(event) -> None:
            self.selected_line = (self.selected_line - 1) % len(self.entries)

        @kb.add("down")
        def _go_up(event) -> None:
            self.selected_line = (self.selected_line + 1) % len(self.entries)

        return kb

    def __pt_container__(self):
        return self.container


def exit_clicked():
    get_app().exit()


dialog_body = HSplit([
    create_title("* Partition to save/restore"),
    indented(PartitionSelector(), amount=2),
    Box(
        HSplit([
            create_title("* Image file to create/use"),
            indented(
                TextArea(height=1),
                amount=2,
            ),
        ]),
        padding=0,
        padding_top=1,
        padding_bottom=1,
    ),
    VSplit([
        HSplit([
            create_title("Action to be done:"),
            RadioList(values=[
                ("save", "Save partition into a new image file"),
                (
                    "restore-partition",
                    "Restore partition from an image file",
                ),
                (
                    "restore-mbr",
                    "Restore an MBR from the imagefile",
                ),
            ]),
            Label(""),
            Checkbox("Connect to server"),
        ]),
        Box(
            HSplit(
                [
                    Button("Next (F5)"),
                    Button("About"),
                    Button("Exit (F6)", handler=exit_clicked),
                ],
                padding=1,
            ),
            padding_top=0,
            padding_left=3,
            padding_right=3,
        ),
    ],),
    indented(
        HSplit([
            VSplit(
                [
                    create_title("IP/name of the server:",
                                 dont_extend_width=True),
                    TextArea(width=Dimension(min=10, preferred=30)),
                    create_title("Port:", dont_extend_width=True),
                    TextArea(width=6, text="4025"),
                ],
                padding=1,
            ),
            Checkbox("Encrypt data on the network with SSL", checked=True),
        ]),
        amount=4,
    ),
])

root_container = Dialog(
    title="Partition Image 0.6.7",
    with_background=True,
    body=Box(
        dialog_body,
        padding=0,
        padding_left=1,
        padding_right=1,
    ),
)

style = Style.from_dict({
    "dialog.body select-box": "bg:#cccccc",
    "dialog.body select-box": "bg:#cccccc",
    "dialog.body select-box cursor-line": "nounderline bg:ansired fg:ansiwhite",
    "dialog.body select-box last-line": "underline",
    "dialog.body text-area": "bg:#4444ff fg:white",
    "dialog.body text-area": "bg:#4444ff fg:white",
    "dialog.body radio-list radio": "bg:#4444ff fg:white",
    "dialog.body checkbox-list checkbox": "bg:#4444ff fg:white",
})

kb = KeyBindings()


@kb.add("f6")
def _exit(event):
    event.app.exit()


@kb.add("f5")
def _next(event):
    # TODO
    pass


application: Application[None] = Application(layout=Layout(root_container),
                                             full_screen=True,
                                             style=style,
                                             key_bindings=kb)
application.run()