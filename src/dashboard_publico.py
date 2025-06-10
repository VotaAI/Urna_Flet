import flet as ft
# TODO -> CORES DOS BOTÕES

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

    # AO ANEXAR O BD, MUDAR A LÓGICA PARA BUSCAR AS INFORMAÇÕES DIRETO DO BANCO DE DADOS

    # TABELA TESTE (FUTURAMENTE, DINAMICA PRA TRAZER A VOTAÇÃO) -> tem candidato, partido, quantidade de votos
    candidatos_nome = ["Candidato A", "Candidato B", "Candidato C"]
    partidos_nome = ["Partido X", "Partido Y", "Partido Z"]
    quantidade_votos = [150, 200, 100]

    # Criação da tabela
    tabela_votacoes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Candidato")),
            ft.DataColumn(ft.Text("Detalhes")),
            ft.DataColumn(ft.Text("Quantidade de Votos")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(candidato)),
                    ft.DataCell(ft.Text(partido)),
                    ft.DataCell(ft.Text(str(votos))),
                ]
            )
            for candidato, partido, votos in zip(candidatos_nome, partidos_nome, quantidade_votos)
        ]
    )

    # CRIAÇÃO DO CARTÃO QUE MOSTRA O VENCEDOR DA VOTAÇÃO
    cartao_vencedor = ft.Container(
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
                                        ft.Text("Vencedor", weight=ft.FontWeight.BOLD),
                                        ft.Text("Candidato B"),
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
    
    # CRIAÇÃO DO CARTÃO VOTAÇÃO ATUAL
    # A LOGICA QUE USEI FOI UM CARTÃO INDIVIDUAL, PROVAVELMENTE ALTERAR AO COLOCAR O BANCO DE DADOS
    cartao_votacao_atual = ft.Container(
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
                    width=1000,  # <-- Aqui você define a "largura máxima"
                    alignment=ft.alignment.center,  # <-- Aqui centraliza horizontalmente
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
                            ft.Text("Votações", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            ft.Text(
                                "Veja o resultado de votações anteriores e quais votações estão ocorrendo no momento.",
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

    # VOTAÇÃO FECHADA:
    container_votacao_fechada = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(col={"lg": 2}),
                ft.Container(
                    content=
                    ft.Column(
                        [
                            ft.Text("Votação Fechada", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            ft.Text(
                                "Período: 10/05/2025 até 30/05/2025.",
                                size=15,
                            ),
                            ft.Text(
                                "Descrição: Votação para eleição do novo presidente do Brasil..",
                                size=15,
                            ),
                            espacamento2,
                            ft.FilledButton(
                                text="Baixar CSV",
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                    color=ft.Colors.PRIMARY_CONTAINER,
                                    shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                    padding=ft.Padding(40, 20, 40, 20),  # aumenta o tamanho (deixa mais quadrado)
                                    
                                ),
                                on_click=lambda e: print("Baixar CSV clicado!"),
                            ),
                            espacamento2,
                            cartao_vencedor,
                            espacamento2,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    alignment=ft.alignment.center,
                    col={"xs": 12, "md": 12, "lg": 4},
                ),
                ft.Container(
                    content=tabela_votacoes,
                    col={"xs": 12, "md": 11, "lg": 4},
                ),
                ft.Container(col={"lg": 2}),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    

    # VOTAÇÕES ATUAIS
    votacoes_atuais = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(col={"lg": 2}),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Votações Atuais", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            cartao_votacao_atual,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    alignment=ft.alignment.center,
                    col={"xs": 12, "md": 6, "lg": 8},
                ),

                ft.Container(col={"lg": 2}),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
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

    # adiciona bordas:
    cartao_vencedor.border = ft.border.all(0.5, ft.Colors.GREY_500)
    cartao_votacao_atual.border = ft.border.all(0.5, ft.Colors.GREY_500)



    # PÁGINA FINAL
    page.add(
        ft.Column(
            [
                container_inicial,
                espacamento, # Espaçamento entre seções
                container_votacao_fechada,
                espacamento,  # Espaçamento entre seções
                votacoes_atuais,
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
