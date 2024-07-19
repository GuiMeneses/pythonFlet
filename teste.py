from flet import *
import flet as ft

def main(page: ft.Page):

    dados = Column()
    array_novos_dados = []
    array_intervalo = []
    array_VF = []

    def coluna_print():
        for i in range(len(array_novos_dados)):
            print(f'{array_novos_dados[i].value},{array_intervalo[i].value},{array_VF[i].value},')


    def adicionar_linha():
        array_novos_dados.append(TextField())
        array_intervalo.append(TextField())
        array_VF.append(Checkbox())
        dados.controls.append(Row([Container(array_novos_dados[-1], expand=1, ),
        Container(array_intervalo[-1], expand=1, ),
        Container(array_VF[-1], padding=padding.only(right=10)), ], ),)
        page.update()

    def remover_linha():
        array_novos_dados.pop()
        array_intervalo.pop()
        array_VF.pop()
        dados.controls.pop()

        page.update()

    tab = Container(
        bgcolor=colors.AMBER,
        expand=1,
        padding=10,
        content=Column(
            [
                Row([Container(Text('Novos Dados', size=20, color=colors.BLACK), expand=1,), Container(Text('Intervalo', size=20, color=colors.BLACK), expand=1,), Container(Text('V/F', size=20, color=colors.BLACK), padding=padding.only(right=10)),],),
                dados,
                Row([Container(expand=1), IconButton(icon=icons.ADD_CIRCLE_OUTLINE_ROUNDED, icon_color=colors.BLACK, icon_size=40, on_click=lambda e: adicionar_linha(), ), IconButton(icon=icons.REMOVE_CIRCLE_OUTLINE_ROUNDED, icon_color=colors.BLACK, icon_size=40, on_click=lambda e: remover_linha()), Container(expand=1),
                 IconButton(icon=icons.PLUS_ONE, icon_color=colors.BLACK, icon_size=40, on_click=lambda e: coluna_print()), Container(expand=1),])

            ],
            expand=1,
            scroll=ft.ScrollMode.ALWAYS,
            auto_scroll=True,
        )
    )

    page.add(tab)

ft.app(main)