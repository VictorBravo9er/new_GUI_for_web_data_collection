import flet as ft

def main(page: ft.Page):
    page.title = "app"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_resizable = True
    from PopulatedEntries import entries
    page.add(
        entries
    )
    page.expand = True
    page.update()


if __name__ == '__main__':
    ft.app(target=main,)# view=ft.AppView.WEB_BROWSER)
