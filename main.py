import flet as ft


APP_TITLE = "Cabine Management"


def main(page: ft.Page) -> None:
    page.title = APP_TITLE
    page.window.width = 1200
    page.window.height = 750
    page.window.center()

    page.add(
        ft.Text(
            "Cabine Management",
            size=30,
            weight=ft.FontWeight.BOLD,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)