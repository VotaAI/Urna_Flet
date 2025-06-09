import flet as ft
# TODO -> AJEIAR OS ESPAÇAMENTOS, DEIXAR MAIS LIMPO, E VER A QUESTÃO DAS IMAGENS
def main(page: ft.Page):
    page.title = "Vota AÍ"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

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

    # CONTAINER INICIAL
    container_inicial = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Bem-vindo(a) ao VotaAÍ!", size=30, weight=ft.FontWeight.BOLD),
                            ft.Text(
                                "Participe como eleitor ou se candidate nas votações que estão ocorrendo no momento",
                                size=20,
                            ),
                            ft.OutlinedButton(text="Entrar"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    col={"xs": 12, "md": 6},
                ),
                ft.Container(
                    content=ft.Image(
                        src="https://cdn-icons-png.flaticon.com/512/107/107831.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    padding=20,
                    col={"xs": 12, "md": 6},
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # VOTAÇÕES ATUAIS
    votacoes_atuais = ft.Container(
        content=ft.Column(
            [
                ft.Text("Verificar votações atuais", size=24, weight=ft.FontWeight.BOLD),

                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                width=60,
                                height=60,
                                bgcolor=ft.Colors.GREY_300,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Votação para novo Representante", weight=ft.FontWeight.BOLD),
                                        ft.Text("Período: 30/05/2025 até 06/06/2025."),
                                        ft.Text("Descrição: Votação para eleição do novo Representante de Classe."),
                                    ]
                                ),
                                expand=True,
                                padding=10,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    border_radius=10,
                    padding=15,
                    width=600,  # <-- Aqui você define a "largura máxima"
                    alignment=ft.alignment.center,  # <-- Aqui centraliza horizontalmente
                ),

                ft.ElevatedButton(text="Ver Mais", width=200),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        padding=20,
    )


    # SOBRE O VOTA AÍ
    sobre_vota_ai = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Image(
                        src="https://cdn-icons-png.flaticon.com/512/107/107831.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    col={"xs": 12, "md": 6},
                    alignment=ft.alignment.center,
                    padding=20,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Nosso sistema de votação online foi criado para facilitar e tornar mais transparente a realização de votações em diferentes contextos.",
                                size=16,
                            ),
                            ft.Text(
                                "Promovemos participação democrática com acessibilidade e segurança.",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    col={"xs": 12, "md": 6},
                    padding=20,
                ),
            ]
        )
    )

    # FORMULÁRIO DE CONTATO
    formulario_contato = ft.Container(
        content=ft.Column(
            [
                ft.Text("Gostaria de Criar suas próprias votações?", size=25, weight=ft.FontWeight.BOLD),
                ft.Text("Entre em contato conosco para mais informações!", size=14),
                ft.TextField(label="Seu Email", width=300),
                ft.FilledButton(text="Quero criar minhas votações!"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
    )

    # FOOTER RESPONSIVO
    footer = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "VotaAÍ - Todos os direitos reservados © 2023",
                    size=12,
                    color=ft.Colors.ON_SURFACE_VARIANT,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Row(
                    [
                        ft.TextButton(text="Política de Privacidade"),
                        ft.TextButton(text="Termos de Uso"),
                        ft.TextButton(text="Contato"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
    )

    # PÁGINA FINAL
    page.add(
        ft.Column(
            [
                container_inicial,
                votacoes_atuais,
                sobre_vota_ai,
                formulario_contato,
                footer,
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
