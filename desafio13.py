#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Insira o valor do seu salário atual: R$ '))
novo_salario  = (salario * 15 / 100) + salario
print(f'O valor do seu salário atualizado com o aumento de 15% é: R$ {novo_salario:.2f}')