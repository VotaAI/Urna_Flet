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
    espacamento_muito_pequeno = ft.Container(height=10)

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

    # CARTÕES DE PLATAFORMA
    cartao_plataforma_windows = ft.Container(
        content=ft.Column([
            ft.Text("Windows", size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            espacamento_pequeno,
            ft.Text("Disponível .EXE"),
            espacamento_pequeno,
            ft.FilledButton(
                text="Baixar Windows",
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                    color=ft.Colors.PRIMARY_CONTAINER,
                    shape=ft.RoundedRectangleBorder(radius=4),
                    padding=ft.Padding(40, 20, 40, 20),
                ),
                on_click=lambda e: print("Baixar Windows clicado!"),
                width=200,
            ),
        ]),
        padding=20,
    )

    cartao_plataforma_android = ft.Container(
        content=ft.Column([
            ft.Text("Android", size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            espacamento_pequeno,
            ft.Text("Disponível .APK"),
            espacamento_pequeno,
            ft.FilledButton(
                text="Baixar Android",
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                    color=ft.Colors.PRIMARY_CONTAINER,
                    shape=ft.RoundedRectangleBorder(radius=4),
                    padding=ft.Padding(40, 20, 40, 20),
                ),
                on_click=lambda e: print("Baixar Android clicado!"),
                width=200,
            ),
        ],
        ),
        padding=20,
    )

    container_inicial = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(col={"xs": 12, "md": 6, "lg": 1}),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Plataformas Disponíveis", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            espacamento_pequeno,
                            ft.Text("Escolha sua plataforma de download", size=14, text_align=ft.TextAlign.CENTER),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    alignment=ft.alignment.center,
                    col={"xs": 12, "md": 6, "lg": 4},
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            cartao_plataforma_windows,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                    col={"xs": 12, "md": 6, "lg": 2},
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            espacamento_muito_pequeno,
                            cartao_plataforma_android,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                    col={"xs": 12, "md": 6, "lg": 2},
                ),
                ft.Container(col={"xs": 12, "md": 6, "lg": 2}),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # FUNCIONALIDADES (MODERNIZADA)
    funcionalidades = ft.Container(
        padding=40,
        content=ft.Column(
            [
                ft.Text("Funcionalidades do App", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                espacamento_pequeno,
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col={"xs": 12, "sm": 6, "md": 4},
                            padding=10,
                            content=ft.Card(
                                content=ft.Container(
                                    padding=20,
                                    content=ft.Column(
                                        [
                                            # ft.Icon(ft.Icons.PERSON_OUTLINE, size=40),
                                            ft.Text("Perfil Personalizado", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                            ft.Text("Gerencie suas informações, preferências e acompanhe seu histórico de votação."),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=10
                                    )
                                )
                            )
                        ),
                        ft.Container(
                            col={"xs": 12, "sm": 6, "md": 4},
                            padding=10,
                            content=ft.Card(
                                content=ft.Container(
                                    padding=20,
                                    content=ft.Column(
                                        [
                                            # ft.Icon(ft.cons.HOW_TO_VOTE_OUTLINED, size=40),
                                            ft.Text("Votações em Tempo Real", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                            ft.Text("Participe de votações instantaneamente com resultados em tempo real."),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=10
                                    )
                                )
                            )
                        ),
                        ft.Container(
                            col={"xs": 12, "sm": 6, "md": 4},
                            padding=10,
                            content=ft.Card(
                                content=ft.Container(
                                    padding=20,
                                    content=ft.Column(
                                        [
                                            # ft.Icon(ft.icons.NOTIFICATIONS_ACTIVE_OUTLINED, size=40),
                                            ft.Text("Notificações Instantâneas", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                            ft.Text("Receba alertas sobre novas votações, resultados e atualizações."),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=10
                                    )
                                )
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30
        )
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

    # adiciona bordas
    cartao_plataforma_android.border = ft.border.all(0.5, ft.Colors.GREY_500)
    cartao_plataforma_windows.border = ft.border.all(0.5, ft.Colors.GREY_500)

    page.add(
        ft.Column(
            [
                banner,
                espacamento,
                container_inicial,
                espacamento,
                funcionalidades,
                espacamento,
                footer,
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
