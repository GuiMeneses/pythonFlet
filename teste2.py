from flet import *
import pandas as pd

import classes, teste3


def main(page: Page):

    # page.theme_mode = ThemeMode.LIGHT
    # botao = classes.BotaoFilePicker(page)
    # nome = Text(botao.arquivo_nome)
    # page.add(botao.botao, nome)

    botao = teste3.example()
    page.add(botao)

app(target=main)
