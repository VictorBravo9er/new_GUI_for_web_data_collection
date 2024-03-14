"""
This module incorporated all EntryField(s) and make a higher order element
"""
from typing import Any, List
import flet as ft
from ..Field import EntryField


class EntryData(ft.UserControl):
    """
    This class incorporated the EntryField(s) to make a list of entries which forms the whole dataset collected.

    Inherited from:
    @   ft.UserControl
    """

    __sumbit_enabled_msg = "Click to submit data"
    __submit_disabled_mdg = "Fill in the above fields"

    def __init__(self, entries: list[EntryField]):
        """
        EntryData Class initializer.

        Args:
        @   entries (list[ft.Control]): a list of elements that needs to be put in the Data.
        """
        super().__init__()

        self.entries = entries
        self.submit_button = ft.ElevatedButton(
            "submit", disabled=True, tooltip=self.__submit_disabled_mdg,
            visible=False
        )
        for entry in self.entries:
            print(entry.entry.value == "")

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