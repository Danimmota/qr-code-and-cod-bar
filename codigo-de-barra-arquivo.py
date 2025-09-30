import pandas as pd
from barcode import EAN13
from barcode.writer import ImageWriter
import os


def gerar_codigos_arquivo(nome_arquivo_csv, coluna_dados='codigo_ean'):

    pasta_saida = "codigos_gerados"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    try:
        df = pd.read_csv(nome_arquivo_csv) #caso seja um arquivo Excel é pd.read_excel
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_csv}' não foi encontrado.")
        return

    # Itera sobre o arquivo
    for index, row in df.iterrows():
        try:
            dados_codigo = str(row[coluna_dados]).strip()

            # Validacao se os dados sao numeros e possuem 12 digitos
            if dados_codigo.isdigit() and len(dados_codigo) == 12:
                codigo_barras = EAN13(dados_codigo, writer=ImageWriter())

                caminho_arquivo = os.path.join(pasta_saida, f"barcode_{dados_codigo}")

                codigo_barras.save(caminho_arquivo)
                print(f"Código de barras para {dados_codigo} gerado com sucesso!")
            else:
                print(f"Aviso: Linha {index + 1} com dados inválidos ({dados_codigo}). Ignorando.")
        except Exception as e:
            print(f"Erro ao processar a linha {index + 1} ({dados_codigo}): {e}")


if __name__ == "__main__":
    gerar_codigos_arquivo("codigos.csv")
