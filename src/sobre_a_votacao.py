import flet as ft
import requests
from datetime import datetime

def tela_sobre_votacao(page: ft.Page):
    page.title = "Vota AÍ"
    page.theme_mode = ft.ThemeMode.LIGHT # trocar modo por aqui
    page.scroll = ft.ScrollMode.AUTO

    text_msg_ao_votar = ft.Text('')

    print(page.client_storage.get("id_user"))

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

    id_votacao = page.client_storage.get("id_votacao")
    if id_votacao is None:
        page.go("/votacoes")
        return

    detalhes_votacao = requests.get(f"https://backend-api-urna.onrender.com/votacoes/{id_votacao}").json()
    opcoes_disponiveis = requests.get(f"https://backend-api-urna.onrender.com/votacoes/{id_votacao}/opcoes").json()
    votos_resultados = requests.get(f"https://backend-api-urna.onrender.com/votacoes/{id_votacao}/votos").json()

    print(f"\n\n\n\n\n\nDETALHES DA VOTAÇÃO: {detalhes_votacao}\n\n\n\n\n")
    print(f"\n\n\n\n\n\nOPÇÕES DISPONÍVEIS: {opcoes_disponiveis}\n\n\n\n\n")
    print(f"\n\n\n\n\n\n\n{votos_resultados}\n\n\n\n\n")

    vencedor_titulo = ''
    vencedor_votos = 0
    vencedor_votos_str = '0 Votos'

    def encontrar_votos(titulo):
        nonlocal vencedor_titulo
        nonlocal vencedor_votos
        nonlocal vencedor_votos_str

        for opcao in votos_resultados:
            print(f"COMPARANDO ENTRE {titulo} E {opcao['id_opcao']}")
            print(f"Vencedor titulo {vencedor_titulo}, vencedor_votos {vencedor_votos}\n\n\n\n\n")
            if opcao["id_opcao"] == titulo:

                if opcao["total_votos"] > vencedor_votos:
                    vencedor_titulo = opcao["id_opcao"]
                    vencedor_votos, vencedor_votos_str =  opcao["total_votos"], f'{opcao["total_votos"]} Votos'

                elif opcao["total_votos"] == vencedor_votos and vencedor_votos!=0:
                    vencedor_titulo+= f', e {opcao["id_opcao"]}'

                return opcao["total_votos"]
        return 0

    id_user = page.client_storage.get("id_user")

    def criar_botao_votar(id_opcao):
        btn = ft.FilledButton(
            text="Votar",
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # se adapta bem a temas claros e escuros
                color=ft.Colors.PRIMARY_CONTAINER,
                shape=ft.RoundedRectangleBorder(radius=4),  # cantos levemente arredondados (mude para 0 se quiser 100% quadrado)
                padding=ft.Padding(10, 10, 10, 10),  # aumenta o tamanho (deixa mais quadrado)
                
            ),
            on_click=lambda e, id_opcao_btn=id_opcao: votar(id_opcao),
            width=120,
        )
        return btn


    # ESPAÇAMENTOS
    espacamento = ft.Container(height=100)  # Espaçamento entre seções
    espacamento2 = ft.Container(height=20)  # Espaçamento entre seções

    def votar(id_opcao):
        nonlocal text_msg_ao_votar
        msg_field = text_msg_ao_votar
        if detalhes_votacao["status"] == "aberta":
            url = "https://backend-api-urna.onrender.com/votos"

            payload = {
                "id_user": id_user,
                "id_votacao": id_votacao,
                "id_opcao": id_opcao,
                "data_voto": str(datetime.utcnow()),
            }

            headers = {
                'accept': 'application/json',
                "Content-Type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                try:
                    msg_field.value = response.json()["msg"]
                    msg_field.size = 40
                    page.update()
                except:
                    print(f"\n\n\n\n\n{response.json()}\n\n\n\n\n\n")
                    msg_field.value= 'SEU VOTO FOI REGISTRADO'
                    msg_field.size = 40
                    page.update()
                    return
            else:
                msg_field.value = response.json()["msg"]
                msg_field.size = 40
                page.update()
        else:
            msg_field.value = 'NÃO É POSSÍVEL VOTAR EM UMA VOTAÇÃO FECHADA'
            msg_field.size = 40
            page.update()







    if votos_resultados == "Votação e/ou opções não encontradas":
        tabela_com_votos = ft.Text(
            "Nenhum voto registrado ou opções disponíveis para esta votação.",
            size=20,
            color=ft.Colors.RED_400,
            text_align=ft.TextAlign.CENTER,
        )
    else:
        tabela_com_votos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Candidato")),
            ft.DataColumn(ft.Text("Detalhes")),
            ft.DataColumn(ft.Text("Quantidade de Votos")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(candidato["titulo"])),
                    ft.DataCell(ft.Text(candidato["detalhes"])),
                    ft.DataCell(ft.Text(str(encontrar_votos(candidato["titulo"])))),
                ]
            )
            for candidato in opcoes_disponiveis
        ]
    )

    #################################### -------------------------- ######################################

    # INICIO DA PARTE ESSENCIAL PRO BACK END

    # TABELA DE CANDIDATOS

    if opcoes_disponiveis == {'msg': 'Votação e/ou opções não encontradas'}:
        candidatos_disponiveis = ft.Text(
            "Nenhum candidato disponível para esta votação.",
            size=20,
            color=ft.Colors.RED_400,
            text_align=ft.TextAlign.CENTER,
        )
    else:
        candidatos_disponiveis = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Opção")),
                ft.DataColumn(ft.Text("Candidato")),
                ft.DataColumn(ft.Text("Detalhes")),
                ft.DataColumn(ft.Text("Votar"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(opcoes_disponiveis.index(candidato)+1))),
                        ft.DataCell(ft.Text(candidato["titulo"])),
                        ft.DataCell(ft.Text(candidato["detalhes"])),
                        ft.DataCell(criar_botao_votar(candidato["id_opcao"])),
                    ]
                )
                for candidato in opcoes_disponiveis
            ]
        )




