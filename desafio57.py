#Validação de Dados
'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0] #Esse zero só pega a primeira letra do que foi inserido.
while sexo not in 'MmFf':
    sexo = str(input('Inválido! Insira novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')