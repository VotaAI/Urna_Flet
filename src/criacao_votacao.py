import flet as ft

def main(page: ft.Page):
    page.title = "Criar votação"
    page.bgcolor = "#303030"
    page.scroll=True

    def ativar(e):
        periodo_inicio.opacity = 1
        periodo_inicio.update()

        periodo_inicio_label.disabled = False
        periodo_inicio_label.opacity = 1
        periodo_inicio_label.update()

        periodo_termino.opacity = 1
        periodo_termino.update()

        periodo_termino_label.disabled = False
        periodo_termino_label.opacity = 1
        periodo_termino_label.update()

        candidaturas_sim_btn.style = ft.ButtonStyle(
            side=ft.BorderSide(width=2, color="#0400FF"),
            bgcolor="#3B3B3B",
            color="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        candidaturas_sim_btn.update()

        candidaturas_nao_btn.style = ft.ButtonStyle(
            side=ft.BorderSide(width=2, color="transparent"),
            bgcolor="#3B3B3B",
            color="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        candidaturas_nao_btn.update()

    def desativar(e):
        periodo_inicio.opacity = 0.6
        periodo_inicio.update()

        periodo_inicio_label.disabled = True
        periodo_inicio_label.opacity = 0.6
        periodo_inicio_label.update()

        periodo_termino.opacity = 0.6
        periodo_termino.update()

        periodo_termino_label.disabled = True
        periodo_termino_label.opacity = 0.6
        periodo_termino_label.update()

        candidaturas_nao_btn.style = ft.ButtonStyle(
            side=ft.BorderSide(width=2, color="#0400FF"),
            bgcolor="#3B3B3B",
            color="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        candidaturas_nao_btn.update()

        candidaturas_sim_btn.style = ft.ButtonStyle(
            side=ft.BorderSide(width=2, color="transparent"),
            bgcolor="#3B3B3B",
            color="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        candidaturas_sim_btn.update()

    def ativar_detalhes(e):
        if candidatos_label.value:
            detalhes.opacity = 1
            detalhes.update()

            detalhes_label.opacity = 1
            detalhes_label.disabled = False
            detalhes_label.update()
        
        else:
            detalhes.opacity = 0.6
            detalhes.update()

            detalhes_label.opacity = 0.6
            detalhes_label.disabled = True
            detalhes_label.update()

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
    
    titulo = ft.Text("Votações", size=45, weight=ft.FontWeight.BOLD, color="#ffffff")
    sub_titulo = ft.Text("Defina os detalhes da votação que deseja criar.", size=16)
    
    container_titulo = ft.Container(
        content=ft.Column([titulo, sub_titulo], spacing=10, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        margin=ft.margin.only(top=20, bottom=20),
        alignment=ft.alignment.center
    )

    # detalhes_votacao = ft.Text("Detalhes da Votação")

    nome_votacao = ft.Text("Nome da Votação", size=18)
    nome_votacao_label = ft.TextField(hint_text="Insira o nome da votação", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    nome_votacao_container = ft.Container(content=ft.Column([nome_votacao, nome_votacao_label], spacing=1))    

    descricao = ft.Text("Descrição", size=18)
    descricao_label = ft.TextField(hint_text="Insira uma breve descrição", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    descricao_container = ft.Container(content=ft.Column([descricao, descricao_label], spacing=1))

    categoria = ft.Text("Categoria", size=18)
    categoria_label = ft.TextField(hint_text="Insira uma categoria para a votação", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    categoria_container = ft.Container(content=ft.Column([categoria, categoria_label], spacing=1))

    candidaturas = ft.Text("Permitir Candidaturas?", size=18)
    candidaturas_sim_btn = ft.ElevatedButton(text="Sim", 
                                            color="#ffffff", 
                                            expand=True,
                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#3B3B3B", side=ft.BorderSide(width=2, color="transparent")), 
                                            height=45,
                                            on_click=ativar)
    
    candidaturas_nao_btn = ft.ElevatedButton(text="Não", 
                                            color="#ffffff", 
                                            expand=True, 
                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#3B3B3B", side=ft.BorderSide(width=2, color="transparent")), 
                                            height=45,
                                            on_click=desativar)
    
    descricao_candidatura = ft.Text("Escolha se os participantes podem se candidatar.", color="#979797")
    candidaturas_btn_container = ft.Container(content=ft.Row([candidaturas_sim_btn, candidaturas_nao_btn]))
    candidaturas_container = ft.Container(content=ft.Column([candidaturas, candidaturas_btn_container, descricao_candidatura], spacing=1)) 

    periodo_inicio = ft.Text("Data de Início", size=18, opacity=0.6)
    periodo_inicio_label = ft.TextField(disabled=True, bgcolor="#FFFFFF", opacity=0.6, color="#000000", border_radius=10, border_color="#352A2A")
    periodo_inicio_container = ft.Container(content=ft.Column([periodo_inicio, periodo_inicio_label], spacing=1))

    periodo_termino = ft.Text("Data de Término", size=18, opacity=0.6)
    periodo_termino_label = ft.TextField(disabled=True, bgcolor="#ffffff", opacity=0.6, color="#000000", border_radius=10, border_color="#352A2A")
    periodo_termino_container = ft.Container(content=ft.Column([periodo_termino, periodo_termino_label], spacing=1))

    candidatos = ft.Text("Registrar opção/candidato", size=18)
    candidatos_label = ft.TextField(hint_text="Insira um(a) opcao/candidato", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    candidatos_container = ft.Container(content=ft.Column([candidatos, candidatos_label], spacing=1))

    candidatos_label.on_change = ativar_detalhes

    detalhes = ft.Text("Detalhes", size=18, opacity=0.6)
    detalhes_label = ft.TextField(hint_text="Insira informações da(o) opcao/candidato", disabled=True, opacity=0.6, bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    detalhes_container = ft.Container(content=ft.Column([detalhes, detalhes_label], spacing=1))

    adicionar_btn = ft.ElevatedButton(
        text="Adicionar", 
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#3B3B3B", color="#ffffff"), 
        expand=True,
        height=45)
    
    adicionar_btn_container = ft.Container(content=ft.Row([adicionar_btn]))
    
    opcoes_disponiveis_titulo = ft.Text("Opções disponíveis", size=32)
    opcoes_disponiveis_titulo_container = ft.Container(content=ft.Row([opcoes_disponiveis_titulo], alignment=ft.MainAxisAlignment.START))

    voltar_btn = ft.ElevatedButton(
        text="Voltar",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), color="#ffffff", side=ft.BorderSide(width=2, color="#ffffff")),
        expand=True,
        height=45
        )
    
    criar_btn = ft.ElevatedButton(
        text="Criar Votação",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),bgcolor="#ffffff", color="#000000"),
        expand=True,
        height=45
    )

    criar_voltar_btn_container = ft.Container(
        content=ft.Row([voltar_btn, criar_btn], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        padding=ft.padding.only(right=100, left=100)
    )

    container_labels = ft.Container(
        content=ft.Column([nome_votacao_container, 
                            descricao_container, 
                            categoria_container,
                            candidaturas_container, 
                            periodo_inicio_container, 
                            periodo_termino_container, 
                            candidatos_container, 
                            detalhes_container,
                            adicionar_btn_container,
                            opcoes_disponiveis_titulo_container,
                            criar_voltar_btn_container], spacing=30, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(right=550, left=550)
    )

    page.add(container_titulo, container_labels)

ft.app(main)