import flet as ft
import requests
from datetime import datetime

informacoes_candidatos = []

def main(page: ft.Page):
    page.title = "Criar votação"
    page.bgcolor = "#303030"
    page.scroll=True

    candidatos_card = ft.Column()

    permitir = False

    id = 17
    informacoes_labels = requests.get(f"https://backend-api-urna.onrender.com/votacoes/{id}").json()

    nome_votacao_info = informacoes_labels['titulo']
    descricao_info = informacoes_labels['descricao']
    permitir_candidatura = informacoes_labels['permite_candidatura']
    periodo_inicio_info = informacoes_labels['data_inicio']
    periodo_termino_info = informacoes_labels['data_fim']

    print(nome_votacao_info)
    print(descricao_info)
    print(periodo_inicio_info)
    print(periodo_termino_info)

    def formatar_data_inicio(e):
        texto = periodo_inicio_label.value
        numeros = ''.join(filter(str.isdigit, texto))[:8]  # Só números, máximo 8 dígitos

        novo_texto = ""
        if len(numeros) >= 1:
            novo_texto += numeros[:2]
        if len(numeros) >= 3:
            novo_texto = numeros[:2] + "/" + numeros[2:4]
        if len(numeros) >= 5:
            novo_texto = numeros[:2] + "/" + numeros[2:4] + "/" + numeros[4:8]

        # Atualiza apenas se o texto mudou (pra evitar loop)
        if novo_texto != texto:
            periodo_inicio_label.value = novo_texto
            periodo_inicio_label.update()

    def formatar_data_termino(e):
        texto = periodo_termino_label.value
        numeros = ''.join(filter(str.isdigit, texto))[:8]  # Só números, máximo 8 dígitos

        novo_texto = ""
        if len(numeros) >= 1:
            novo_texto += numeros[:2]
        if len(numeros) >= 3:
            novo_texto = numeros[:2] + "/" + numeros[2:4]
        if len(numeros) >= 5:
            novo_texto = numeros[:2] + "/" + numeros[2:4] + "/" + numeros[4:8]

        # Atualiza apenas se o texto mudou (pra evitar loop)
        if novo_texto != texto:
            periodo_termino_label.value = novo_texto
            periodo_termino_label.update()

    def obter_token(username, password):
        url = "https://backend-api-urna.onrender.com/login"

        payload = {
            "username": username,
            "password": password
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url, data=payload, headers=headers)

        # print("Status:", response.status_code)
        # print("Resposta:", response.text)

        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            return None

    token = obter_token("email", "senha")

    def salvar_votacao(e):
        try:
            # Converter string para objeto datetime
            datetime_2 = datetime.strptime(periodo_termino_label.value, "%d/%m/%Y")

            # Converter para formato ISO 8601 (com Z para indicar UTC, se quiser)
            data_iso_fim = datetime_2.isoformat() + "Z"

            url = f'https://backend-api-urna.onrender.com/admin/votacoes/{id}/'

            header = {
                'accept': 'application/json',
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }

            data = {
                "titulo": nome_votacao_label.value,
                "descricao": descricao_label.value,
                "status": "aberta",
                "data_fim": data_iso_fim
                }
            
            response = requests.put(
                url=url,
                headers=header,
                json=data
            )

            print("Status Code:", response.status_code)
            print("Resposta JSON:", response.json())

        except ValueError:
            print("Preencha os campos.")

    def ativar(e):
        nonlocal permitir

        permitir = True
        print(permitir)

    def desativar(e):
        nonlocal permitir

        

        permitir = False
        print(permitir)

    def ativar_design(e):
        candidaturas_sim_btn.style = ft.ButtonStyle(
            side=ft.BorderSide(width=2, color="#0400FF"),
            bgcolor="#3B3B3B",
            color="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        candidaturas_sim_btn.update()

        candidaturas_nao_btn.style = ft.ButtonStyle(
            side=ft.BorderSide(width=2, color="#ffffff"),
            bgcolor="#3B3B3B",
            color="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10)
        )
        
        candidaturas_nao_btn.update()
    
    def desativar_design(e):
        candidaturas_nao_btn.style = ft.ButtonStyle(
            side=ft.BorderSide(width=2, color="#0400FF"),
            bgcolor="#3B3B3B",
            color="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        candidaturas_nao_btn.update()

        candidaturas_sim_btn.style = ft.ButtonStyle(
            side=ft.BorderSide(width=2, color="#ffffff"),
            bgcolor="#3B3B3B",
            color="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10)
        )

        candidaturas_sim_btn.update()

    message_error_nome_votacao = ft.Text("", color="red", size=16)
    message_error_descricao = ft.Text("", color="red", size=16)
    message_error_periodo_inicio = ft.Text("", color="red", size=16)
    message_error_periodo_termino = ft.Text("", color="red", size=16)

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
    sub_titulo = ft.Text("Defina os detalhes da votação que deseja criar.", size=16, color="#ffffff")
    
    container_titulo = ft.Container(
        content=ft.Column([titulo, sub_titulo], spacing=10, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        margin=ft.margin.only(top=20, bottom=20),
        alignment=ft.alignment.center
    )

    # detalhes_votacao = ft.Text("Detalhes da Votação")

    nome_votacao = ft.Text("Nome da Votação", size=18, color="#ffffff")
    nome_votacao_label = ft.TextField(f"{nome_votacao_info}",hint_text="Insira o nome da votação", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    # message_error_nome_votacao = ft.Text("", color="red", size=16)
    nome_votacao_container = ft.Container(content=ft.Column([nome_votacao, nome_votacao_label, message_error_nome_votacao], spacing=1))    

    descricao = ft.Text("Descrição", size=18, color="#ffffff")
    descricao_label = ft.TextField(f"{descricao_info}", hint_text="Insira uma breve descrição", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    # message_error_descricao = ft.Text("", color="red", size=16)
    descricao_container = ft.Container(content=ft.Column([descricao, descricao_label, message_error_descricao], spacing=1))

    candidaturas = ft.Text("Permitir Candidaturas?", size=18, color="#ffffff", opacity=0.6)
    candidaturas_sim_btn = ft.ElevatedButton(text="Sim",
                                            color="#ffffff", 
                                            expand=True,
                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#3B3B3B", side=ft.BorderSide(width=2, color="#ffffff")), 
                                            height=45,
                                            on_click=lambda e: [ativar(e), ativar_design(e)],
                                            disabled=True,
                                            opacity=0.6)
    
    candidaturas_nao_btn = ft.ElevatedButton(text="Não", 
                                            color="#ffffff", 
                                            expand=True, 
                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#3B3B3B", side=ft.BorderSide(width=2, color="#ffffff")), 
                                            height=45,
                                            on_click=lambda e: [desativar(e), desativar_design(e)],
                                            disabled=True,
                                            opacity=0.6)
    
    descricao_candidatura = ft.Text("", color="#98989898")
    candidaturas_btn_container = ft.Container(content=ft.Row([candidaturas_sim_btn, candidaturas_nao_btn]))
    candidaturas_container = ft.Container(content=ft.Column([candidaturas, candidaturas_btn_container, descricao_candidatura], spacing=1)) 

    periodo_inicio = ft.Text("Data de Início", size=18, opacity=0.6, color="#ffffff")
    periodo_inicio_label = ft.TextField(f"{periodo_inicio_info}",disabled=True, bgcolor="#FFFFFF", opacity=0.6, color="#000000", border_radius=10, border_color="#352A2A", hint_text="dd-mm-yyyy")
    # message_error_periodo_inicio = ft.Text("", color="red", size=16)
    periodo_inicio_container = ft.Container(content=ft.Column([periodo_inicio, periodo_inicio_label, message_error_periodo_inicio], spacing=1))

    periodo_termino = ft.Text("Data de Término", size=18, opacity=1, color="#ffffff")
    periodo_termino_label = ft.TextField(f"{periodo_termino_info}", disabled=False, bgcolor="#ffffff", opacity=1, color="#000000", border_radius=10, border_color="#352A2A", on_change=formatar_data_termino, hint_text="dd-mm-yyyy")
    # message_error_periodo_termino = ft.Text("", color="red", size=16)
    periodo_termino_container = ft.Container(content=ft.Column([periodo_termino, periodo_termino_label, message_error_periodo_termino], spacing=1))

    cancelar_btn = ft.ElevatedButton(
        text="Cancelar",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), color="#ffffff", side=ft.BorderSide(width=2, color="#ffffff"), text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
        expand=True,
        height=45,
        bgcolor="#303030"
        )
    
    salvar_btn = ft.ElevatedButton(
        text="Salvar Votação",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),bgcolor="#ffffff", color="#000000", text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
        expand=True,
        height=45,
        on_click=salvar_votacao
    )

    salvar_cancelar_btn_container = ft.Container(
        content=ft.Row([cancelar_btn, salvar_btn], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        padding=ft.padding.only(right=100, left=100)
    )

    resetar_votos_btn = ft.ElevatedButton(
        text="Resetar Votos",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),bgcolor="#ffffff", color="#000000", text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
        expand=True,
        height=45
        )
    
    deletar_btn = ft.ElevatedButton(
        text="Deletar",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), color="#ffffff", side=ft.BorderSide(width=2, color="#ffffff"), text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
        expand=True,
        height=45,
        bgcolor="#303030"
        )
    
    resetar_votos_deletar_btn_container = ft.Container(
        content=ft.Row([resetar_votos_btn, deletar_btn], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        padding=ft.padding.only(right=100, left=100)
    )

    btn_container = ft.Container(
        content=ft.Column([salvar_cancelar_btn_container, resetar_votos_deletar_btn_container]) 
    )

    container_labels = ft.Container(
            content=ft.ResponsiveRow(
                [
                    ft.Container(col={"xl": 3,"md": 2, "sm": 1}),
                    ft.Container(
                        content=ft.Column([nome_votacao_container, 
                                    descricao_container, 
                                    candidaturas_container, 
                                    periodo_inicio_container, 
                                    periodo_termino_container, 
                                    btn_container], spacing=30),
                                    alignment=ft.alignment.center,
                                    col={"xl": 6,"md": 8, "sm": 10}
                        ),
                        ft.Container(col={"xl": 3,"md": 2, "sm": 1})
                ]
            )
        )
        
    
    
    campo_erro_map = {
        nome_votacao_label: message_error_nome_votacao,
        descricao_label: message_error_descricao,
        periodo_inicio_label: message_error_periodo_inicio,
        periodo_termino_label: message_error_periodo_termino
    }

    def limpar_erro_campo(campo):
        campo_erro_map[campo].value = ""
        campo_erro_map[campo].update()
    
    nome_votacao_label.on_change = lambda e: limpar_erro_campo(nome_votacao_label)
    descricao_label.on_change = lambda e: limpar_erro_campo(descricao_label)
    periodo_inicio_label.on_change = lambda e: [limpar_erro_campo(periodo_inicio_label), formatar_data_inicio(e)]
    periodo_termino_label.on_change = lambda e: [limpar_erro_campo(periodo_termino_label), formatar_data_termino(e)]

    page.add(container_titulo, container_labels)

    if permitir:
        pass
        
    
    elif not permitir:

        pass

    if permitir_candidatura == True:
        ativar(None)
        ativar_design(None)
    elif permitir_candidatura == False:
        desativar(None)
        desativar_design(None)

    print(permitir)

ft.app(main)