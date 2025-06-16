import flet as ft
import requests
import matplotlib.pyplot as plt
import io
import base64

def main(page: ft.Page):
    page.title = "Vota AÍ"
    page.theme_mode = ft.ThemeMode.LIGHT
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

    id_votacao = 1
    votos_resultados = requests.get(f"https://backend-api-urna.onrender.com/votacoes/{id_votacao}/votos").json()

    # Ordena os resultados pelos votos (do maior para o menor)
    top_3 = sorted(votos_resultados, key=lambda x: x["total_votos"], reverse=True)[:3]

    # Cria as listas apenas com os 3 primeiros
    nome_candidato = [opcao['id_opcao'] for opcao in top_3]
    quantidade_votos = [opcao['total_votos'] for opcao in top_3]


    # Gerar gráfico com matplotlib e salvar em buffer
    plt.figure(figsize=(5, 3))
    plt.bar(nome_candidato, quantidade_votos, color='red')
    plt.xticks(rotation=45)
    plt.ylabel('Votos')
    plt.xlabel('Candidatos')
    plt.title('Resultado da Votação')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()

    # Exibir no Flet como imagem
    image_widget = ft.Image(src_base64=image_base64, width=600, height=400)

    page.add(image_widget)

ft.app(target=main)
