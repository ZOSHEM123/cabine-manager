"""
Dashboard view.

Main application screen.
"""

import flet as ft


class DashboardView:
    """Main dashboard screen."""

    def __init__(self, page: ft.Page):
        self.page = page

    def build(self) -> ft.Control:
        """
        Build dashboard interface.
        """

        return ft.Column(
            controls=[
                ft.Text(
                    "Cabine Management",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    "Tableau de bord",
                    size=24,
                ),

                ft.Divider(),

                ft.Row(
                    controls=[
                        self.create_card(
                            "Stock",
                            "Gestion des unités disponibles",
                        ),

                        self.create_card(
                            "Ventes",
                            "Suivi des ventes",
                        ),

                        self.create_card(
                            "Finance",
                            "Suivi financier",
                        ),
                    ]
                ),
            ]
        )

    def create_card(
        self,
        title: str,
        description: str,
    ) -> ft.Card:

        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            title,
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),

                        ft.Text(description),
                    ]
                ),
                padding=20,
                width=250,
            )
        )