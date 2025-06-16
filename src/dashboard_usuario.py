import flet as ft
import requests

def tela_dashboard_usuario(page: ft.Page):

    id = page.client_storage.get("user_id")
    token = page.client_storage.get("token")
    id_votacao = "teste"
    id_votacao = page.client_storage.get("id_votacao")
    page.client_storage.remove("id_votacao")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = f"https://backend-api-urna.onrender.com/users/{id}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dados_usuario = response.json()
        print(dados_usuario)
    else:
        print("Erro ao buscar dados:", response.status_code)


    # ESPAÇAMENTOS
    espacamento = ft.Container(height=100)  # Espaçamento entre seções
    espacamento2 = ft.Container(height=20)  # Espaçamento entre seções
    espacamento3 = ft.Container(height=10)  # Espaçamento entre seções

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
    
    # pegando votacoes atuais da api

    def ir_tela_votacao(id_votacao):
            page.client_storage.set("id_votacao", id_votacao)
            page.go(f"/sobre_a_votacao")
    
    def gerar_callback_ir_tela(id_votacao):
        return lambda e: ir_tela_votacao(id_votacao)


    json_votacoes_abertas = requests.get("https://backend-api-urna.onrender.com/votacoes/open?limit=10&offset=0").json()
    lista = []

    for votacao in json_votacoes_abertas:
        id_votacao = votacao['id_votacao']
        print(f"ID da Votação: {id_votacao}")  # Debugging para verificar o ID da votação
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
                                        ft.Text(f"Título: {votacao['titulo']}.", weight=ft.FontWeight.BOLD),
                                        ft.Text(f"Período: {votacao['data_inicio']} até {votacao['data_fim']}."),
                                        ft.Text(f"Descrição: {votacao['descricao']}."),
                                    ]
                                ),
                                expand=True,
                                padding=10,
                            ),
                            ft.Column(
                                
                                    [
                                        ft.Row(
                                            [
                                                espacamento3,
                                                ft.FilledButton(text="CANDIDATAR-SE", width=160, style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.ON_TERTIARY,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                ),),
                                                ft.FilledButton(text="VOTAR", width=160, style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.ON_TERTIARY,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                ),),
                                            ]
                                        ),
                                        ft.Row(
                                            [
                                                espacamento3,
                                                ft.FilledButton(text="MAIS INFORMAÇÕES", width=160, style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                                                color=ft.Colors.ON_TERTIARY,
                                                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                                                ), on_click=gerar_callback_ir_tela(id_votacao)),
                                            ]
                                        ),
                                    ],
                  
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    border_radius=10,
                    padding=15,
                    width=1500,  # <-- Aqui você define a "largura máxima"
                    alignment=ft.alignment.center,  # <-- Aqui centraliza horizontalmente
                )
        cartao_votacao_atual.border = ft.border.all(0.5, ft.Colors.GREY_500)
        lista.append(cartao_votacao_atual)

    
        

    votacoes_dinamicas = ft.Container(
        content=ft.Column(lista, spacing=20),
        padding=20,
        alignment=ft.alignment.center
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
    votacoes_atuais_titulo = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(col={"lg": 2}),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Votações Atuais", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            votacoes_dinamicas,
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

    return ft.View(
        route="/dashboard_usuario",
        appbar=ft.AppBar(
            leading=ft.Icon(ft.Icons.HOW_TO_VOTE),
            title=ft.Text("VotaAÍ"),
            center_title=False,
            actions=[
                ft.TextButton(text="Tela Inicial", on_click=lambda e: page.go("/dashboard_usuario")),
            ],
        ),
        controls=[
                container_inicial,
                espacamento, # Espaçamento entre seções
                container_votacao_fechada,
                espacamento,  # Espaçamento entre seções
                votacoes_atuais_titulo,
                espacamento,
                footer,
        ],
        scroll=ft.ScrollMode.AUTO
    )



