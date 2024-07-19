from flet import *
import flet as ft
import classes
def main(page: ft.Page):

    dados = Column()
    array_novos_dados = []
    array_intervalo = []
    array_VF = []


    page.add(classes.tabela_dados(page, dados, array_novos_dados, array_intervalo, array_VF).tabela())

ft.app(main)