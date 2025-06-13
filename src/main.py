import flet as ft
from tela_inicio import tela_inicial
from tela_downloads import tela_downloads

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(tela_inicial(page))
        elif page.route == "/instalar":
            page.views.append(tela_downloads(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
