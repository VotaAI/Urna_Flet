import flet as ft
# TODO -> AJEIAR OS ESPAÇAMENTOS, DEIXAR MAIS LIMPO, E VER A QUESTÃO DAS IMAGENS (OK)
# TODO -> QUESTÃO DE CONVERTER IMAGENS EM BASE64
def main(page: ft.Page):
    page.title = "Vota AÍ"
    page.theme_mode = ft.ThemeMode.LIGHT # trocar modo por aqui
    page.scroll = ft.ScrollMode.AUTO

    # BORA COMEÇAR REQUESTS!
    import requests

    json_votacoes_abertas = requests.get("https://backend-api-urna.onrender.com/votacoes/open?limit=10&offset=0").json()
    # json_votacoes_fechadas = requests.get("https://backend-api-urna.onrender.com/votacoes/closed?limit=10&offset=0").json()
    lista = []

    for votacao in json_votacoes_abertas:
        cartao = ft.Container(
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
                                        ft.Text(f"Votação: {votacao['titulo']}", weight=ft.FontWeight.BOLD),
                                        ft.Text(f"Período: {votacao['data_inicio']} até {votacao['data_fim']}."),
                                        ft.Text(f"Descrição: {votacao['descricao']}."),
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
                )
        lista.append(cartao)
        print(f"Votação: {votacao['titulo']}, Período: {votacao['data_inicio']} até {votacao['data_fim']}, Descrição: {votacao['descricao']}")

    # for votacao in json_votacoes_fechadas:
    #     print(f"Votação: {votacao['titulo']}, Período: {votacao['data_inicio']} até {votacao['data_fim']}, Descrição: {votacao['descricao']}")


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

    # IMAGENS:
    imagem_bem_vindo = ft.Image(
        src=f"/assets/banner_votai.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    # CONTAINER INICIAL
    container_inicial = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Bem-vindo(a) ao VotaAÍ!", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            ft.Text(
                                "Participe como eleitor ou se candidate nas votações que estão ocorrendo no momento",
                                size=20,
                            ),
                            espacamento2,
                            ft.OutlinedButton(text="Entrar", width=200),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    alignment=ft.alignment.center,

                    col={"xs": 12, "md": 6, "lg": 5},
                ),
                ft.Container(
                    content=ft.Image(
                        src=f"banner_votai.png",
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center_right,
                    expand=True,
                    col={"xs": 12, "md": 6, "lg": 7},
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    votacoes_dinamicas = ft.Container(
            content=ft.Column(lista, spacing=20),
            padding=20,
            alignment=ft.alignment.center
        )

    # VOTAÇÕES ATUAIS
    votacoes_atuais = ft.Container(
        content=ft.Column(
            [
                ft.Text("Verificar votações atuais", size=24, weight=ft.FontWeight.BOLD),

                votacoes_dinamicas,

                ft.ElevatedButton(text="Ver Mais", width=200),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        padding=20,
    )

    votacoes_dinamicas = ft.Container(
            content=ft.Column(lista, spacing=20),
            padding=20,
            alignment=ft.alignment.center
        )
    


    # SOBRE O VOTA AÍ
    sobre_vota_ai = ft.Column(
        [
            ft.Text(
                "Mas o que é o “VotaAÍ”?",
                size=30,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.ResponsiveRow(
                [
                    ft.Container(col={"lg": 3}),
                    ft.Container(
                        content=ft.Image(
                            src="imagem_pessoas.png",
                            fit=ft.ImageFit.COVER,
                        ),
                        col={"xs": 12, "md": 6, "lg": 2},
                        padding=10,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Nosso sistema de votação online foi criado para facilitar e tornar mais transparente a realização de votações em diferentes contextos — seja em escolas, empresas, comunidades ou projetos.",
                                    size=18,
                                    text_align=ft.TextAlign.LEFT,
                                ),
                                ft.Text(
                                    "Nosso objetivo é promover a participação democrática, com transparência, acessibilidade e segurança.",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.LEFT,
                                ),
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                        col={"xs": 12, "md": 6, "lg": 4},
                        padding=10,
                    ),
                    ft.Container(col={"lg": 3}),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )



    # FORMULÁRIO DE CONTATO
    formulario_contato = ft.Container(
        content=ft.Column(
            [
                ft.Text("Gostaria de Criar suas próprias votações?", size=25, weight=ft.FontWeight.BOLD),
                espacamento2,
                ft.Text("Entre em contato conosco para mais informações!", size=14),
                ft.TextField(label="Seu Email", width=300),
                espacamento2,
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
                espacamento, # Espaçamento entre seções
                votacoes_atuais,
                espacamento,
                sobre_vota_ai,
                espacamento,
                formulario_contato,
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
