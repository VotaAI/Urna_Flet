import flet as ft
import requests

def dashboard(page: ft.Page):
    id_votacao = "id_votacao"  # Placeholder para o ID da votação, se necessário
    page.title = "Vota AÍ"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    user_type = page.client_storage.get("user_type")
    print(f"\n\n\n\n\n\nUSER TYPE: {user_type}\n\n\n\n\n\n")

    # Configurações iniciais
    limite_aberto = 3
    limite_fechado = 3

    # ESPAÇAMENTOS
    espacamento = ft.Container(height=100)
    espacamento2 = ft.Container(height=20)
    espacamento3 = ft.Container(height=10)

    #######################################################################
    ##### ABAIXO É A PARTE DE AUTENTICAÇÃO E CONFIGURAÇÕES GERAIS #####
    #######################################################################

    def login():
        url = "https://backend-api-urna.onrender.com/login"
        payload = {"username": "string", "password": "string"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url, data=payload, headers=headers)
        return response.json() if response.status_code == 200 else None

    login = login()
    token, user_type = (login["access_token"], user_type) if login else (None, None)

    #######################################################################
    ##### ABAIXO É A PARTE DE GERENCIAMENTO DE CANDIDATOS #####
    #######################################################################

    def debug_acao(tipo, candidato):
        print(f"\n{'='*50}")
        print(f"{tipo.upper()} candidato:")
        print(f"ID: {candidato['id_candidatura']}")
        print(f"Nome: {candidato['nome_completo']}")
        print(f"Votação: {candidato['titulo']}")
        print(f"Detalhes: {candidato['detalhes'] or 'Sem detalhes'}")
        print("="*50 + "\n")

    def carregar_candidatos(status="pendentes"):
        response = requests.get(
            f"https://backend-api-urna.onrender.com/candidaturas/{status}",
            headers={"Authorization": f"Bearer {token}"}
        )
        return response.json() if response.status_code == 200 else []

    def aprovar_candidatura(e, candidato):
        try:
            print(f"\nTentando aprovar candidato {candidato['nome_completo']}")
            response = requests.put(
                f"https://backend-api-urna.onrender.com/admin/candidaturas/{candidato['id_candidatura']}",
                json={"detalhes": candidato['detalhes'] or "", "status": "aprovada"},
                headers={"Authorization": f"Bearer {token}"}
            )
            
            debug_acao("aprovou", candidato)
            print(f"Resposta da API: {response.status_code} - {response.text}")
            atualizar_tabelas()
        except Exception as e:
            print(f"Erro ao aprovar candidatura: {str(e)}")

    def recusar_candidatura(e, candidato):
        try:
            print(f"\nTentando recusar candidato {candidato['nome_completo']}")
            response = requests.put(
                f"https://backend-api-urna.onrender.com/admin/candidaturas/{candidato['id_candidatura']}",
                json={"detalhes": candidato['detalhes'] or "", "status": "recusada"},
                headers={"Authorization": f"Bearer {token}"}
            )
            
            debug_acao("recusou", candidato)
            print(f"Resposta da API: {response.status_code} - {response.text}")
            atualizar_tabelas()
        except Exception as e:
            print(f"Erro ao recusar candidatura: {str(e)}")

    def aprovar_todos(e):
        print("\n=== APROVANDO TODOS OS CANDIDATOS PENDENTES ===")
        candidatos = carregar_candidatos("pendentes")
        for candidato in candidatos:
            aprovar_candidatura(None, candidato)

    def rejeitar_todos(e):
        print("\n=== REJEITANDO TODOS OS CANDIDATOS PENDENTES ===")
        candidatos = carregar_candidatos("pendentes")
        for candidato in candidatos:
            recusar_candidatura(None, candidato)

    def atualizar_tabelas():
        try:
            print("\nAtualizando tabelas...")
            pendentes = carregar_candidatos("pendentes")
            aprovados = carregar_candidatos("aprovadas")
            recusados = carregar_candidatos("recusadas")
            
            print(f"Encontrados: {len(pendentes)} pendentes, {len(aprovados)} aprovados, {len(recusados)} recusados")
            
            tab_candidatos.tabs[0].content.rows = criar_linhas_tabela(pendentes, "pendentes")
            tab_candidatos.tabs[1].content.rows = criar_linhas_tabela(aprovados, "aprovadas")
            tab_candidatos.tabs[2].content.rows = criar_linhas_tabela(recusados, "recusadas")
            
            page.update()
            print("Tabelas atualizadas com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar tabelas: {str(e)}")

    def criar_linhas_tabela(candidatos, status):
        linhas = []
        for candidato in candidatos:
            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(candidato["nome_completo"])),
                    ft.DataCell(ft.Text(candidato["titulo"])),
                    ft.DataCell(ft.Text(candidato["detalhes"] or "-")),
                    ft.DataCell(
                        ft.Row([
                            ft.ElevatedButton(
                                "Aprovar",
                                on_click=lambda e, c=candidato: aprovar_candidatura(e, c),
                                visible=status == "pendentes"
                            ),
                            ft.ElevatedButton(
                                "Recusar",
                                on_click=lambda e, c=candidato: recusar_candidatura(e, c),
                                visible=status == "pendentes"
                            ),
                            ft.Text("✅ Aprovado", visible=status == "aprovadas"),
                            ft.Text("❌ Recusado", visible=status == "recusadas"),
                        ], spacing=5)
                    )
                ]
            )
            linhas.append(linha)
        return linhas

    # Configuração da interface de gerenciamento de candidatos
    tab_candidatos = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(
                text="Pendentes",
                content=ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Candidato")),
                        ft.DataColumn(ft.Text("Votação")),
                        ft.DataColumn(ft.Text("Detalhes")),
                        ft.DataColumn(ft.Text("Ações")),
                    ],
                    rows=[]
                )
            ),
            ft.Tab(
                text="Aprovados",
                content=ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Candidato")),
                        ft.DataColumn(ft.Text("Votação")),
                        ft.DataColumn(ft.Text("Detalhes")),
                        ft.DataColumn(ft.Text("Status")),
                    ],
                    rows=[]
                )
            ),
            ft.Tab(
                text="Recusados",
                content=ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Candidato")),
                        ft.DataColumn(ft.Text("Votação")),
                        ft.DataColumn(ft.Text("Detalhes")),
                        ft.DataColumn(ft.Text("Status")),
                    ],
                    rows=[]
                )
            ),
        ],
        expand=1
    )

    container_candidatos_pendentes = ft.Container(
        content=ft.Column([
            ft.Text("Gerenciamento de Candidaturas", size=30, weight=ft.FontWeight.BOLD),
            ft.Row([
                ft.ElevatedButton(
                    "Aprovar Todos",
                    on_click=aprovar_todos
                ),
                ft.ElevatedButton(
                    "Recusar Todos",
                    on_click=rejeitar_todos
                ),
            ], spacing=20),
            ft.Container(
                content=tab_candidatos,
                height=400,
                border=ft.border.all(1, ft.Colors.GREY_400),
                border_radius=ft.border_radius.all(5),
            )
        ]),
        padding=20
    )

    #######################################################################
    ##### ACIMA É A PARTE DE GERENCIAMENTO DE CANDIDATOS #####
    #######################################################################

    #######################################################################
    ##### ABAIXO É A PARTE DE VOTAÇÕES E LAYOUT PRINCIPAL #####
    #######################################################################

    # Carregar dados iniciais da API
    candidatos_pendentes_api = requests.get(
        "https://backend-api-urna.onrender.com/candidaturas/pendentes?limit=3&offset=0",
        headers={"Authorization": f"Bearer {token}"} if token else {}
    ).json() or []

    votacoes_fechadas_api = requests.get(
        "https://backend-api-urna.onrender.com/votacoes/closed?limit=3&offset=0"
    ).json() or []

    votacoes_abertas_api = requests.get(
        "https://backend-api-urna.onrender.com/votacoes/open?limit=3&offset=0"
    ).json() or []

    # Funções para votações
    def ir_tela_votacao(id_votacao):
        page.client_storage.set("id_votacao", id_votacao)
        page.go(f"/sobre")
    
    def gerar_callback_ir_tela(id_votacao):
        return lambda e: ir_tela_votacao(id_votacao)

    def ver_mais_aberto(e):
        nonlocal limite_aberto, cartoes_votacoes
        limite_aberto += 3
        novos_dados = requests.get(f"https://backend-api-urna.onrender.com/votacoes/open?limit={limite_aberto}&offset=0").json()
        cartoes_votacoes.clear()
        
        for votacao in novos_dados:
            id_votacao = votacao['id_votacao']
            cartao = criar_cartao_votacao(votacao, id_votacao)
            cartoes_votacoes.append(cartao)

        cartao_votacao_atual.controls = cartoes_votacoes
        page.update()
        
    def ver_mais_fechado(e):
        nonlocal limite_fechado, cartoes_votacoes_fechadas
        limite_fechado += 3
        novos_dados = requests.get(f"https://backend-api-urna.onrender.com/votacoes/closed?limit={limite_fechado}&offset=0").json()
        cartoes_votacoes_fechadas.clear()
        
        for votacao in novos_dados:
            id_votacao = votacao['id_votacao']
            cartao = criar_cartao_votacao(votacao, id_votacao)
            cartoes_votacoes_fechadas.append(cartao)

        cartao_votacao_fechada.controls = cartoes_votacoes_fechadas
        page.update()

    def criar_cartao_votacao(votacao, id_votacao):
        return ft.Container(
            content=ft.ResponsiveRow(
                [
                    ft.Container(width=60, height=60, bgcolor=ft.Colors.GREY_300),
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"{votacao['titulo']}", weight=ft.FontWeight.BOLD, size=20),
                            ft.Text(f"Período: {votacao['data_inicio']} até {votacao['data_fim']}."),
                            ft.Text(f"Descrição: {votacao['descricao']}"),
                        ]),
                        expand=True,
                        padding=10,
                    ),
                    ft.Container(
                        content=ft.Row([
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
                        ]),
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
            margin=10,
            border=ft.border.all(1, ft.Colors.GREY_500),
        )

    # AppBar
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

    # Componentes da interface
    container_inicial = ft.Container(
        content=ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Text("Votações", size=30, weight=ft.FontWeight.BOLD),
                    espacamento2,
                    ft.Text("Veja o resultado de votações anteriores e quais votações estão ocorrendo no momento.", size=20),
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20,
                bgcolor=ft.Colors.SURFACE,
                alignment=ft.alignment.center,
            ),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # Votações abertas
    titulo_votacoes = ft.Text("Votações em Aberto", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START)
    cartoes_votacoes = [criar_cartao_votacao(votacao, votacao['id_votacao']) for votacao in votacoes_abertas_api]
    cartao_votacao_atual = ft.Column(cartoes_votacoes, scroll=ft.ScrollMode.AUTO)

    # Votações fechadas
    titulo_votacoes_fechadas = ft.Text("Votações Fechadas", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.START)
    cartoes_votacoes_fechadas = [criar_cartao_votacao(votacao, votacao['id_votacao']) for votacao in votacoes_fechadas_api]
    cartao_votacao_fechada = ft.Column(cartoes_votacoes_fechadas, scroll=ft.ScrollMode.AUTO)

    # Botões
    botao_criar_votacao = ft.FilledButton(
        text="CRIAR VOTAÇÃO",
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,
            color=ft.Colors.PRIMARY_CONTAINER,
            shape=ft.RoundedRectangleBorder(radius=4),
            padding=ft.Padding(40, 40, 40, 40),
        ),
        on_click=lambda e: page.go("/criar_votacao"),
        width=1000,
    )

    botao_ver_mais = ft.FilledButton(
        text="Ver Mais",
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,
            color=ft.Colors.PRIMARY_CONTAINER,
            shape=ft.RoundedRectangleBorder(radius=4),
            padding=ft.Padding(20, 20, 20, 20),
        ),
        on_click=ver_mais_aberto,
        width=230,
    )

    botao_ver_mais_fechado = ft.FilledButton(
        text="Ver Mais",
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,
            color=ft.Colors.PRIMARY_CONTAINER,
            shape=ft.RoundedRectangleBorder(radius=4),
            padding=ft.Padding(20, 20, 20, 20),
        ),
        on_click=ver_mais_fechado,
        width=230,
    )

    # Footer
    footer = ft.Container(
        content=ft.Column([
            ft.Text("VotaAÍ - Todos os direitos reservados © 2025", size=12, color=ft.Colors.ON_SURFACE_VARIANT, text_align=ft.TextAlign.CENTER),
            ft.Row([
                ft.TextButton(text="Política de Privacidade"),
                ft.TextButton(text="Termos de Uso"),
                ft.TextButton(text="Contato"),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20,
    )

    # Montagem da página
    elementos_pagina = [
        container_inicial,
        espacamento,
        titulo_votacoes,
        espacamento3,
        cartao_votacao_atual,
        botao_ver_mais,
        espacamento2,
        titulo_votacoes_fechadas,
        espacamento2,
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

    # Atualizar tabelas iniciais
    atualizar_tabelas()

    return ft.View(
        route="/dashboard",
        appbar=ft.AppBar(  
            leading=ft.Icon(ft.Icons.HOW_TO_VOTE),
            title=ft.Text("VotaAÍ"),
            center_title=False,
            actions=[
                ft.TextButton(text="Tela Inicial", on_click=lambda e: page.go("/votacoes")),
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