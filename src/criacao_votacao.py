import flet as ft

def main(page: ft.Page):
    page.title = "Criar votação"
    page.bgcolor = "#303030"

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
    
    titulo = ft.Text("Configurar Nova Votação")
    sub_titulo = ft.Text("Defina os detalhes da votação que deseja criar.")

    btn_cancelar = ft.ElevatedButton(
        text="Cancelar",
        bgcolor="#ffffff",
        color="#000000",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
    
    btn_salvar = ft.ElevatedButton(
        text="Salvar",
        bgcolor="#000000",
        color="#ffffff",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
    
    container_btn = ft.Container(content=ft.Row([btn_cancelar, btn_salvar], spacing=25, alignment=ft.MainAxisAlignment.CENTER))
    
    container_titulo = ft.Container(
        content=ft.Column([titulo, sub_titulo, container_btn], spacing=25, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        alignment=ft.alignment.center
    )

    # detalhes_votacao = ft.Text("Detalhes da Votação")

    nome_votacao = ft.Text("Nome da Votação")
    nome_votacao_label = ft.TextField(hint_text="Insira o nome da votação")
    nome_votacao_container = ft.Container(content=ft.Column([nome_votacao, nome_votacao_label]))    

    descricao = ft.Text("Descrição")
    descricao_label = ft.TextField(hint_text="Insira uma breve descrição")
    descricao_container = ft.Container(content=ft.Column([descricao, descricao_label]))

    categoria = ft.Text("Categoria")
    categoria_label = ft.TextField(hint_text="Insira uma categoria para a votação")
    categoria_container = ft.Container(content=ft.Column([categoria, categoria_label]))

    candidaturas = ft.Text("Permitir Candidaturas?")
    candidaturas_sim_btn = ft.ElevatedButton(text="Sim")
    candidaturas_nao_btn = ft.ElevatedButton(text="Não")
    descricao_candidatura = ft.Text("Escolha se os participantes podem se candidatar.")
    candidaturas_btn_container = ft.Container(content=ft.Row([candidaturas_sim_btn, candidaturas_nao_btn]))
    candidaturas_container = ft.Container(content=ft.Column([candidaturas, candidaturas_btn_container, descricao_candidatura])) 

    periodo_inicio = ft.Text("data de Início")
    periodo_inicio_label = ft.TextField(disabled=True)
    # descricao_periodo = ft.Text("Preencha caso a opção acima seja 'Sim'")
    periodo_inicio_container = ft.Container(content=ft.Column([periodo_inicio, periodo_inicio_label]))

    periodo_termino = ft.Text("Data de Término")
    periodo_termino_label = ft.TextField(disabled=True)
    periodo_termino_container = ft.Container(content=ft.Column([periodo_termino, periodo_termino_label]))

    candidatos = ft.Text("Registrar opção/candidato")
    candidatos_label = ft.TextField(hint_text="Insira um(a) opcao/candidato")
    candidatos_container = ft.Container(content=ft.Column([candidatos, candidatos_label]))

    detalhes = ft.Text("Detalhes")
    detalhes_label = ft.TextField(hint_text="Insira informações da(o) opcao/candidato", disabled=True)
    detalhes_container = ft.Container(content=ft.Column([detalhes, detalhes_label]))

    adicionar_btn = ft.ElevatedButton(
        text="Adicionar", 
        style=ft.ButtonStyle(bgcolor="#3b3b3b", color="#ffffff"), 
        expand=True)
    
    opcoes_disponiveis_titulo = ft.Text("Opções disponíveis")

    voltar_btn = ft.ElevatedButton(
        text="Voltar",
        style=ft.ButtonStyle(color="#ffffff")
        )
    
    criar_btn = ft.ElevatedButton(
        text="Criar Votação",
        style=ft.ButtonStyle(bgcolor="#ffffff", color="#000000")
    )

    container_labels = ft.Container(
        content=ft.Column([nome_votacao_container, descricao_container, categoria_container, candidaturas_container, periodo_inicio_container, periodo_termino_container, candidatos_container, detalhes_container])
    )

    page.add(container_titulo)

ft.app(main)