# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na 
# tela o nome do escolhido.
from random import choice
al = input("Primeiro aluno: ")
al2 = input("Segundo aluno: ")
al3 = input("Terceiro aluno: ")
al4 = input("Quarto aluno: ")
lista = [al, al2, al3, al4]
escolhido = choice(lista)
print(f"O aluno escolhido foi {escolhido}")