from barcode import EAN13
from barcode.writer import ImageWriter

codigos_produtos = {
    "Feijão" : "123456789123",
    "Arroz" : "789456123789",
    "Macarrão" : "456789123456",
    "Azeite" : "159951159951"
}

for produto in codigos_produtos:
    codigo = codigos_produtos[produto]
    codigo_barra = EAN13(codigo, writer=ImageWriter())
    codigo_barra.save(f"codigo_barra_{produto}")