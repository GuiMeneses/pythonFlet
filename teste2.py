from flet import *
import pandas as pd

import classes


def main(page: Page):

    botao = classes.BotaoFilePicker(page)
    page.theme_mode = ThemeMode.LIGHT
    page.update()
    page.add(botao.botao)


app(target=main)
