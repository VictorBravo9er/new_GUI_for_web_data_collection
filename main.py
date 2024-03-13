from tkinter import Entry
import flet
from Elements.Field import EntryField


def main(page: flet.Page):
    page.title = "app"
    page.theme_mode = flet.ThemeMode.DARK
    page.window_resizable = True

    page.add(
        EntryField("head", True, button_icon=flet.icons.EXIT_TO_APP),
    )
    page.update()


if __name__ == '__main__':
    flet.app(target=main,)# view=flet.AppView.WEB_BROWSER)
