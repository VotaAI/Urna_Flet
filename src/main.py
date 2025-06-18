import flet as ft
from tela_inicio import tela_inicial
from dashboard import dashboard
from tela_downloads import tela_downloads
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
        elif rota == "/votacoes":
            page.views.append(dashboard(page))
        elif rota == "/instalar":
            page.views.append(tela_downloads(page))
        elif rota == "/entrar":
            page.views.append(tela_login(page))
            page.bgcolor = "#303030"
        elif rota == "/cadastrar":
            page.views.append(tela_cadastro(page))
        elif rota == "/sobre":
            from sobre_a_votacao import tela_sobre_votacao
            page.views.append(tela_sobre_votacao(page))
        elif rota == "/criar_votacao":
            from criacao_votacao import tela_criar_votacao
            page.views.append(tela_criar_votacao(page))
        elif rota == "/enviar_candidatura":
            from enviar_candidatura import tela_enviar_candidatura
            page.views.append(tela_enviar_candidatura(page))

        page.update()  # <- importante que fique no final

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)