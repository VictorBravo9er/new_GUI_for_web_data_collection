from Elements.List import EntryData
import flet as ft

def main(page: ft.Page):
    page.title = "app"
    page.window_resizable = True
    page.add(
        EntryData.makePreDefinedElement(page)
    )
    # page.expand = True
    page.update()


if __name__ == '__main__':
    ft.app(target=main,)#view=ft.AppView.WEB_BROWSER, port=2343)
    