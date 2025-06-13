import flet as ft
from requests import get

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    votacoes_abertas = get("https://backend-api-urna.onrender.com/votacoes/open?limit=3&offset=0").json()
    votacoes_fechadas = get("https://backend-api-urna.onrender.com/votacoes/closed?limit=3&offset=0").json()
    candidatos_pendentes = get("https://backend-api-urna.onrender.com/candidaturas/pendentes?limit=3&offset=0").json()

    votacoes_abertas_exibicao = []
    votacoes_fechadas_exibicao = []
    candidatos_pendentes_lista = []


    def criar_exibicao_votacao(id_votacao, titulo, descricao, data_inicio, data_fim, status, list):
        btn_status = ft.Container(
            content=ft.Text("Status", color=ft.Colors.WHITE),
            width=200,
            height=40,
            bgcolor=ft.Colors.BLACK,
            alignment=ft.alignment.center,
            border_radius=10,
            ink=True,
            on_click=lambda e: print("Clickable transparent with Ink clicked!"),
        )
        excluir = ft.Container(
            content=ft.Text("Excluir", color=ft.Colors.WHITE),
            width=200,
            height=40,
            bgcolor=ft.Colors.BLACK,
            alignment=ft.alignment.center,
            border_radius=10,
            ink=True,
            on_click=lambda e: print("Clickable transparent with Ink clicked!"),
        )

        title = ft.Text(titulo)
        periodo = ft.Text(f"Período: {data_inicio} até {data_fim}.")
        description = ft.Text(f"Descrição: {descricao}")

        votacao_detalhes = ft.Column(
            controls=[title,periodo,description]
        )

        votacao = ft.Container(
            content=votacao_detalhes
        )

        row = ft.Container(
            content=ft.Row(
                width=800,
                controls=[votacao,btn_status,excluir],
            ),
            margin=20  # ou ft.Margin(top=10, left=10, right=10, bottom=10)
        )

        list.append(row)

    for votacao in votacoes_abertas:
        criar_exibicao_votacao(votacao["id_votacao"], votacao["titulo"], votacao["descricao"], votacao["data_inicio"], votacao["data_fim"], votacao["status"], votacoes_abertas_exibicao)

    for votacao in votacoes_fechadas:
        criar_exibicao_votacao(votacao["id_votacao"], votacao["titulo"], votacao["descricao"], votacao["data_inicio"], votacao["data_fim"], votacao["status"], votacoes_fechadas_exibicao)

    aceitar_todos = ft.Container(
        content=ft.Text("Aceitar todos",color=ft.Colors.BLACK),
        alignment=ft.alignment.center,
        #border=ft.Border(2,2,2,2),
        bgcolor=ft.Colors.WHITE,
        width=100,
        height=40,
        border_radius=10,
        ink=True,
        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
    )

    rejeitar_todos = ft.Container(
        content=ft.Text("Rejeitar todos"),
        alignment=ft.alignment.center,
        #border=ft.Border(2,2,2,2),
        width=100,
        height=40,
        border_radius=10,
        ink=True,
        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
    )






    pendentes = ft.Text("Candidatos pendentes", size=34)
    pendentes_detalhes = ft.Text("Aprovar ou rejeitar candidatos")

    row_candidatos_pendentes = ft.Row(
        controls=[aceitar_todos,rejeitar_todos],
        alignment=ft.alignment.center,
    )

    col_candidatos_pendentes = ft.Column(
        controls=[pendentes, pendentes_detalhes, row_candidatos_pendentes],
        alignment=ft.alignment.center,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=800,
        height=500
    )

    aprovar_candidato = ft.Container(
        content=ft.Text("Aprovar"),
        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
        height=30,
        width=70,
    )

    rejeitar_candidato = ft.Container(
        content=ft.Text("Rejeitar"),
        on_click=lambda e: print("Clickable transparent with Ink clicked!"),
        height=30,
        width=70,
    )

    def criar_candidato_exibicao(nome, detalhes, votacao):
        nome_candidato = ft.Text("NOME DO CANDIDATO")
        candidato_detalhes = ft.Text("Detalhes")
        candidato_votacao = ft.Text("Votação a qual se candidatou")
        candidato_info = ft.Column(
            controls=[nome_candidato,candidato_detalhes, candidato_votacao]
        )

        controles_candidato = ft.Row(
            controls=[aprovar_candidato,rejeitar_candidato]
        )

        # img_candidato = ft.Image(
        #     src='frame.svg',
        #     width=100,
        #     height=100,
        #     fit=ft.ImageFit.CONTAIN,
        # )

        candidato_template = ft.Row(
            controls=[candidato_info,controles_candidato],
            #alignment=ft.alignment.center,
            width=800,
            spacing=450
        )
        candidatos_pendentes_lista.append(candidato_template)

    for candidato in candidatos_pendentes:
        criar_candidato_exibicao(candidato["id_user"], candidato["detalhes"], candidato["id_votacao"])

    page.add(
        ft.Container(
            content=ft.Text("Votações", size=30),
            alignment=ft.alignment.center,
        ),

        ft.Container(
            content=ft.Text("Veja o resultado de votações anteriores e quais votações estão\nocorrendo no momento"),
            alignment=ft.alignment.center,
        ),

        ft.Container(
            content=ft.Text("Votações em aberto", size=34),
            alignment=ft.alignment.center_left,
            width=800,
            margin=10
        ),

        *votacoes_abertas_exibicao,

        ft.Container(
            content=ft.Text("Criar Votação", color=ft.Colors.BLACK),
            margin=50,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            width=800,
            height=60,
            border_radius=5,
            ink=True,
            on_click=lambda e: print("Clickable transparent with Ink clicked!"),
        ),

        ft.Container(
            content=ft.Text("Votações Fechadas", size=34),
            alignment=ft.alignment.center_left,
            width=800,
        ),

        *votacoes_fechadas_exibicao,

        ft.Container(
            content=col_candidatos_pendentes,
            alignment=ft.alignment.center,
            width=800,
            height=600
        ),

        *candidatos_pendentes_lista,
    ),

ft.app(main)
