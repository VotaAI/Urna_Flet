import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centraliza no eixo Y
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#303030"
    page.scroll = True

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
    subtitulo =ft.Text("Realize o seu papel de votante ou candidato.", size=20, color="#ffffff", text_align=ft.TextAlign.CENTER)

    registrar = ft.ElevatedButton(
        text="Registrar-se", 
        bgcolor="#ffffff", 
        color="#000000", 
        width=380, 
        height=37, 
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)
            ))
    
    container_titulo = ft.Container(
        content=ft.Column([titulo, subtitulo, registrar], spacing=25, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        # padding=200,
        # col={"xs":6, "md":1, "xl":6},
        alignment=ft.alignment.center,
        margin=ft.Margin(0,0,0,0)
    )

    def resize_handler(e=None):
        if page.window.width < 1200:
            container_titulo.margin = ft.Margin(0, 0, 0, 35)
        else:  
            container_titulo.margin = ft.Margin(0, 0, 0, 0)
        page.update()

    page.on_resized = resize_handler

    # resize_handler()

    email_cpf = ft.Text("Email/CPF", color="#ffffff", size=20)
    email_cpf_label = ft.TextField(hint_text="Insira seu Email ou CPF", expand=True, height=40, bgcolor="#ffffff", content_padding=10)

    container_email = ft.Container(
        content=ft.Column([email_cpf, email_cpf_label], spacing=5)
    )

    senha = ft.Text("Senha", color="#ffffff", size=20)
    senha_label = ft.TextField(hint_text="Digite sua senha", expand=True, height=40, bgcolor="#ffffff", content_padding=10)

    container_senha = ft.Container(
        content=ft.Column([senha, senha_label], spacing=5)
    )

    login = ft.Row([
        ft.ElevatedButton(
            text="Login",
            bgcolor="#ffffff",
            color="#000000",
            expand=True,
            height=47,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
            ),
        )
    ])


    container_labels = ft.Container(
        content=ft.Column([container_email, container_senha, login], spacing=50),
        # padding=150,
        # col={"xs":6, "md":1, "xl":6},
        alignment=ft.alignment.center
    )

    linha = ft.ResponsiveRow([
        ft.Container(content=ft.Column(), col={"xl":1}),
        ft.Container(content=ft.Column([container_titulo]), col={"xl":4, "md": 8, "sm": 10}),
        ft.Container(content=ft.Column(), col={"xl":1}),
        ft.Container(content=ft.Column([container_labels]), col={"xl":4, "md": 8, "sm": 10}),   
        ft.Container(content=ft.Column(), col={"xl":1})],
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente na linha
        vertical_alignment=ft.CrossAxisAlignment.CENTER  # Alinha os itens no meio verticalmente
    )

    page.add(linha)

ft.app(main)