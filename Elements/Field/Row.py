"""
Each row element is defined by this class. They have a Text description, \
text-field and an optional intractable (preferably a button)
"""

import flet


class EntryField(flet.UserControl):
    """
    This class related to an individual data point to be collected. \
    They have a Text description, text-field and an optional intractable \
    (preferably a button)

    Inherited from:
    @   flet.UserControl
    """

    def __init__(
            self, heading: str, button_visible: bool = False,
            button_icon: str = ''
    ):
        """
        EntryField Class initializer.

        Args:
        @   heading (str): _description_
        @   button_visible (bool, optional): _description_. Defaults to False.
        @   button_icon (str, optional): _description_. Defaults to ''.
        """
        super().__init__()
        self.heading = flet.Text(value=heading, expand=True)
        self.entry = flet.TextField(
            value=heading, hint_text=f"Enter {heading}", expand=True,
        )
        self.intractable = flet.IconButton(
            icon=button_icon, expand=True, visible=button_visible,
            disabled=not button_visible
        )

    def build(self) -> flet.Row:
        """
        Builds the element.

        Returns:
        ?   flet.Row: A row element with the Text description, text-field and an optional intractable
        """
        return flet.Row(
            controls=[
                self.heading,
                self.entry,
                self.intractable
            ],
            expand=True,
        )
