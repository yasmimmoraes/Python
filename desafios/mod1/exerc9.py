# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento
sal = float(input("Qual o valor do salário do funcionário? R$"))
sal2 = sal * 15 / 100
print(f"O salário que era de {sal} agora passa a ser {sal + sal2}")