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
        self, heading: str, page:ft.Page, type_: SelectorType = SelectorType.text_field,
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
        self.page = page
        self.file_picker = ft.FilePicker(on_result=self.fileSelectorEvent)
        # set the elements of the field
        try:
            self.entry, self.intractable = { 
                self.SelectorType.text_field: (
                    ft.TextField(
                        hint_text=f"Enter {heading}", expand=True, label=heading,
                        on_blur=self.displayCheckMark,
                    ),
                    ft.IconButton(
                        icon=ft.icons.CHECK, icon_color=ft.colors.GREEN, visible=False,
                        disabled=True,
                    )
                ),
                self.SelectorType.file_picker: (
                    ft.TextField(
                        hint_text=f"Enter {heading}", expand=True, label=heading,
                        read_only=True,
                    ),
                    ft.IconButton(
                        icon=ft.icons.FILE_UPLOAD, visible=True,
                        on_click=lambda _:self.file_picker.pick_files(
                            f"Select the {heading} file",
                            file_type=ft.FilePickerFileType.ANY,
                            allow_multiple=False
                        )
                    )
                )
            }[type_]
        except(KeyError):
            raise TypeError(f"'{type_}' is not a valid type for SelectorType")
        self.entry.color = ft.colors.BLACK
        self.entry.bgcolor = ft.colors.GREY_400
        self.intractable.bgcolor = ft.colors.GREY_400
        self.page.overlay.append(self.file_picker)
        self.update()

    def fileSelectorEvent(self, e: ft.FilePickerResultEvent):
        file = e.files[0].path  # type: ignore
        self.entry.value = file
        self.entry.on_change(e)  # type: ignore
        self.update()

    def __bool__(self) -> bool:
        """
        Returns True if the entry field is filled.

        Returns:
        ?   bool:
        """
        return True if self.entry.value else False

    def displayCheckMark(self, e: ft.ControlEvent):
        """
        Changes the visible status of the IconButton {self.intractable}

        Args:
        @   e (ft.ControlEvent): Control event object
        """
        if self.entry.value:
            self.intractable.visible=True
            self.update()
            return
        self.intractable.visible=False
        self.update()

    def build(self) -> ft.Row:
        """
        Builds the element.

        Returns:
        ?   ft.Row: A row element with the Text description, text-field and an optional intractable
        """
        return ft.Row(
            controls=[
                self.entry,
                self.intractable
            ],
            expand=True,
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of an object instance

        Returns:
        ?   str
        """
        return f"{self.entry.label}{self.entry.value}: {self.intractable.icon}"


def main(page: ft.Page):
    page.title = "Row test"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_resizable = True
    page.add(
        EntryField("hi", type_=EntryField.SelectorType.file_picker, page=page)
    )
    page.update()


if __name__ == "__main__":
    # a = EntryField("asd")
    # if a:
    #     print("sadas")
    # print(a)
    ft.app(main)