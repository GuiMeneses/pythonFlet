from flet import *
import flet as ft

def main(page: ft.Page):

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

            Container(
                bgcolor=colors.BLACK54,
                expand=3,
                alignment=alignment.center,
                border_radius=30,
                padding=10,
                content=Column(
                    auto_scroll=True,
                    adaptive=True,
                    alignment=alignment.center,
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=1,
                    controls=[Row([Container(content=cl_novos_dados, expand=1), Container(content=cl_intervalo, expand=1), Container(content=cl_check_box)]), Container(
                        alignment=alignment.center,
                        content=CupertinoFilledButton(content=Text('+', size=30), on_click=lambda e: adicionar_linha(), border_radius=5, padding=padding.only(bottom=5))
                    )]

                )
            ),
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