from decimal import Decimal

def converteBinToDec (numero:int):
    original = int(numero)
    mult = 1
    dec = 0
    while numero > 0:
        dec = dec + Decimal(numero % 10) * mult
        mult = mult * 2
        numero = int(numero / 2)
    print(f"Binario: {original} e o decinal é {dec}")

converteBinToDec(111)