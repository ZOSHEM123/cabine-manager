import flet as ft

from views.dashboard.dashboard_view import DashboardView


APP_TITLE = "Cabine Management"


def main(page: ft.Page):

    page.title = APP_TITLE
    page.padding = 20

    dashboard = DashboardView(page)

    page.add(
        dashboard.build()
    )


if __name__ == "__main__":
    ft.app(
        target=main
    )