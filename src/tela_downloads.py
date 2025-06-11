import flet as ft

def main(page: ft.Page):
    page.title = "Vota AÍ - Instale nosso App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.HOW_TO_VOTE),
        title=ft.Text("VotaAÍ"),
        center_title=False,
        actions=[
            ft.TextButton(text="Tela Inicial"),
            ft.TextButton(text="Votações"),
            ft.TextButton(text="Instalar"),
            ft.TextButton(text="Entrar"),
        ],
    )

    espacamento = ft.Container(height=60)
    espacamento_pequeno = ft.Container(height=20)

    # HERO SECTION
    banner = ft.Container(
        padding=30,
        content=ft.Column([
            ft.Text("Conheça nosso aplicativo!", size=28, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text("Faça o download para obter nossos recursos", size=16, text_align=ft.TextAlign.CENTER),
            espacamento_pequeno,
            ft.Row([
                ft.OutlinedButton("Conferir mais"),
                ft.FilledButton("Instalar agora"),
            ], alignment=ft.MainAxisAlignment.CENTER)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10)
    )

    # FOOTER
    footer = ft.Container(
        bgcolor=ft.Colors.GREY_100,
        padding=20,
        content=ft.Column([
            ft.Text("© 2025 VotaAÍ - Todos os direitos reservados", size=12, text_align=ft.TextAlign.CENTER),
            ft.Row([
                ft.TextButton("Privacy Policy"),
                ft.TextButton("Terms of Service"),
                ft.TextButton("Contact Us")
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=15)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    page.add(
        ft.Column(
            [
                banner,
                espacamento, # Espaçamento entre seções
                footer,
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
