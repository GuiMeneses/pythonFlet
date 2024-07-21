from flet import *
import flet as ft
import pandas as pd


def main(page: ft.Page):

    tabela_teste = pd.read_excel('arquivos/excel_teste.xlsx', header=None)
    def container_tabela(arquivo_tabela):
        coluna_principal = Column()

        for index, row in arquivo_tabela.iterrows():
            linha = []
            for coluna in arquivo_tabela.columns:
                valor = row[coluna]
                linha.append(valor)
            print(linha)
            containers = Row()
            for i in range(len(linha)):
                containers.controls.append(Container(expand=1, content=Text(linha[i])))
            coluna_principal.controls.append(Container(expand=1, content=containers))





        page.update()
        return Container(
            border=border.all(5, color=colors.BLACK),
            border_radius=30,
            expand=1,
            content=coluna_principal
        )



    coluna_tabelas = Container(
        bgcolor=colors.BLUE_300,
        padding=40,
        expand=2,
        content=Container(
                    bgcolor=colors.BLACK54,
                    expand=1,
                    alignment=alignment.center,
                    border_radius=30,
                    content=container_tabela(tabela_teste),

                ),

    )

    page.add(coluna_tabelas)

ft.app(main)