"""
Escreva um script que leia a data atual e mostre a quantidade de dias decorridos
"""

import time

#horas = time.time() / 3600
#print(f"Horas decorridas  {horas} ")
#print(f"Dias decorridos  {horas/24} ")
#print(f"Anos decorridos  {(horas/24)/365} ")

data = str(input("Informe a data atual no formato dd/MM/yyyy: "))
# print(data[6::])
ano = int(data[6::])
mes = (int(data[3::5]) + ano/12)
print(f"Quantidade de meses: {mes}")
dia = (int(data[0:2]) + mes * 30.4167)
print(f"ano lido: {ano}")
print(f"Quantidade de dias corridos: {dia}")