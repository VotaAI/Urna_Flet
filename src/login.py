import flet as ft
import requests

def tela_login(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centraliza no eixo Y
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#303030"
    # page.scroll = True

    try:
        token_inicio = page.client_storage.get("jwt_token")
        if token_inicio != None:
            print("\n\n\n\n\n\nTOKEN LOCALIZADO NO INICIO DA PAGINA: ", token_inicio,"\n\n\n\n\n\n")
    except:
        print("\n\n\n\n\n\nTOKEN NAO LOCALIZADO\n\n\n\n\n\n\n\n\n")

    def login(e):
        url = "https://backend-api-urna.onrender.com/login/"

        header = {
                'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        
        payload = f"grant_type=password&username={email_cpf_label.value}&password={senha_label.value}&client_id=&client_secret=&scope="
        
        response = requests.post(url=url,
                                headers=header,
                                json=payload)
        
        print("Status Code:", response.status_code)
        print("Resposta JSON:", response.json(),"\n\n\n")

        token = response.json()["access_token"]
        user_type = response.json()["user"]["user_type"]


        # Para salvar:
        page.client_storage.set("jwt_token", token)

        # Para recuperar:
        token_storage = page.client_storage.get("jwt_token")

        # user type
        page.client_storage.set("user_type", user_type)

        print(token_storage)

        page.go("/votacoes")


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
    registrar.on_click = lambda e: page.go("/cadastrar")

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
    email_cpf_label = ft.TextField(hint_text="Insira seu Email ou CPF", expand=True, height=40, bgcolor="#ffffff", content_padding=10, color="#000000")

    container_email = ft.Container(
        content=ft.Column([email_cpf, email_cpf_label], spacing=5)
    )

    senha = ft.Text("Senha", color="#ffffff", size=20)
    senha_label = ft.TextField(hint_text="Digite sua senha", expand=True, height=40, bgcolor="#ffffff", content_padding=10, color="#000000", password=True, can_reveal_password=True)

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
            on_click=login
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

    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=linha,
                    alignment=ft.alignment.center
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    return ft.View(
        
        route="/entrar",
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
            ft.Column(
            controls=[
                ft.Container(
                    content=linha,
                    alignment=ft.alignment.center
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        ],
        scroll=ft.ScrollMode.AUTO
    )