import flet as ft

def main(page: ft.Page):
    page.title = "Enviar candidatura"
    page.bgcolor = "#303030"
    page.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.HOW_TO_VOTE),
            title=ft.Text("VotaAÍ"),
            center_title=False,
            actions=[
                ft.TextButton(text="Tela Inicial"),
                ft.TextButton(text="Votações"),
                ft.TextButton(text="Instalar App"),
                ft.TextButton(text="Entrar"),
            ],
        )

    titulo = ft.Text("Enviar Candidatura", size=45, weight=ft.FontWeight.BOLD, color="#ffffff")
    sub_titulo = ft.Text("Confirme os dados, envie e concorra na votação.", size=16, color="#ffffff")
    
    container_titulo = ft.Container(
        content=ft.Column([titulo, sub_titulo], spacing=10, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        margin=ft.margin.only(top=40, bottom=40),
        alignment=ft.alignment.center
    )

    nome_candidato = ft.Text("Nome", size=18, color="#ffffff")
    nome_candidato_label = ft.TextField(hint_text="Insira seu nome", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    nome_candidato_container = ft.Container(content=ft.Column([nome_candidato, nome_candidato_label], spacing=1))    

    descricao = ft.Text("Descrição/Detalhes", size=18, color="#ffffff")
    descricao_label = ft.TextField(hint_text="Insira uma breve descrição", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    descricao_container = ft.Container(content=ft.Column([descricao, descricao_label], spacing=1))

    nome_votacao = ft.Text("Nome da Votação", size=18, color="#ffffff")
    nome_votacao_label = ft.TextField(hint_text="Votação para presidente - 2025", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    nome_votacao_container = ft.Container(content=ft.Column([nome_votacao, nome_votacao_label], spacing=1))

    voltar_btn = ft.ElevatedButton(
        text="Voltar",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), color="#ffffff", side=ft.BorderSide(width=2, color="#ffffff"), text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
        expand=True,
        height=45,
        bgcolor="#303030"
        )
    
    enviar_btn = ft.ElevatedButton(
        text="Enviar Votação",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),bgcolor="#ffffff", color="#000000", text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
        expand=True,
        height=45
    )

    enviar_voltar_btn_container = ft.Container(
        content=ft.Row([voltar_btn, enviar_btn], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        padding=ft.padding.only(right=100, left=100)
    )

    container_labels = ft.Container(content=ft.Column([
        nome_candidato_container,
        descricao_container,
        nome_votacao_container,
        enviar_voltar_btn_container
    ], spacing=40, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER))

    page.add(container_titulo, container_labels)

ft.app(main)