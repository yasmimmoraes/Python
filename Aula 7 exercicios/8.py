#Escreva um programa que leia um valor em metros e o exiba 
#convertido em centímetros e milímetros.
valor = float(input("Digite o valor em metros: "))
cent = valor * 100
mili = valor * 1000
print(f"O valor em centimetros será de {cent:.0f}cm, e o valor em milietros será de {mili:.0f}mm")