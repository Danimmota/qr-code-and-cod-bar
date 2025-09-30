import pandas as pd
from barcode import EAN13
from barcode.writer import ImageWriter
from pathlib import Path


def gerar_codigos_excel(nome_arquivo_excel: str, coluna_dados: str = 'codigo_ean'):
    pasta_saida = Path("codigos_gerados_excel")
    pasta_saida.mkdir(exist_ok=True)


    try:
        # Lê o Excel como string para não perder zeros à esquerda
        df = pd.read_excel(nome_arquivo_excel, dtype=str)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_excel}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return

    if coluna_dados not in df.columns:
        print(f"Erro: A coluna '{coluna_dados}' não foi encontrada no arquivo Excel.")
        return

    for index, codigo in enumerate(df[coluna_dados], start=1):
        codigo = str(codigo).strip() if pd.notna(codigo) else ""

        if not (codigo.isdigit() and 12 <= len(codigo) <= 13):
            print(f"⚠️  Linha {index}: código inválido ({codigo}). Ignorando.")
            continue

        try:
            codigo_base = codigo[:12]  # EAN13 usa só os 12 primeiros dígitos
            caminho = pasta_saida / f"barcode_{codigo_base}"

            EAN13(codigo_base, writer=ImageWriter()).save(str(caminho))
            print(f"Linha {index}: Código {codigo_base} gerado com sucesso!")

        except Exception as e:
            print(f"Erro ao processar a linha {index + 1}: {e}")


if __name__ == "__main__":
    gerar_codigos_excel("codigos.xlsx")