#criar_botao_votar(candidato["id_opcao"])





    # DICIONÁRIO COM INFORMAÇÕES SOBRE A VOTAÇÃO
    if detalhes_votacao == None:
        sobre_a_votacao = {
            "titulo": "Votação não encontrada", 
            "inicio": "N/A",
            "fim": "N/A",
            "descricao": "N/A",
            "status": "N/A".title(),
            # "categoria": "Educação",
            "permite_candidatura": False,
        }
    else:
        sobre_a_votacao = {
            "titulo": detalhes_votacao["titulo"], 
            "inicio": detalhes_votacao["data_inicio"],
            "fim": detalhes_votacao["data_fim"],
            "descricao": detalhes_votacao["descricao"],
            "status": detalhes_votacao["status"].title(),
            # "categoria": "Educação",
            "permite_candidatura": detalhes_votacao["permite_candidatura"],
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
                            ft.Text(F"{sobre_a_votacao['titulo']}", size=30, weight=ft.FontWeight.BOLD),
                            espacamento2,
                            ft.Text(
                                f"Início: {sobre_a_votacao['inicio']} - Fim: {sobre_a_votacao['fim']}",
                                size=15,
                            ),
                            ft.Text(
                                f"Descrição: {sobre_a_votacao['descricao']}",
                                size=15,
                            ),
                            ft.Text(
                                f"Status: {sobre_a_votacao['status']}",
                                size=15,
                            ),
                            # ft.Text(
                            #     f"Categoria: {sobre_a_votacao['categoria']}",
                            #     size=15,
                            # ),
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
        route="/sobre",
        appbar=ft.AppBar(
            leading=ft.Icon(ft.Icons.HOW_TO_VOTE),
            title=ft.Text("VotaAÍ"),
            center_title=False,
            actions=[
                ft.TextButton(text="Tela Inicial", on_click=lambda e: page.go("/dashboard_usuario")),
            ],
        ),
        controls=[
                ft.Column(
                    [
                        espacamento,
                        container_inicial,
                        espacamento2,
                        text_msg_ao_votar,
                        container_area_votacao,
                        espacamento,
                        espacamento,
                        tabela_com_votos,
                        espacamento,
                        footer,
                    ],
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
        ],
    
    )
