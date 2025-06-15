import flet as ft
import requests

def tela_cadastro(page: ft.Page):

    def cadastrar(e):
        if senha_label.value == senha_confirmar_label.value:
            url = "https://backend-api-urna.onrender.com/cadastro/"

            header = {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }

            data = {
                "nome_completo": nome_completo_label.value,
                "cpf": cpf_label.value,
                "email": email_label.value,
                "user_type": "user",
                "senha": senha_label.value
            }

            
            response = requests.post(
                url,
                headers=header,
                json=data
            )

            print("Status Code:", response.status_code)
            print("Resposta JSON:", response.json())

        else:
            mensagem_status_senha.value = "As senhas não coincidem!"
            mensagem_status_senha.color = "red"
            mensagem_status_senha.update()
            page.update()

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

    titulo = ft.Text("Bem-vindo(a) ao sistema de votação!", size=45, color="#ffffff", text_align=ft.TextAlign.CENTER, style=(ft.TextStyle(weight=ft.FontWeight.BOLD)))
    subtitulo =ft.Text("Realize o seu papel de votante ou candidato.", size=20, color="#ffffff")

    registrar = ft.ElevatedButton(
        text="Login", 
        bgcolor="#ffffff", 
        color="#000000", 
        width=380, 
        height=37, 
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)
            ))
    
    registrar.on_click = lambda e: page.go("/entrar")
    
    container_titulo = ft.Container(
        content=ft.Column([titulo, subtitulo, registrar], spacing=25, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        # padding=200,
        # col={"xs":6, "md":1, "xl":6},
        alignment=ft.alignment.center,
        margin=ft.padding.only(bottom=90)
    )

    nome_completo = ft.Text("Nome completo:", color="#ffffff", size=20)
    nome_completo_label = ft.TextField(hint_text="Insira seu nome completo", expand=True, height=40, bgcolor="#ffffff", content_padding=10)
    container_nome = ft.Container(
        content=ft.Column([nome_completo, nome_completo_label], spacing=5)
    )

    cpf = ft.Text("CPF:", color="#ffffff", size=20)
    cpf_label = ft.TextField(hint_text="Insira seu CPF", expand=True, height=40, bgcolor="#ffffff", content_padding=10)
    container_cpf = ft.Container(
        content=ft.Column([cpf, cpf_label], spacing=5)
    )
    
    email = ft.Text("Email:", color="#ffffff", size=20)
    email_label = ft.TextField(hint_text="Insira seu email", expand=True, height=40, bgcolor="#ffffff", content_padding=10)
    container_email = ft.Container(
        content=ft.Column([email, email_label], spacing=5)
    )

    senha = ft.Text("Senha:", color="#ffffff", size=20)
    senha_label = ft.TextField(hint_text="Digite sua senha", expand=True, height=40, bgcolor="#ffffff", content_padding=10, password=True, can_reveal_password=True)
    mensagem_status_senha = ft.Text(value="", color="red", size=15)
    container_senha = ft.Container(
        content=ft.Column([senha, senha_label, mensagem_status_senha], spacing=5)
    )

    senha_confirmar = ft.Text("Senha:", color="#ffffff", size=20)
    senha_confirmar_label = ft.TextField(hint_text="Confirme sua senha", expand=True, height=40, bgcolor="#ffffff", content_padding=10, password=True, can_reveal_password=True) 
    container_senha_confirmar = ft.Container(
        content=ft.Column([senha_confirmar, senha_confirmar_label, mensagem_status_senha], spacing=5)
    )

    registrar = ft.Row([
        ft.ElevatedButton(
            text="Registrar",
            bgcolor="#ffffff",
            color="#000000",
            expand=True,
            height=47,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
            ),
            on_click=cadastrar
        )
    ])

    column_labels = ft.Column(
        [container_nome, container_cpf, container_email, container_senha, container_senha_confirmar, registrar],
        spacing=50
    )

    container_labels = ft.Container(
        content=column_labels,
        # padding=150,
        # col={"xs":6, "md":1, "xl":6},
        alignment=ft.alignment.center
    )

    def resize_handler(e=None):
        if page.window.width < 1200:  # Breakpoint médio do Flet
            print("a")
            container_titulo.margin = ft.Margin(0, 0, 0, 35)
            column_labels.spacing = 25
        if page.window.width > 1200:
            column_labels.spacing = 50
        page.update()

    page.on_resized = resize_handler

    linha = ft.ResponsiveRow([
        ft.Container(content=ft.Column(), col={"xl":1}),
        ft.Container(content=ft.Column([container_titulo]), col={"xl":4, "md": 8, "sm": 10}),
        ft.Container(content=ft.Column(), col={"xl":1}),
        ft.Container(content=ft.Column([container_labels]), col={"xl":4, "md": 8, "sm": 10}),   
        ft.Container(content=ft.Column(), col={"xl":1})],
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente na linha
        vertical_alignment=ft.CrossAxisAlignment.CENTER  # Alinha os itens no meio verticalmente
    )


    return ft.View(
        route="/cadastrar",
        appbar=ft.AppBar(
            leading=ft.Icon(ft.Icons.HOW_TO_VOTE),
            title=ft.Text("VotaAÍ"),
            center_title=False,
            actions=[
                ft.TextButton(text="Tela Inicial", on_click=lambda e: page.go("/")),
                ft.TextButton(text="Votações", on_click=lambda e: page.go("/votacoes")),
                ft.TextButton(text="Instalar", on_click=lambda e: page.go("/instalar")),
                ft.TextButton(text="Entrar", on_click=lambda e: page.go("/entrar")),
            ],
        ),
        controls=[
            linha
        ],
        scroll=ft.ScrollMode.AUTO
    )
