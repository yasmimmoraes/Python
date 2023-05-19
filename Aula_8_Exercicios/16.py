# Crie um programa que leia um número Real qualquer pelo
#  teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input("Digite um número real qualquer "))
print(f"O número real em inteiro ficará {trunc(num)}")

# ou (tbm está certo e n precisa importa nenhuma biblioteca)

# from math import trunc
# num = float(input("Digite um número real qualquer "))
# print(f"O número real em inteiro ficará {int(num)}")

