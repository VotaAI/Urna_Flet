import flet as ft
import  requests

def tela_sobre_votacao(page: ft.Page):

    id = page.client_storage.get("user_id")
    token = page.client_storage.get("token")
    id_votacao = page.client_storage.get("id_votacao")
    url = f"https://backend-api-urna.onrender.com/votacoes/{id_votacao}"
    url_votacoes_opcoes = f"https://backend-api-urna.onrender.com/{id_votacao}/opcoes"

    

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    response_opcoes = requests.get(url_votacoes_opcoes, headers=headers)
    if response_opcoes.status_code == 200:
        opcoes_votacao = response_opcoes.json()
        print(opcoes_votacao)
    else:
        print("Erro ao buscar opções de votação:", response_opcoes.status_code)

    if response.status_code == 200:
        dados_votacao = response.json()
        print(dados_votacao)
    else:
        print("Erro ao buscar dados:", response.status_code)

    # ESPAÇAMENTOS
    espacamento = ft.Container(height=100)  # Espaçamento entre seções
    espacamento2 = ft.Container(height=20)  # Espaçamento entre seções

    #################################### -------------------------- ######################################

    # INICIO DA PARTE ESSENCIAL PRO BACK END

    # TABELA DE CANDIDATOS
    candidatos_nome = ["Candidato A", "Candidato B", "Candidato C"]
    numero_candidato = ["001", "002", "003"]

    candidatos_disponiveis = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Opção")),
            ft.DataColumn(ft.Text("Número")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("titulo")),
                    ft.DataCell(ft.Text("id_votacao")),
                ]
            )
            # for opcao in opcoes_votacao
        ]
    )

    # DICIONÁRIO COM INFORMAÇÕES SOBRE A VOTAÇÃO
    sobre_a_votacao = {
        "titulo": "Votação de Representantes", 
        "inicio": "01/06/2025",
        "fim": "31/06/2025",
        "descricao": "Participe da votação para escolher os representantes do nosso projeto. Vote no candidato de sua preferência digitando o número correspondente.",
        "status": "Aberta",
        "categoria": "Educação",
        "permite_candidatura": True,
    }

    # FIM DA PARTE ESSENCIAL PRO BACK END
    #################################### -------------------------- ######################################

    # CONTAINER INICIAL
    container_inicial = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(col={"lg": 1, "md": 1, "xs": 1}),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(F"{dados_votacao['titulo']}", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            ft.Text(
                                f"Início: {dados_votacao['data_inicio']} - Fim: {dados_votacao['data_fim']}",
                                size=15,
                            ),
                            ft.Text(
                                f"Descrição: {dados_votacao['descricao']}",
                                size=15,
                            ),
                            ft.Text(
                                f"Status: {dados_votacao['status']}",
                                size=15,
                            ),
                            #ft.Text(
                             #   f"Categoria: {sobre_a_votacao['categoria']}",
                             #   size=15,
                            #),
                            espacamento2,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.SURFACE,
                    alignment=ft.alignment.center,
                    col={"xs": 12, "md": 12, "lg": 10},
                ),
                ft.Container(col={"lg": 1,"md": 3}),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    # area votação

    container_area_votacao = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(col={"lg": 1, "md": 1, "xs": 1}),
                ft.Container(
                    content=candidatos_disponiveis,
                    col={"xs": 12, "md": 12, "lg": 10},
                ),
                ft.Container(col={"lg": 1,"md": 3}),
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

    return ft.View(
        route="/sobre_a_votacao",
        appbar=ft.AppBar(
            leading=ft.Icon(ft.Icons.HOW_TO_VOTE),
            title=ft.Text("VotaAÍ"),
            center_title=False,
            actions=[
                ft.TextButton(text="Tela Inicial", on_click=lambda e: page.go("/dashboard_usuario")),
            ],
        ),
        controls=[
                espacamento,
                container_inicial,
                espacamento2,
                container_area_votacao,
                espacamento,
                espacamento2,
                footer,
        ],
        scroll=ft.ScrollMode.AUTO
    )
