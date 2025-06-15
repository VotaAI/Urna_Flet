import flet as ft
from tela_inicio import tela_inicial
from tela_downloads import tela_downloads
from dashboard_publico import tela_votacoes
from login import tela_login
from cadastro import tela_cadastro

# se possivel, melhorar essa logica do uso do token e user_type

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()

        rota = page.route
        token = page.client_storage.get("token")
        user_type = page.client_storage.get("user_type")

        if rota == "/":
            page.views.append(tela_inicial(page))
        elif rota == "/instalar":
            page.views.append(tela_downloads(page))
        elif rota == "/votacoes":
            page.views.append(tela_votacoes(page))
        elif rota == "/entrar":
            page.views.append(tela_login(page))
        elif rota == "/cadastrar":
            page.views.append(tela_cadastro(page))
        elif rota == "/dashboard_usuario":
            if token and user_type == "user":
                from dashboard_usuario import tela_dashboard_usuario
                page.views.append(tela_dashboard_usuario(page))
            else:
                page.go("/entrar")  # redireciona se não tiver login
        elif rota == "/dashboard_admin":
            if token and user_type == "admin":
                from dashboard import tela_dashboard_admin
                page.views.append(tela_dashboard_admin(page))
            else:
                page.go("/entrar")

        page.update()  # <- importante que fique no final

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
