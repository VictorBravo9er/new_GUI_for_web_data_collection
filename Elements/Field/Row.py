"""
Each row element is defined by this class. They have a Text description, \
text-field and an optional intractable (preferably a button)
"""
from enum import Enum
from turtle import color
import flet as ft


class EntryField(ft.UserControl):
    """
    This class related to an individual data point to be collected. \
    They have a Text description, text-field and an optional intractable \
    (preferably a button)

    Inherited from:
    @   ft.UserControl
    """

    class SelectorType(Enum):
        text_field = "text"
        file_picker = "file"
        

    def __init__(
        self, heading: str, type_: SelectorType = SelectorType.text_field,
        button_icon: None | str = None, 
        visible: None | bool = None, disabled: None | bool = None,   # inbuilt functionalities
        width: None | int | float = None, height: None | int | float = None,  
        expand: None | bool | int = None, opacity: None | int | float = None,

    ):
        """
        EntryField Class initializer.

        Args:
        @   heading (str): _description_
        @   button_visible (bool, optional): _description_. Defaults to False.
        @   button_icon (str, optional): _description_. Defaults to ''.
        @   The rest are in-built.
        """
        super().__init__(
            width=width, height=height, expand=expand, 
            opacity=opacity, visible=visible, disabled=disabled,
        )

        # set the elements of the field
        self.heading = ft.Text(value=heading, width=250, text_align=ft.TextAlign.END)
        try:
            self.entry, self.intractable = { 
                self.SelectorType.text_field: (
                    ft.TextField(
                        hint_text=f"Enter {heading}", expand=True,
                        on_blur=self.displayIntractable,
                    ),
                    ft.IconButton(
                        icon=ft.icons.CHECK, icon_color=ft.colors.GREEN, visible=False,
                        disabled=True,
                    )
                ),
                self.SelectorType.file_picker: (
                    ft.TextField(
                        hint_text=f"Enter {heading}", expand=True,
                        read_only=True,
                    ),
                    ft.IconButton(
                        icon=ft.icons.FILE_UPLOAD, visible=True,
                        tooltip="Select the desired file", on_click=...
                        # TODO: complete the file picker funtionality
                    )
                )
            }[type_]
        except(KeyError):
            raise TypeError(f"'{type}' is not a valid type for SelectorType")

    def displayIntractable(self, e):
        self.intractable.visible=True
        self.update()

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
        return f"{self.heading.value}{self.entry.value}: {self.intractable.icon}"
        