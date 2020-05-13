def converteBinToDec (numero=111):
    original = numero
    mult = 1
    decimal = 0
    while numero > 0:
        decimal = decimal + numero % 10 * mult
        mult = mult * 2
        numero = numero / 2
    print(f"Binario: {original} e o decinal é {numero}")

converteBinToDec()