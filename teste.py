from flet import *
import pandas as pd
import os.path
import classes

def main(page: Page):


    def cabecalho_tabela(texto_nome, texto_arquivo, botao):
        # Cabeçalho da tabela (Nome e file picker)
        return Container(
            content=Row(
                [Container(expand=1, padding=padding.only(left=10),
                           content=Row([texto_nome, texto_arquivo])),
                 Container(content=botao)]
            )
        )

    def container_tabela(arquivo_tabela):
        # Container onde mostra os dados da tabela.
        coluna_principal = Column(scroll=ScrollMode.ALWAYS,)

        for index, row in arquivo_tabela.iterrows():
            linha = []
            for coluna in arquivo_tabela.columns:
                valor = row[coluna]
                linha.append(valor)
            celulas = Row()
            for i in range(len(linha)):
                celulas.controls.append(Container(content=Text(linha[i]), width=150, padding=padding.only(bottom=15, top=15), alignment=alignment.center, border=border.only(right=BorderSide(2, color=colors.BLACK))))
            coluna_principal.controls.append(Container(content=celulas, border=border.only(bottom=BorderSide(2, color=colors.BLACK))))

        # Array feito para colocar o scroll horizontal.
        a=[]
        a.append(coluna_principal)

        page.update()
        return Container(
            bgcolor=colors.BLACK26,
            border=border.only(top=BorderSide(2, color=colors.BLACK)),
            expand=1,
            content=Row(controls=a, scroll=ScrollMode.ALWAYS)
        )

    texto_arquivo_nome = Text(value='Nome:')
    texto_arquivo_caminho = Text(value='Arquivo:')
    texto_dados_df = Text(value='Dados:')
    botao_file_picker = classes.BotaoFilePicker(page, return_nome=texto_arquivo_nome, return_arquivo=texto_arquivo_caminho,hover_color=colors.with_opacity(opacity=0.4, color=colors.GREY_50))

    coluna_tabelas = Container(
        bgcolor=colors.BLUE_300,
        expand=2,
        content=Column([cabecalho_tabela(texto_arquivo_nome, texto_arquivo_caminho, botao_file_picker.botao), container_tabela(botao_file_picker.dados_df),])
    )

    page.add(coluna_tabelas)


app(main)