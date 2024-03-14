"""
Each row element is defined by this class. They have a Text description, \
text-field and an optional intractable (preferably a button)
"""

from ctypes import alignment
import flet as ft


class EntryField(ft.UserControl):
    """
    This class related to an individual data point to be collected. \
    They have a Text description, text-field and an optional intractable \
    (preferably a button)

    Inherited from:
    @   ft.UserControl
    """

    def __init__(
            self, heading: str, button_visible: bool = False,
            button_icon: str = '', type:str = "text"
    ):
        """
        EntryField Class initializer.

        Args:
        @   heading (str): _description_
        @   button_visible (bool, optional): _description_. Defaults to False.
        @   button_icon (str, optional): _description_. Defaults to ''.
        """
        super().__init__()

        # set the elements of the field
        self.heading = ft.Text(
            value=heading, width=250, text_align=ft.TextAlign.END
        )
        self.entry = ft.TextField(
            hint_text=f"Enter {heading}", expand=True,
        )
        self.intractable = ft.IconButton(
            icon=button_icon, visible=button_visible,
            disabled=not button_visible,
        )


    def build(self) -> ft.Row:
        """
        Builds the element.

        Returns:
        ?   ft.Row: A row element with the Text description, text-field and an optional intractable
        """
        return ft.Row(
            controls=[
                self.heading,
                self.entry,
                self.intractable
            ],
            expand=True,
        )

    def __repr__(self):
        return f"{self.heading.value}: {self.intractable.icon}"
        