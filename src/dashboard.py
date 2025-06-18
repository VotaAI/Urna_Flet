import flet as ft
import requests

def dashboard(page: ft.Page):
    id_votacao = "id_votacao"  # Placeholder para o ID da votação, se necessário
    page.title = "Vota AÍ"
    page.theme_mode = ft.ThemeMode.LIGHT # trocar modo por aqui
    page.scroll = ft.ScrollMode.AUTO
    user_type = page.client_storage.get("user_type")
    print(f"\n\n\n\n\n\nUSER TYPE: {user_type}\n\n\n\n\n\n")

    def login():
        url = "https://backend-api-urna.onrender.com/login"

        payload = {
            "username": "string",
            "password": "string"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url, data=payload, headers=headers)

        # print("Status:", response.status_code)
        # print("Resposta:", response.text)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    login = login()


    if login:
        token, user_type = login["access_token"], user_type
    else:
        token, user_type = None




    def aprovar_candidatura(id_candidatura, detalhes):
        url = f"https://backend-api-urna.onrender.com/admin/candidaturas/{id_candidatura}"

        payload = {
            "detalhes": detalhes or "",
            "status": "aprovada"
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.put(url, json=payload, headers=headers)

        print("Status:", response.status_code)
        print("Resposta:", response.text)





    def recusar_candidatura(id_candidatura, detalhes):
        url = f"https://backend-api-urna.onrender.com/admin/candidaturas/{id_candidatura}"

        payload = {
            "detalhes": detalhes or "",
            "status": "recusada"
        }

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.put(url, json=payload, headers=headers)

        print("Status:", response.status_code)
        print("Resposta:", response.text)




    def aprovar_todos():
        print("\n\n\n\n\nAPROVANDO TODOS BRRRRRRRRRRRRRRRR")
        for candidato in candidatos_pendentes_api:
            aprovar_candidatura(candidato["id_candidatura"], candidato["detalhes"])




    def rejeitar_todos():
        for candidato in candidatos_pendentes_api:
            url = f"https://backend-api-urna.onrender.com/admin/candidaturas/{candidato['id_candidatura']}"

            payload = {
                "detalhes": candidato['detalhes'] or "",
                "status": "recusada"
            }

            headers = {
                'accept': 'application/json',
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }

            response = requests.put(url, json=payload, headers=headers)

            print("Status:", response.status_code)
            print("Resposta:", response.text)


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


    limite_aberto = 3
    limite_fechado = 3

    def ver_mais_aberto(e):
        nonlocal limite_aberto, cartoes_votacoes

        limite_aberto += 3  # Aumenta o limite

        # Faz nova requisição com o novo limite
        novos_dados = requests.get(f"https://backend-api-urna.onrender.com/votacoes/open?limit={limite_aberto}&offset=0").json()

        # Limpa os cartões antigos
        cartoes_votacoes.clear()

        # Recria os cartões
        for votacao in novos_dados:
            id_votacao = votacao['id_votacao']
            cartao = ft.Container(
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
                                    ft.Text(f"{votacao['titulo']}", weight=ft.FontWeight.BOLD, size=20),
                                    ft.Text(f"Período: {votacao['data_inicio']} até {votacao['data_fim']}."),
                                    ft.Text(f"Descrição: {votacao['descricao']}"),
                                ]
                            ),
                            expand=True,
                            padding=10,
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.FilledButton(
                                        text="Detalhes",
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                            color=ft.Colors.PRIMARY_CONTAINER,
                                            shape=ft.RoundedRectangleBorder(radius=4),
                                            padding=ft.Padding(40, 20, 40, 20),
                                        ),
                                        on_click=gerar_callback_ir_tela(id_votacao),
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
                width=1000,
                alignment=ft.alignment.center,
                margin=10,  # <-- Isso aqui separa visualmente os cartões
                border=ft.border.all(1, ft.Colors.GREY_500),  # <-- Adiciona uma borda ao redor
            )

            cartoes_votacoes.append(cartao)

        # Atualiza o container que exibe os cartões
        cartao_votacao_atual.controls = cartoes_votacoes
        page.update()
        
    
    def ver_mais_fechado(e):
        nonlocal limite_fechado, cartoes_votacoes_fechadas

        limite_fechado += 3

        novos_dados = requests.get(f"https://backend-api-urna.onrender.com/votacoes/closed?limit={limite_fechado}&offset=0").json()

        cartoes_votacoes_fechadas.clear()

        for votacao in novos_dados:
            id_votacao = votacao['id_votacao']  # Pega o ID da votação para usar no botão de detalhes
            cartao = ft.Container(
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
                                                ft.Text(f"{votacao['titulo']}", weight=ft.FontWeight.BOLD, size=20),
                                                ft.Text(f"Período: {votacao['data_inicio']} até {votacao['data_fim']}."),
                                                ft.Text(f"Descrição: {votacao['descricao']}"),
                                            ]
                                        ),
                                        expand=True,
                                        padding=10,
                                    ),
                                    ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.FilledButton(
                                                    text="Detalhes",
                                                    style=ft.ButtonStyle(
                                                        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                                        color=ft.Colors.PRIMARY_CONTAINER,
                                                        shape=ft.RoundedRectangleBorder(radius=4),
                                                        padding=ft.Padding(40, 20, 40, 20),
                                                    ),
                                                    on_click=gerar_callback_ir_tela(id_votacao),
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
                            width=1000,
                            alignment=ft.alignment.center,
                            margin=10,  # <-- Isso aqui separa visualmente os cartões
                            border=ft.border.all(1, ft.Colors.GREY_500),  # <-- Adiciona uma borda ao redor
                        )
            
            cartoes_votacoes_fechadas.append(cartao)

            cartao_votacao_fechada.controls = cartoes_votacoes_fechadas

            page.update()


    candidatos_aprovados_api = requests.get("https://backend-api-urna.onrender.com/candidaturas/aprovadas?limit=3&offset=0").json()

    candidatos_recusados_api = requests.get("https://backend-api-urna.onrender.com/candidaturas/recusadas?limit=3&offset=0").json()

    candidatos_pendentes_api = requests.get("https://backend-api-urna.onrender.com/candidaturas/pendentes?limit=3&offset=0").json()

    votacoes_fechadas_api = requests.get(f"https://backend-api-urna.onrender.com/votacoes/closed?limit={limite_fechado}&offset=0").json()

    votacoes_abertas_api = requests.get(f"https://backend-api-urna.onrender.com/votacoes/open?limit={limite_aberto}&offset=0").json()






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

    cartoes_votacoes = []

    def ir_tela_votacao(id_votacao):
            page.client_storage.set("id_votacao", id_votacao)
            print(f"ID da votação para ir à tela: {id_votacao}")  # Debug: Verifica o ID da votação
            page.go(f"/sobre")
    
    def gerar_callback_ir_tela(id_votacao):
        print(f"Gerando callback para ID da votação: {id_votacao}")  # Debug: Verifica o ID da votação
        return lambda e: ir_tela_votacao(id_votacao)

    for votacao in votacoes_abertas_api:
        id_votacao = votacao['id_votacao']  # Pega o ID da votação para usar no botão de detalhes
        print(f"ID da votação: {id_votacao}")  # Debug: Verifica o ID da votação
        cartao = ft.Container(
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
                                ft.Text(f"{votacao['titulo']}", weight=ft.FontWeight.BOLD, size=20),
                                ft.Text(f"Período: {votacao['data_inicio']} até {votacao['data_fim']}."),
                                ft.Text(f"Descrição: {votacao['descricao']}"),
                            ]
                        ),
                        expand=True,
                        padding=10,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.FilledButton(
                                    text="Detalhes",
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                        color=ft.Colors.PRIMARY_CONTAINER,
                                        shape=ft.RoundedRectangleBorder(radius=4),
                                        padding=ft.Padding(40, 20, 40, 20),
                                    ),
                                    on_click=gerar_callback_ir_tela(id_votacao),
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
            width=1000,
            alignment=ft.alignment.center,
            margin=10,  # <-- Isso aqui separa visualmente os cartões
            border=ft.border.all(1, ft.Colors.GREY_500),  # <-- Adiciona uma borda ao redor
        )

        cartoes_votacoes.append(cartao)


    cartao_votacao_atual =ft.Column(
            cartoes_votacoes,
            scroll=ft.ScrollMode.AUTO,  # Se quiser scrollável
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
    


    botao_ver_mais = ft.FilledButton(
                                        text="Ver Mais",
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.PRIMARY_CONTAINER,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                padding=ft.Padding(20, 20, 20, 20),  # aumenta o tamanho (deixa mais quadrado)
                                                
                                            ),
                                            on_click=ver_mais_aberto,
                                            width=230,
                                        )
    
    botao_ver_mais_fechado = ft.FilledButton(
                                        text="Ver Mais",
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.PRIMARY_CONTAINER,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                padding=ft.Padding(20, 20, 20, 20),  # aumenta o tamanho (deixa mais quadrado)
                                                
                                            ),
                                            on_click=ver_mais_fechado,
                                            width=230,
                                        )




    # CONTAINER VOTAÇÕES FECHADAS
    titulo_votacoes_fechadas = ft.Text(
        "Votações Fechadas",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.START,
    )

    cartoes_votacoes_fechadas = []

    for votacao in votacoes_fechadas_api:
        id_votacao = votacao['id_votacao']  # Pega o ID da votação para usar no botão de detalhes
        cartao = ft.Container(
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
                                ft.Text(f"{votacao['titulo']}", weight=ft.FontWeight.BOLD, size=20),
                                ft.Text(f"Período: {votacao['data_inicio']} até {votacao['data_fim']}."),
                                ft.Text(f"Descrição: {votacao['descricao']}"),
                            ]
                        ),
                        expand=True,
                        padding=10,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.FilledButton(
                                    text="Detalhes",
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
                                        color=ft.Colors.PRIMARY_CONTAINER,
                                        shape=ft.RoundedRectangleBorder(radius=4),
                                        padding=ft.Padding(40, 20, 40, 20),
                                    ),
                                    on_click=gerar_callback_ir_tela(id_votacao),
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
            width=1000,
            alignment=ft.alignment.center,
            margin=10,  # <-- Isso aqui separa visualmente os cartões
            border=ft.border.all(1, ft.Colors.GREY_500),  # <-- Adiciona uma borda ao redor
        )

        cartoes_votacoes_fechadas.append(cartao)


    cartao_votacao_fechada =ft.Column(
            cartoes_votacoes_fechadas,
            scroll=ft.ScrollMode.AUTO,  # Se quiser scrollável
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
                                on_click=lambda e: rejeitar_todos(),
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
                                on_click=lambda e: aprovar_todos(),
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
            ft.DataColumn(ft.Text("Nome da votação")),
            ft.DataColumn(ft.Text("Descrição")),
            ft.DataColumn(ft.Text("Ações")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(candidato["nome_completo"])),
                    ft.DataCell(ft.Text(candidato["titulo"])),
                    ft.DataCell(ft.Text(candidato["detalhes"])),
                    ft.DataCell(
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.Icons.CHECK,
                                    on_click=lambda e, c=candidato: aprovar_candidatura(c["id_candidatura"], c["detalhes"]),
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.CANCEL,
                                    on_click=lambda e, c=candidato: recusar_candidatura(c["id_candidatura"], c["detalhes"]),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ),
                ]
            )
            for candidato in candidatos_pendentes_api
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






    elementos_pagina =  [
                container_inicial,
                espacamento,
                titulo_votacoes,
                espacamento3,  # Espaçamento entre seções
                cartao_votacao_atual,
                botao_ver_mais,
                espacamento2,  # Espaçamento entre seções
                titulo_votacoes_fechadas,
                espacamento2,  # Espaçamento entre seções
                cartao_votacao_fechada,
                botao_ver_mais_fechado,
            ]

    if user_type == "admin":
        elementos_pagina.extend([
            espacamento2,
            botao_criar_votacao,
            espacamento,
            container_candidatos_pendentes,
            espacamento
        ])

    elementos_pagina.extend([espacamento, footer])

    page.add(ft.Column(
        elementos_pagina,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ))






    # PÁGINA FINAL
    # page.add(
    #     ft.Column(
    #         [
    #             container_inicial,
    #             espacamento,
    #             titulo_votacoes,
    #             espacamento2,  # Espaçamento entre seções
    #             cartao_votacao_atual,
    #             espacamento2,  # Espaçamento entre seções
    #             botao_criar_votacao,
    #             espacamento,  # Espaçamento entre seções
    #             titulo_votacoes_fechadas,
    #             espacamento2,  # Espaçamento entre seções
    #             cartao_votacao_fechada,
    #             espacamento,  # Espaçamento entre seções
    #             container_candidatos_pendentes,
    #             espacamento2,  # Espaçamento entre seções
    #             tabela_candidatos_pendentes,
    #             espacamento,
    #             footer,
    #         ],
    #         expand=True,
    #         scroll=ft.ScrollMode.AUTO,
    #         alignment=ft.MainAxisAlignment.START, 
    #         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #     )
    # )

    return ft.View(
        route="/dashboard",
        appbar=ft.AppBar(  
            leading=ft.Icon(ft.Icons.HOW_TO_VOTE),
            title=ft.Text("VotaAÍ"),
            center_title=False,
            actions=[
                ft.TextButton(text="Tela Inicial", on_click=lambda e: page.go("/dashboard_usuario")),
            ],
        ),
        controls=[ft.Column(
            elementos_pagina,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            
        )]
    )


 