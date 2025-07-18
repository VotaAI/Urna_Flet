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

    def criar_votacao(e):

        # Resetar mensagens de erro
        message_error_nome_votacao.text = ""
        message_error_descricao.text = ""
        message_error_periodo_inicio.text = ""
        message_error_periodo_termino.text = ""
        
        # Verificar campos vazios
        has_error = False
        
        if not nome_votacao_label.value:
            message_error_nome_votacao.value = "Coloque o nome da votação."
            has_error = True
        
        if not descricao_label.value:
            message_error_descricao.value = "Coloque descrição para a votação."
            has_error = True
        
        if not periodo_inicio_label.value:
            message_error_periodo_inicio.value = "Coloque uma data de inicio para a votação."
            has_error = True
        
        if not periodo_termino_label.value:
            message_error_periodo_termino.value = "Coloque uma data de finalização para a votação."
            has_error = True
        
        # Atualizar mensagens de erro
        message_error_nome_votacao.update()
        message_error_descricao.update()
        message_error_periodo_inicio.update()
        message_error_periodo_termino.update()
        
        if has_error:
            return

        try:
            if nome_votacao_label.value and descricao_label.value and periodo_inicio_label.value and periodo_termino_label.value:
                # Converter string para objeto datetime
                datetime_1,datetime_2 = datetime.strptime(periodo_inicio_label.value, "%d/%m/%Y"), datetime.strptime(periodo_termino_label.value, "%d/%m/%Y")

                # Converter para formato ISO 8601 (com Z para indicar UTC, se quiser)
                data_iso_inicio, data_iso_fim = datetime_1.isoformat() + "Z", datetime_2.isoformat() + "Z"

                url = 'https://backend-api-urna.onrender.com/admin/votacoes/'

                header = {
                    'accept': 'application/json',
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json'
                }

                data = {
                    "titulo": nome_votacao_label.value,
                    "descricao": descricao_label.value,
                    "status": "aberta",
                    "permite_candidatura": permitir,
                    "data_inicio": data_iso_inicio,
                    "data_fim": data_iso_fim
                    }
                
                response = requests.post(
                    url=url,
                    headers=header,
                    json=data
                )

                print("Status Code:", response.status_code)
                print("Resposta JSON:", response.json())

                id_votacao = response.json()["id_votacao"]

                url_candidatos = 'https://backend-api-urna.onrender.com/admin/opcoes/'

                header_candidatos = {
                    'accept': 'application/json',
                    'Authorization': f'Bearer {token}', 
                    'Content-Type': 'application/json'
                }

                for candidatos in informacoes_candidatos:
                    nome_candidato = candidatos.get("nome")
                    detalhes_candidato = candidatos.get("detalhes")

                    data_candidatos = {
                        "id_votacao": id_votacao,
                        "titulo": nome_candidato,
                        "detalhes": detalhes_candidato or ""
                    }

                    response_candidato = requests.post(
                        url=url_candidatos,
                        headers=header_candidatos,
                        json=data_candidatos
                    )

                    print("Status Code:", response_candidato.status_code)
                    print("Resposta JSON:", response_candidato.json())

        except ValueError:
            print("Preencha os campos.")

    def funcionalidade_adicionar(e):
        if candidatos_label.value:
            informacoes_candidatos.append({
                "nome": candidatos_label.value,
                "detalhes": detalhes_label.value
            })

            card_container = ft.Container()

            def remover_ultimo_candidato(ev):
                if candidatos_card.controls:
                    candidatos_card.controls.remove(card_container)
                    candidatos_card.update()

            icone_pessoa = ft.Container(content=ft.CircleAvatar(ft.Icon(name=ft.Icons.PERSON, size=55, color="#54799B"), radius=30, bgcolor="#3a3a3a"))

            apagar_btn = ft.ElevatedButton(text="Apagar", 
                                        style=ft.ButtonStyle(
                                            bgcolor="transparent", 
                                            overlay_color="transparent", 
                                            shadow_color="transparent", 
                                            color="#ffffff", 
                                            elevation=0, 
                                            text_style=ft.TextStyle(size=20)), 
                                            on_click=remover_ultimo_candidato)

            card_container.content = ft.Row(
                [
                    ft.Row(
                        [
                            icone_pessoa,
                            ft.Column([
                                ft.Text(candidatos_label.value, size=20, color="#ffffff"),
                                ft.Text(detalhes_label.value, size=16, color="#989898")
                            ], spacing=1)
                        ]
                    ),
                    apagar_btn
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )

            card_container.padding = 10
            card_container.bgcolor = "transparent"
            card_container.border_radius = 10
            card_container.expand = True
            card_container.border = ft.Border(bottom=ft.BorderSide(1, "#535353"))
            card_container.border_radius = ft.BorderRadius(bottom_left=0, bottom_right=0, top_left=0, top_right=0)

            candidatos_card.controls.append(card_container)
            candidatos_card.update()

            # Limpa os campos após adicionar
            candidatos_label.value = ""
            detalhes_label.value = ""
            detalhes_label.disabled = True
            detalhes_label.opacity = 0.6
            detalhes_label.update()
            candidatos_label.update()
        else:
            print("Campo de nome está vazio")

    def ativar(e):
        nonlocal permitir
        # periodo_inicio.opacity = 1
        # periodo_inicio.update()

        # periodo_inicio_label.disabled = False
        # periodo_inicio_label.opacity = 1
        # periodo_inicio_label.update()

        # periodo_termino.opacity = 1
        # periodo_termino.update()

        # periodo_termino_label.disabled = False
        # periodo_termino_label.opacity = 1
        # periodo_termino_label.update()

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

        permitir = True
        print(permitir)

        candidaturas_nao_btn.update()
        # return permitir

    def desativar(e):
        nonlocal permitir
        # periodo_inicio.opacity = 0.6
        # periodo_inicio.update()

        # periodo_inicio_label.disabled = True
        # periodo_inicio_label.opacity = 0.6
        # periodo_inicio_label.update()

        # periodo_termino.opacity = 0.6
        # periodo_termino.update()

        # periodo_termino_label.disabled = True
        # periodo_termino_label.opacity = 0.6
        # periodo_termino_label.update()

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

        permitir = False
        print(permitir)

        candidaturas_sim_btn.update()
        # return permitir

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
    nome_votacao_label = ft.TextField(hint_text="Insira o nome da votação", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    # message_error_nome_votacao = ft.Text("", color="red", size=16)
    nome_votacao_container = ft.Container(content=ft.Column([nome_votacao, nome_votacao_label, message_error_nome_votacao], spacing=1))    

    descricao = ft.Text("Descrição", size=18, color="#ffffff")
    descricao_label = ft.TextField(hint_text="Insira uma breve descrição", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    # message_error_descricao = ft.Text("", color="red", size=16)
    descricao_container = ft.Container(content=ft.Column([descricao, descricao_label, message_error_descricao], spacing=1))

    # categoria = ft.Text("Categoria", size=18, color="#ffffff")
    # categoria_label = ft.TextField(hint_text="Insira uma categoria para a votação", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    # categoria_container = ft.Container(content=ft.Column([categoria, categoria_label], spacing=1))

    candidaturas = ft.Text("Permitir Candidaturas?", size=18, color="#ffffff")
    candidaturas_sim_btn = ft.ElevatedButton(text="Sim", 
                                            color="#ffffff", 
                                            expand=True,
                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#3B3B3B", side=ft.BorderSide(width=2, color="#ffffff")), 
                                            height=45,
                                            on_click=ativar)
    
    candidaturas_nao_btn = ft.ElevatedButton(text="Não", 
                                            color="#ffffff", 
                                            expand=True, 
                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#3B3B3B", side=ft.BorderSide(width=2, color="#ffffff")), 
                                            height=45,
                                            on_click=desativar)
    
    descricao_candidatura = ft.Text("", color="#98989898")
    candidaturas_btn_container = ft.Container(content=ft.Row([candidaturas_sim_btn, candidaturas_nao_btn]))
    candidaturas_container = ft.Container(content=ft.Column([candidaturas, candidaturas_btn_container, descricao_candidatura], spacing=1)) 

    periodo_inicio = ft.Text("Data de Início", size=18, opacity=1, color="#ffffff")
    periodo_inicio_label = ft.TextField(disabled=False, bgcolor="#FFFFFF", opacity=1, color="#000000", border_radius=10, border_color="#352A2A", hint_text="dd-mm-yyyy")
    # message_error_periodo_inicio = ft.Text("", color="red", size=16)
    periodo_inicio_container = ft.Container(content=ft.Column([periodo_inicio, periodo_inicio_label, message_error_periodo_inicio], spacing=1))

    periodo_termino = ft.Text("Data de Término", size=18, opacity=1, color="#ffffff")
    periodo_termino_label = ft.TextField(disabled=False, bgcolor="#ffffff", opacity=1, color="#000000", border_radius=10, border_color="#352A2A", on_change=formatar_data_termino, hint_text="dd-mm-yyyy")
    # message_error_periodo_termino = ft.Text("", color="red", size=16)
    periodo_termino_container = ft.Container(content=ft.Column([periodo_termino, periodo_termino_label, message_error_periodo_termino], spacing=1))

    candidatos = ft.Text("Registrar opção/candidato", size=18, color="#FFFFFF")
    candidatos_label = ft.TextField(hint_text="Insira um(a) opcao/candidato", bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    candidatos_container = ft.Container(content=ft.Column([candidatos, candidatos_label], spacing=1))

    candidatos_label.on_change = ativar_detalhes

    detalhes = ft.Text("Detalhes", size=18, opacity=0.6, color="#ffffff")
    detalhes_label = ft.TextField(hint_text="Insira informações da(o) opcao/candidato", disabled=True, opacity=0.6, bgcolor="#ffffff", color="#000000", border_radius=10, border_color="#352A2A")
    detalhes_container = ft.Container(content=ft.Column([detalhes, detalhes_label], spacing=1))

    adicionar_btn = ft.ElevatedButton(
        text="Adicionar", 
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor="#3B3B3B", color="#ffffff"), 
        expand=True,
        height=45,
        on_click=funcionalidade_adicionar)
    
    adicionar_btn_container = ft.Container(content=ft.Row([adicionar_btn]))
    
    opcoes_disponiveis_titulo = ft.Text("Opções disponíveis", size=32, color="#ffffff")

    opcoes_disponiveis_titulo_container = ft.Container(content=ft.Row([opcoes_disponiveis_titulo], alignment=ft.MainAxisAlignment.START))
    opcoes_disponiveis_cards_container = ft.Container(content=ft.Column([candidatos_card], alignment=ft.MainAxisAlignment.START, expand=True))

    voltar_btn = ft.ElevatedButton(
        text="Voltar",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), color="#ffffff", side=ft.BorderSide(width=2, color="#ffffff"), text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
        expand=True,
        height=45,
        bgcolor="#303030"
        )
    
    criar_btn = ft.ElevatedButton(
        text="Criar Votação",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),bgcolor="#ffffff", color="#000000", text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
        expand=True,
        height=45,
        on_click=criar_votacao
    )

    criar_voltar_btn_container = ft.Container(
        content=ft.Row([voltar_btn, criar_btn], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        padding=ft.padding.only(right=100, left=100)
    )

    container_labels = ft.Container(
            content=ft.ResponsiveRow(
                [
                    ft.Container(col={"xl": 3,"md": 2, "sm": 1}),
                    ft.Container(
                        content=ft.Column([nome_votacao_container, 
                                    descricao_container, 
                                    # categoria_container,
                                    candidaturas_container, 
                                    periodo_inicio_container, 
                                    periodo_termino_container, 
                                    candidatos_container, 
                                    detalhes_container,
                                    adicionar_btn_container,
                                    opcoes_disponiveis_titulo_container,
                                    opcoes_disponiveis_cards_container,
                                    criar_voltar_btn_container], spacing=30),
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

ft.app(main)