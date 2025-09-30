import qrcode
import os # Lib para interagir com o sistema operacional

dados_usuario = input("Digite o texto ou URL que deseja gerar o QR Code: ")

if dados_usuario:
    qr = qrcode.QRCode(
    version=1, # Controla o tamanho do QR Code. 1 é o menor.
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Nível de correção de erros. H é o mais alto. L é mais baixo
    box_size=10,
    border=4,
    )

    qr.add_data(dados_usuario)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")

    nome_arquivo = "qrcode.png"

    img.save(nome_arquivo)

    print(f"""
        \nQR Code gerado com sucesso!
        \nO arquivo '{nome_arquivo}' foi salvo com sucesso, e poderá ser acesso neste caminho: 
        """)
    print(os.path.abspath(nome_arquivo))

else:
    print("A entrada não pode ser vazia. Por favor, tente novamente.")







