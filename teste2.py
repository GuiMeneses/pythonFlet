import pandas as pd


# Função para percorrer todas as células de uma tabela Excel
def percorrer_celulas(caminho_arquivo):
    # Leitura do arquivo Excel em um DataFrame
    df = pd.read_excel(caminho_arquivo, engine='openpyxl', header=None)

    # Iterar sobre todas as células do DataFrame
    for index, row in df.iterrows():
        for coluna in df.columns:
            valor = row[coluna]
            print(f"Célula ({index}, {coluna}): {valor}")


# Caminho do arquivo Excel
caminho_arquivo = 'arquivos/excel_teste.xlsx'

# Chamada da função para percorrer todas as células e imprimir seus valores
percorrer_celulas(caminho_arquivo)
