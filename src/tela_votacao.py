import flet as ft
# TODO -> responsividade, esta etranho a posição do teclado, não sei pq...
# TODO -> alterar as cores, etc
def main(page: ft.Page):
    page.title = "Vota AÍ"
    page.theme_mode = ft.ThemeMode.LIGHT # trocar modo por aqui
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

    # ESPAÇAMENTOS
    espacamento = ft.Container(height=100)  # Espaçamento entre seções
    espacamento2 = ft.Container(height=20)  # Espaçamento entre seções

    #################################### -------------------------- ######################################

    # INICIO DA PARTE ESSENCIAL PRO BACK END

    candidatos_nome = ["Candidato A", "Candidato B", "Candidato C"]
    numero_candidato = ["001", "002", "003"]

    candidatos_disponiveis = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Candidato")),
            ft.DataColumn(ft.Text("Numero")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(candidato)),
                    ft.DataCell(ft.Text(numero)),
                ]
            )
            for candidato, numero in zip(candidatos_nome, numero_candidato)
        ]
    )

    # FIM DA PARTE ESSENCIAL PRO BACK END
    #################################### -------------------------- ######################################

    # CONTAINER INICIAL
    container_inicial = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Votação", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            ft.Text(
                                "Escolha o seu candidato e vote!",
                                size=20,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # area votação

    # teclado numerico
    teclado = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                                [
                                    ft.ElevatedButton(text="1", width=60),
                                    ft.ElevatedButton(text="2", width=60),
                                    ft.ElevatedButton(text="3", width=60),
                                    ft.ElevatedButton(text="NULO", width=80, bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE),
                                ],
                                spacing=10,
                                alignment=ft.alignment.center,
                            ),
                            ft.Row(
                                [
                                    ft.ElevatedButton(text="4", width=60),
                                    ft.ElevatedButton(text="5", width=60),
                                    ft.ElevatedButton(text="6", width=60),
                                    ft.ElevatedButton(
                                        text="VO\nTAR",
                                        width=80,
                                        height=80,
                                        bgcolor=ft.Colors.GREEN_400,
                                        color=ft.Colors.WHITE,
                                    ),
                                ],
                                spacing=10,
                                alignment=ft.alignment.center,
                            ),
                            ft.Row(
                                [
                                    ft.ElevatedButton(text="7", width=60),
                                    ft.ElevatedButton(text="8", width=60),
                                    ft.ElevatedButton(text="9", width=60),
                                ],
                                spacing=10,
                                alignment=ft.alignment.center,
                            ),
                            ft.Row(
                                [
                                    ft.Container(width=60),  # Espaço vazio para alinhar o 0 centralizado
                                    ft.ElevatedButton(text="0", width=60),
                                ],
                                spacing=10,
                                alignment=ft.alignment.center,
                            ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
        alignment=ft.alignment.center,
    )


    container_area_votacao = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Vote no seu candidato", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            ft.Text(
                                "Digite o número do candidato para votar.",
                                size=15,
                            ),
                            ft.TextField(
                                label="Número do Candidato",
                                width=300,
                                text_align=ft.TextAlign.CENTER,
                                keyboard_type=ft.KeyboardType.NUMBER,
                                autofocus=True,
                            ),
                            teclado,
                            espacamento2,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    alignment=ft.alignment.center,
                    col={"xs": 12, "md": 12, "lg": 4},
                ),
                ft.Container(
                    content=candidatos_disponiveis,
                    col={"xs": 12, "md": 11, "lg": 4},
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


    # FOOTER RESPONSIVO
    footer = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "VotaAÍ - Todos os direitos reservados © 2025",
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
                espacamento2,
                container_area_votacao,
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
