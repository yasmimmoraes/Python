# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#  de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
num = float(input('Comprimento do cateto oposto:'))
num2 = float(input('Comprimento do cateto adjacente:'))
hipo = hypot(num, num2)
print(f'A hipotenusa vai medir {hipo:.2f}')

# ou

# num = float(input('Comprimento do cateto oposto:'))
# num2 = float(input('Comprimento do cateto adjacente:'))
# hipo = (num ** 2 + num2 ** 2) ** (1/2)
# print(f'A hipotenusa vai medir {hipo:.2f}')