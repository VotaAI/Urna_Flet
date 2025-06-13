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

    #################################### -------------------------- ######################################

    # INICIO DA PARTE ESSENCIAL PRO BACK END

    # TABELA DE CANDIDATOS
    candidatos_nome = ["Candidato A", "Candidato B", "Candidato C"]
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
                            ft.Text(
                                f"Categoria: {sobre_a_votacao['categoria']}",
                                size=15,
                            ),
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
    page.add(
        ft.Column(
            [
                espacamento,
                container_inicial,
                espacamento2,
                container_area_votacao,
                espacamento,
                espacamento2,
                footer,
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
