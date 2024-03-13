"""
Each row element is defined by this class. They have a Text description, \
text-field and an optional intractable (preferably a button)
"""

import flet


class Row(flet.UserControl):

    def __init__(
            self, heading: str, button_visible: bool = False,
            button_icon: flet.icons = None
    ):
        super().__init__()
        self.heading = flet.Text(value=heading, expand=True)
        self.entry = flet.TextField(
            value=heading, hint_text=f"Enter {heading}", expand=True,
        )
        self.intractable = flet.IconButton(
            icon=button_icon, width=40 if button_visible else 0,
            visible=button_visible
        )

    def build(self):
        """

        Returns:
            flet.Row : A row element with the Text description, \
                text-field and an optional intractable
        """
        return flet.Row(
            controls=[
                self.heading,
                self.entry,
                self.intractable
            ]
        )
