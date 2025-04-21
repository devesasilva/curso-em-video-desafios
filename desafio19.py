'''
19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
aluno1 = str(input('Insira o nome do primeiro aluno: '))
aluno2 = str(input('Insira o nome do segundo aluno: '))
aluno3 = str(input('Insira o nome do terceiro aluno: '))
aluno4 = str(input('Insira o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido =  random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')