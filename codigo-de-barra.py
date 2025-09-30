from barcode import EAN13
from barcode.writer import ImageWriter #lib para mudar a extensão do cod barras
import os

def gerar_cod_barras():
    """
    Gera um código de barras EAN-13 a partir de uma entrada do usuário.
    """
    while True:
        dados_usuario = input("Por favor, digite 12 dígitos para gerar o código de barras: ")
        dados_usuario = dados_usuario.replace(" ", "")

        if dados_usuario.isdigit() and len(dados_usuario) == 12:
            try:
                codigo_barras = EAN13(dados_usuario, writer=ImageWriter())
                nome_arquivo = f"barcode_{dados_usuario}"

                codigo_barras.save(nome_arquivo)

                print(f"""
                      \nCódigo de barras gerado com sucesso!
                      O arquivo '{nome_arquivo}.png' foi salvo no mesmo diretório.
                      Você pode encontrar a imagem neste caminho: 
                """)
                print(os.path.abspath(nome_arquivo + '.png'))
                break
            except Exception as e:
                print(f"Ocorreu um erro ao gerar o código de barras: {e}")
                print("Por favor, tente novamente com uma entrada válida.")
        else:
            print("Entrada inválida. Um código EAN-13 deve ter exatamente 12 dígitos numéricos.")

if __name__ == "__main__":
    gerar_cod_barras()



