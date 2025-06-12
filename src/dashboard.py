import flet as ft

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
    espacamento3 = ft.Container(height=10)  # Espaçamento entre seções

    #################################### -------------------------- ######################################

    # INICIO DA PARTE ESSENCIAL PRO BACK END

    # TABELA DE CANDIDATOS
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

    # DICIONÁRIO COM INFORMAÇÕES SOBRE A VOTAÇÃO
    votacao_aberta_sobre_a_votacao = {
        "titulo": "Votação de Representantes", 
        "inicio": "01/06/2025",
        "fim": "31/06/2025",
        "descricao": "Participe da votação para escolher os representantes do nosso projeto. Vote no candidato de sua preferência digitando o número correspondente.",
        "status": "Aberta",
        "categoria": "Educação",
        "permite_candidatura": True,
    }

    votacao_fechada_sobre_a_votacao = {
        "titulo": "Votação de Representantes - Anterior", 
        "inicio": "01/01/2025",
        "fim": "31/01/2025",
        "descricao": "Votação de representabtes do primeiro semestre de 2025.",
        "status": "Fechada",
        "categoria": "Educação",
        "permite_candidatura": False,
    }

    # candidatos pendentes

    candidatos_pendentes = [
        {"nome": "Candidato A", "numero": "001", "descricao": "Partido X","cpf": "123.456.789-00"},
        {"nome": "Candidato B", "numero": "002", "descricao": "Partido Y", "cpf": "987.654.321-00"},
        {"nome": "Candidato C", "numero": "003", "descricao": "Partido Z", "cpf": "456.789.123-00"},
    ]


    


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
    # ACHO MELHOR TIRAR... TIPO, COMO É SÓ UM DASHBOARDSIMPLES, SÓ MOSTRA NA TELA AS VOTAÇ~ES EM ABERTO E AS FECHADAS

    # CONTAINER VOTAÇÕES EM ABERTO
    titulo_votacoes = ft.Text(
        "Votações em Aberto",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.START,
    )

    cartao_votacao_atual = ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Container(
                                width=60,
                                height=60,
                                bgcolor=ft.Colors.GREY_300,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(f"{votacao_aberta_sobre_a_votacao['titulo']}", weight=ft.FontWeight.BOLD, size=20),
                                        ft.Text(f"Período: {votacao_aberta_sobre_a_votacao['inicio']} até {votacao_aberta_sobre_a_votacao['fim']}."),
                                        ft.Text(f"Descrição: {votacao_aberta_sobre_a_votacao['descricao']}"),
                                    ]
                                ),
                                expand=True,
                                padding=10,
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.FilledButton(
                                            text="STATUS",
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.PRIMARY_CONTAINER,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                padding=ft.Padding(40, 20, 40, 20),  # aumenta o tamanho (deixa mais quadrado)
                                                
                                            ),
                                            on_click=lambda e: print("Baixar CSV clicado!"),
                                            width=200,
                                        ),
                                        ft.FilledButton(
                                        text="EXCLUIR",
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.PRIMARY_CONTAINER,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                padding=ft.Padding(40, 20, 40, 20),  # aumenta o tamanho (deixa mais quadrado)
                                                
                                            ),
                                            on_click=lambda e: print("Baixar CSV clicado!"),
                                            width=200,
                                        ),
                                    ]
                                ),
                                expand=True,
                                padding=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    border_radius=10,
                    padding=15,
                    width=1000,  # <-- Aqui você define a "largura máxima"
                    alignment=ft.alignment.center,  # <-- Aqui centraliza horizontalmente
                )
    # BOTÃO CRIAR VOTAÇÃO
    botao_criar_votacao = ft.FilledButton(
                                        text="CRIAR VOTAÇÃO",
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.PRIMARY_CONTAINER,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                padding=ft.Padding(40, 40, 40, 40),  # aumenta o tamanho (deixa mais quadrado)
                                                
                                            ),
                                            on_click=lambda e: print("Baixar CSV clicado!"),
                                            width=1000,
                                        )
    
    # CONTAINER VOTAÇÕES FECHADAS
    titulo_votacoes_fechadas = ft.Text(
        "Votações Fechadas",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.START,
    )

    cartao_votacao_fechada = ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Container(
                                width=60,
                                height=60,
                                bgcolor=ft.Colors.GREY_300,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(f"{votacao_fechada_sobre_a_votacao['titulo']}", weight=ft.FontWeight.BOLD, size=20),
                                        ft.Text(f"Período: {votacao_fechada_sobre_a_votacao['inicio']} até {votacao_aberta_sobre_a_votacao['fim']}."),
                                        ft.Text(f"Descrição: {votacao_fechada_sobre_a_votacao['descricao']}"),
                                    ]
                                ),
                                expand=True,
                                padding=10,
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.FilledButton(
                                            text="STATUS",
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.PRIMARY_CONTAINER,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                padding=ft.Padding(40, 20, 40, 20),  # aumenta o tamanho (deixa mais quadrado)
                                                
                                            ),
                                            on_click=lambda e: print("Baixar CSV clicado!"),
                                            width=200,
                                        ),
                                        ft.FilledButton(
                                        text="EXCLUIR",
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.PRIMARY_CONTAINER,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                padding=ft.Padding(40, 20, 40, 20),  # aumenta o tamanho (deixa mais quadrado)
                                                
                                            ),
                                            on_click=lambda e: print("Baixar CSV clicado!"),
                                            width=200,
                                        ),
                                    ]
                                ),
                                expand=True,
                                padding=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    border_radius=10,
                    padding=15,
                    width=1000,  # <-- Aqui você define a "largura máxima"
                    alignment=ft.alignment.center,  # <-- Aqui centraliza horizontalmente
                )
    
    # CONTAINER CANDIDAOS PENDENTES

    container_candidatos_pendentes = ft.Container(
        alignment=ft.alignment.center,
        padding=20,
        content=ft.Column(
            [
                ft.Text("Candidatos Pendentes", size=30, weight=ft.FontWeight.BOLD),
                espacamento3,
                ft.Text(
                    "Aprovar ou rejeitar candidatos que se candidataram à votação.",
                    size=15,
                    text_align=ft.TextAlign.CENTER,
                ),
                espacamento3,
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            col={"lg": 4, "md": 2, "xs": 1},
                        ),
                        ft.Container(
                            content=ft.FilledButton(
                                text="Rejeitar Todos",
                                width=400,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                    color=ft.Colors.PRIMARY_CONTAINER,
                                    shape=ft.RoundedRectangleBorder(radius=6),
                                    padding=ft.Padding(40, 20, 40, 20),
                                ),
                                on_click=lambda e: print("Botão 1 clicado"),
                            ),
                            col={"lg": 2, "md": 4, "xs": 5},
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.FilledButton(
                                text="Aprovar Todos",
                                width=400,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                    color=ft.Colors.PRIMARY_CONTAINER,
                                    shape=ft.RoundedRectangleBorder(radius=6),
                                    padding=ft.Padding(40, 20, 40, 20),
                                ),
                                on_click=lambda e: print("Botão 2 clicado"),
                            ),
                            col={"lg": 2, "md": 4, "xs": 5},
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            col={"lg": 4, "md": 2, "xs": 1},
                        ),
                        ft.Container(
                            content=ft.FilledButton(
                                text="Pendentes",
                                width=200,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                    color=ft.Colors.PRIMARY_CONTAINER,
                                    shape=ft.RoundedRectangleBorder(radius=6),
                                ),
                                on_click=lambda e: print("Botão 3 clicado"),
                            ),
                            col={"lg": 1, "md": 2, "xs": 3},
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.FilledButton(
                                text="Aprovados",
                                width=200,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                    color=ft.Colors.PRIMARY_CONTAINER,
                                    shape=ft.RoundedRectangleBorder(radius=6),
                                ),
                                on_click=lambda e: print("Botão 4 clicado"),
                            ),
                            col={"lg": 1, "md": 2, "xs": 3},
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.FilledButton(
                                text="Rejeitados",
                                width=200,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                    color=ft.Colors.PRIMARY_CONTAINER,
                                    shape=ft.RoundedRectangleBorder(radius=6),
                                ),
                                on_click=lambda e: print("Botão 4 clicado"),
                            ),
                            col={"lg": 1, "md": 2, "xs": 3},
                            alignment=ft.alignment.center,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                    run_spacing=10,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    tabela_candidatos_pendentes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Candidato")),
            ft.DataColumn(ft.Text("Número")),
            ft.DataColumn(ft.Text("Descrição")),
            ft.DataColumn(ft.Text("CPF")),
            ft.DataColumn(ft.Text("Ações")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(candidato["nome"])),
                    ft.DataCell(ft.Text(candidato["numero"])),
                    ft.DataCell(ft.Text(candidato["descricao"])),
                    ft.DataCell(ft.Text(candidato["cpf"])),
                    ft.DataCell(
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.Icons.CHECK,
                                    on_click=lambda e, c=candidato: print(f"Aprovar {c['nome']}"),
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.CANCEL,
                                    on_click=lambda e, c=candidato: print(f"Rejeitar {c['nome']}"),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ),
                ]
            )
            for candidato in candidatos_pendentes
        ]
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
    cartao_votacao_fechada.border = ft.border.all(0.5, ft.Colors.GREY_500)

    # tabela candidatos disponiveis

    # BASE PRO RESPONSIVE ROW

    container_candidatos = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(col={"lg": 2, "md": 1, "xs": 1}),
                ft.Container(
                    content=candidatos_disponiveis,
                    col={"xs": 12, "md": 12, "lg": 8},
                ),
                ft.Container(col={"lg": 2,"md": 3}),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )



    # PÁGINA FINAL
    page.add(
        ft.Column(
            [
                container_inicial,
                espacamento,
                titulo_votacoes,
                espacamento2,  # Espaçamento entre seções
                cartao_votacao_atual,
                espacamento2,  # Espaçamento entre seções
                botao_criar_votacao,
                espacamento,  # Espaçamento entre seções
                titulo_votacoes_fechadas,
                espacamento2,  # Espaçamento entre seções
                cartao_votacao_fechada,
                espacamento,  # Espaçamento entre seções
                container_candidatos_pendentes,
                espacamento2,  # Espaçamento entre seções
                tabela_candidatos_pendentes,
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
 