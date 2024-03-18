"""
This module incorporated all EntryField(s) and make a higher order element
"""
import flet as ft
from ..Field import EntryField


class EntryData(ft.UserControl):
    """
    This class incorporated the EntryField(s) to make a list of entries which forms the whole dataset collected.

    Inherited from:
    @   ft.UserControl
    """

    __sumbit_enabled_msg = "Click to submit data"
    __submit_disabled_msg = "Fill in the above fields"

    def __init__(
        self, controls: list[EntryField], 
        width: None | int | float = None,   # in built functionalities
        height: None | int | float = None, expand: None | bool | int = None,
        opacity: None | int | float = None, visible: bool | None = None, disabled: bool | None = None, 
    ):
        """
        EntryData Class initializer.

        Args:
        @   entries (list[ft.Control]): a list of elements that needs to be put in the Data.
        """
        super().__init__(
            width=width, height=height, expand=expand,
            opacity=opacity, visible=visible, disabled=disabled
        )

        self.entries = controls
        for ent in self.entries:
            ent.entry.on_change = self.checkForSubmit
            # ent.entry.on
        self.submit_button = ft.ElevatedButton(
            "submit", disabled=True, tooltip=self.__submit_disabled_msg,
            visible=False, on_click=...
        )

    def build(self) -> ft.ListView:
        """
        Build the element.

        Returns:
        ?   ft.ListView: holds all the data
        """
        view =  ft.ListView(
            controls=self.entries, expand=True  # type: ignore
        )
        view.controls.append(ft.Row(
            [
                self.submit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ))
        return view
    
    def checkForSubmit(self, e: ft.ControlEvent) -> None:
        """
        Checks if all fields are populated. If True, shows the Submit button,\
        else hides it.

        Args:
        @   e (ft.ControlEvent):
        """
        self.submit_button.disabled, self.submit_button.visible = (
            (False, True) if all(self.entries) else (True, False)
        )
        self.update()

    @classmethod
    def makePreDefinedElement(cls, page: ft.Page) -> "EntryData":
        ent: list[tuple[str, EntryField.SelectorType]] = [ 
            ("Website Name", EntryField.SelectorType.text_field, ),
            ("Age", EntryField.SelectorType.text_field, ),
            ("DA/PA (ahrefs)", EntryField.SelectorType.file_picker, ),
            ("Performance Data", EntryField.SelectorType.file_picker, ),
            ("Niche", EntryField.SelectorType.text_field, ),
            ("Ahrefs data", EntryField.SelectorType.file_picker, ),
            ("Monetization", EntryField.SelectorType.file_picker, ),
            ("Revenue data", EntryField.SelectorType.file_picker, ),
        ]
        """
        List of Entries
        Each Entry is a tuple of the entry heading, followed by an \
        icon, if any.
        """
        return EntryData(
            [
                EntryField(
                    heading=entry[0], type_=entry[1], page=page
                ) for entry in ent
            ]
        )



