from flet import *
import pandas as pd


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
                        scroll=ScrollMode.ALWAYS,

                    ),
                ],
                expand=1,
            )
        )
        return tab

class BotaoFilePicker:

    def __init__(self, page, return_nome=None, return_arquivo=None, return_dados=None, icon_color=colors.BLACK, bgcolor=colors.TRANSPARENT, hover_color=colors.GREY_300):
        self.page = page
        self.return_nome = return_nome
        self.return_arquivo = return_arquivo
        self.return_dados = return_dados
        self.arquivo_nome = 'Arquivo não selecionado'
        self.dados_df = pd.read_excel('arquivos/excel_teste2.xlsx', header=None)
        self.arquivo_caminho = 'Arquivo não selecionado'
        self.botao = IconButton(
            icon_color=icon_color,
            hover_color=hover_color,
            bgcolor=bgcolor,
            icon=icons.FILE_PRESENT_SHARP,
            on_click=lambda _: self.pick_files_dialog.pick_files(
                allowed_extensions=["xlsx", "xls"],  # Permite apenas arquivos Excel
                allow_multiple=False  # Permite selecionar apenas um arquivo
            )
        )
        self.pick_files_dialog = FilePicker(on_result=self.pick_files_result)
        self.page.overlay.append(self.pick_files_dialog)

    def pick_files_result(self, e: FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path  # Pega o caminho arquivo selecionado
            self.dados_df = pd.read_excel(file_path, header=None)  # Carrega o arquivo Excel em um DataFrame
            self.arquivo_nome = f"{e.files[0].name}"
            self.arquivo_caminho = f'{e.files[0].path}'
            # Caso queira verificar os dados.
            # print(self.dados_df)
            # print(self.arquivo_nome)
            # print(self.arquivo_caminho)

        if self.return_nome != None:
            self.return_nome.value = str(f'Nome: {self.arquivo_nome}')

        if self.return_arquivo != None:
            self.return_arquivo.value = str(f'Arquivo: {self.arquivo_caminho}')

        if self.return_dados != None:
            try:
                self.page.remove_at(1)
            except:
                print('class BotaoFilePicker.pick_files_result: self.return_dados inexistente.')
            try:
                self.page.add(self.return_dados(arquivo_tabela=f'{self.arquivo_caminho}', return_TF=True))
            except:
                print(f'class BotaoFilePicker.pick_files_result: {self.arquivo_caminho}')

        self.page.update()


