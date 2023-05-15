# Crie um programa que leia quanto dinheiro uma pessoa 
# tem na carteira e mostre quantos dólares ela pode comprar.
dim = float(input("Digite quanto reais você possui: "))
conversao = dim / 4.95
print(f"Você possui {dim:.2f} e pode comprar {conversao:.2f} dólares")