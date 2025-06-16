import flet as ft

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

    espacamento = ft.Container(height=100)
    espacamento2 = ft.Container(height=20)

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

    # Campo de entrada (precisa estar acessível às funções)
    campo_numero = ft.TextField(
        label="Número do Candidato",
        width=300,
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        autofocus=True,
    )

    # Callbacks dos botões
    def adicionar_numero(e):
        if campo_numero.value != "NULO":
            campo_numero.value += e.control.text
        else:
            campo_numero.value = e.control.text
        campo_numero.update()

    def votar(e):
        print("Votando no número:", campo_numero.value)
        campo_numero.value = ""
        campo_numero.update()

    def voto_nulo(e):
        campo_numero.value = "NULO"
        campo_numero.update()

    def criar_botao(texto, cor, texto_cor, largura=60, altura=None, acao=None):
        return ft.FilledButton(
            text=texto,
            width=largura,
            height=altura,
            on_click=acao,
            style=ft.ButtonStyle(
                bgcolor=cor,
                color=texto_cor,
                shape=ft.RoundedRectangleBorder(radius=4),
            ),
        )

    teclado = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        criar_botao("1", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                        criar_botao("2", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                        criar_botao("3", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                        criar_botao("NULO", ft.Colors.RED_400, ft.Colors.WHITE, largura=80, acao=voto_nulo),
                    ],
                    spacing=10,
                    alignment=ft.alignment.center,
                ),
                ft.Row(
                    [
                        criar_botao("4", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                        criar_botao("5", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                        criar_botao("6", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                        criar_botao("VOTAR", ft.Colors.GREEN_400, ft.Colors.WHITE, largura=80, altura=80, acao=votar),
                    ],
                    spacing=10,
                    alignment=ft.alignment.center,
                ),
                ft.Row(
                    [
                        criar_botao("7", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                        criar_botao("8", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                        criar_botao("9", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                    ],
                    spacing=10,
                    alignment=ft.alignment.center,
                ),
                ft.Row(
                    [
                        ft.Container(width=60),  # espaço vazio para alinhar
                        criar_botao("0", ft.Colors.ON_SURFACE_VARIANT, ft.Colors.ON_TERTIARY, acao=adicionar_numero),
                    ],
                    spacing=10,
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
    )

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

    container_area_votacao = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(col={"lg": 2, "md": 1, "xs": 1}),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Vote no seu candidato", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            ft.Text("Digite o número do candidato para votar.", size=15),
                            campo_numero,
                            espacamento2,
                            teclado,
                            espacamento2,
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    alignment=ft.alignment.center,
                    col={"xs": 10, "md": 6, "lg": 4},
                ),
                ft.Container(
                    content=candidatos_disponiveis,
                    col={"xs": 12, "md": 12, "lg": 4},
                ),
                ft.Container(col={"lg": 2, "md": 3}),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

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
