import flet as ft
import requests
# TODO: MELHGORAR CORES NAS TELAS LOGIM E CADASTRO, FICAM OK NO NAVEGADOR, MAS EM DESL=KTOP, FICA ERRADO
def tela_login(page: ft.Page):
    page.title = "VotaAÍ - Login"
    page.client_storage.remove("access_token")
    page.client_storage.remove("user_type")
    page.client_storage.remove("user_id")

    def login(e):
        page.client_storage.remove("access_token")
        page.client_storage.remove("user_type")
        page.client_storage.remove("user_id")
        url = "https://backend-api-urna.onrender.com/login/"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        payload = f"grant_type=password&username={email_cpf_label.value}&password={senha_label.value}&client_id=string&client_secret=string&scope="
        
        response = requests.post(url=url, headers=headers, data=payload)

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            
            print("Resposta JSON:", response.json())
            data = response.json()
            token = data["access_token"]
            user_type = data["user"]["user_type"]
            user_id = data["user"]["id_user"]
            print(f"Token: {token}, Tipo de usuário: {user_type}, ID do usuário: {user_id}")

            # Você pode armazenar os dados no page.client_storage se quiser manter o login
            page.client_storage.set("token", token)
            page.client_storage.set("user_type", user_type)
            page.client_storage.set("user_id", user_id)

            # Navegar baseado no tipo de usuário
            if user_type == "admin":
                page.go("/dashboard_admin")
            elif user_type == "user":
                page.go("/dashboard_usuario")
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Tipo de usuário não reconhecido!"))
                page.snack_bar.open = True
                page.update()
        else:
            try:
                erro = response.json()
            except:
                erro = {"detail": "Erro desconhecido"}

            page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao fazer login: {erro.get('detail')}"))
            page.snack_bar.open = True
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
                ft.Container( # solucao temporaria
                    height=100,
                ),
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

