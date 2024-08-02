from flet import *
import pandas as pd

import classes, teste3


def main(page: Page):

    # page.theme_mode = ThemeMode.LIGHT
    # botao = classes.BotaoFilePicker(page)
    # nome = Text(botao.arquivo_nome)
    # page.add(botao.botao, nome)


    texto_arquivo_nome = Text(value='Nome:')
    texto_arquivo_caminho = Text(value='Arquivo:')
    texto_dados_df = Text(value='Dados:')
    botao = classes.BotaoFilePicker(page, return_nome=texto_arquivo_nome, return_arquivo=texto_arquivo_caminho, return_dados=texto_dados_df)
    page.add(botao.botao, texto_arquivo_nome, texto_arquivo_caminho, texto_dados_df)






app(target=main)
