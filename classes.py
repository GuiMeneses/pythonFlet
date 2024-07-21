from flet import *
import flet as ft

class TabelaDados:
    # Cria uma tabela de dados, 2 colunas com TextField() e uma com um Checkbox(), caso o Checkbox for verdadeiro o código interpretará a primeira coluna(coluna_novos_dados) como referências de célula, assim ela pegara os valores dessa celula da primeira planilha e passará para a segunda planilha na referências de célula que o usuário inseriu na segunda coluna.
    def __init__(self, page, coluna_principal, coluna_novos_dados, coluna_intervalos, coluna_VF):
        self.page = page
        self.coluna_principal = coluna_principal
        self.coluna_novos_dados = coluna_novos_dados
        self.coluna_intervalos = coluna_intervalos
        self.coluna_VF = coluna_VF

    def print_coluna_principal(self):
        # Funçao caso queria verificar os dados.
        print('  ----##----  \n')
        for i in range(len(self.coluna_novos_dados)):
            print(f'{self.coluna_novos_dados[i].value},{self.coluna_intervalos[i].value},{self.coluna_VF[i].value},')


    def adicionar_linha(self):
        # Adiciona linhas da colina principal, primeiro adiciona os objetos(TextField(),TextField(),Checkbox()) em seus respectivos arrays e os divide em containers.
        self.coluna_novos_dados.append(TextField())
        self.coluna_intervalos.append(TextField())
        self.coluna_VF.append(Checkbox(check_color=colors.BLACK, hover_color=colors.WHITE24, fill_color=colors.WHITE24, border_side=BorderSide(1, color=colors.BLACK)))
        self.coluna_principal.controls.append(Row([
        Container(self.coluna_novos_dados[-1], expand=1, ),
        Container(self.coluna_intervalos[-1], expand=1, ),
        Container(self.coluna_VF[-1], padding=padding.only(right=10)),
        ], ),)
        self.page.update()

    def remover_linha(self):
        # Remove linhas da colina principal, primeiro remove os objetos(TextField(),TextField(),Checkbox()) de seus respectivos arrays e por fim remove a linha junto com os containers da coluna principal.
        if len(self.coluna_novos_dados) > 0:
            self.coluna_novos_dados.pop()
            self.coluna_intervalos.pop()
            self.coluna_VF.pop()
            self.coluna_principal.controls.pop()
            self.page.update()

    def tabela(self):
        # Retorna a tabela pronta.
        tab = Container(
            bgcolor=colors.AMBER,
            expand=2,
            padding=10,
            border_radius=30,
            content=Column(
                [
                    Row([Container(Text('Novos Dados', size=20, color=colors.BLACK), expand=1, ),
                         Container(Text('Intervalo', size=20, color=colors.BLACK), expand=1, ),
                         Container(Text('V/F', size=20, color=colors.BLACK), padding=padding.only(right=10)), ], ),

                    Column([
                        self.coluna_principal,

                        Row([Container(expand=1),
                             IconButton(icon=icons.ADD_CIRCLE_OUTLINE_ROUNDED, icon_color=colors.BLACK, icon_size=40,
                                        on_click=lambda e: self.adicionar_linha(), ),
                             IconButton(icon=icons.REMOVE_CIRCLE_OUTLINE_ROUNDED, icon_color=colors.BLACK, icon_size=40,
                                        on_click=lambda e: self.remover_linha()), Container(expand=1),
                             # Para caso queira testar se os valores estão corretos
                             # IconButton(icon=icons.PLUS_ONE, icon_color=colors.BLACK, icon_size=40,
                             #            on_click=lambda e: self.print_coluna_principal()), Container(expand=1),
                             ])
                    ],
                        expand=1,
                        scroll=ft.ScrollMode.ALWAYS,

                    ),
                ],
                expand=1,
            )
        )
        return tab