import flet as ft
from tela_inicio import tela_inicial
from tela_downloads import tela_downloads
from dashboard_publico import tela_votacoes
from login import tela_login
from cadastro import tela_cadastro

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(tela_inicial(page))
        elif page.route == "/instalar":
            page.views.append(tela_downloads(page))
        elif page.route == "/votacoes":
            page.views.append(tela_votacoes(page))
        elif page.route == "/entrar":
            page.views.append(tela_login(page))
        elif page.route == "/cadastrar":
            page.views.append(tela_cadastro(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
