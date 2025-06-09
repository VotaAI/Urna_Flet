import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    status = ft.Container(
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

    title = ft.Text("Nome da votação")
    periodo = ft.Text("Período: 30/05/2025 até 06/06/2025.")
    descricao = ft.Text("Descrição: Votação para eleição do novo Representante de Classe.")

    votacao_detalhes = ft.Column(
        controls=[title,periodo,descricao]
    )

    votacao = ft.Container(
        content=votacao_detalhes
    )
    
    row = ft.Row(
        width=800,
        controls=[votacao,status,excluir]
    )

    pendentes = ft.Text("Candidatos pendentes", size=34)
    pendentes_detalhes = ft.Text("Aprovar ou rejeitar candidatos")

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

    row_candidatos_pendentes = ft.Row(
        controls=[aceitar_todos,rejeitar_todos],
        alignment=ft.alignment.center,
    )

    col_candidatos_pendentes = ft.Column(
        controls=[pendentes, pendentes_detalhes, row_candidatos_pendentes],
        alignment=ft.alignment.center,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=800,
        height=200
    )

    nome_candidato = ft.Text("NOME DO CANDIDATO")
    candidato_votacao = ft.Text("Votação a qual se candidatou")

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

    candidato_info = ft.Column(
        controls=[nome_candidato,candidato_votacao]
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

        ft.Container(
            content=row,
            margin=5
        ),

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

        ft.Container(
            content=row,
            margin=20
        ),

        ft.Container(
            content=col_candidatos_pendentes,
            alignment=ft.alignment.center,
            width=800,
            height=600
        ),

        candidato_template,
    ),

ft.app(main)
