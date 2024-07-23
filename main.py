from flet import *
import flet as ft
import classes

def main(page: Page):

    # variaveis da coluna de informações
    dados = Column()
    array_novos_dados = []
    array_intervalo = []
    array_vf = []

    # page.adaptive = True
    coluna_tabelas = Container(
        bgcolor=colors.BLUE_300,
        padding=40,
        expand=2,
        content=Column(
            [
                Container(
                    bgcolor=colors.BLACK54,
                    content=Text('Opa'),
                    expand=1,
                    alignment=alignment.center,
                    border_radius=30,


                ),
                Container(
                    bgcolor=colors.BLACK54,
                    content=Text('Opa'),
                    expand=1,
                    alignment=alignment.center,
                    border_radius=30,
                ),

            ],
            expand=True,
        ),

    )





    coluna_informacoes = Container(
        bgcolor=colors.AMBER_800,
        padding=40,
        expand=1,
        content=Column([

            classes.TabelaDados(page, dados, array_novos_dados, array_intervalo, array_vf).tabela(),
            Container(
                bgcolor=colors.BLACK54,
                content=Text('Opa'),
                expand=1,
                alignment=alignment.center,
                border_radius=30,

            ),
        ])

    )


    page.add(Row([coluna_tabelas, coluna_informacoes,],
                 expand=True,
                 ))

ft.app(main)