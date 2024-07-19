from flet import *
import flet as ft
import classes

def main(page: ft.Page):

    # variaveis da coluna de informações
    dados = Column()
    array_novos_dados = []
    array_intervalo = []
    array_VF = []

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

    cl_novos_dados = Column()
    cl_intervalo = Column()
    cl_check_box = Column()

    cl_novos_dados.controls.append(Text('Novos dados'))
    cl_intervalo.controls.append(Text('Intervalo'))
    cl_check_box.controls.append(Text('V/F'))

    def adicionar_linha():
        cl_novos_dados.controls.append(TextField())
        cl_intervalo.controls.append(TextField())
        cl_check_box.controls.append(Checkbox())
        page.update()



    coluna_informacoes = Container(
        bgcolor=colors.AMBER_800,
        padding=40,
        expand=1,
        content=Column([

            classes.tabela_dados(page, dados, array_novos_dados, array_intervalo, array_VF).tabela(),
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