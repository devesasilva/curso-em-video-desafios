'''
O mesmo professor do desafio anterior  quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
dos quatro alunos e mostre a ordem sorteada.
'''
import random #chamei o módulo

#pedi para os usuários o nome dos grupos
aluno1 = str(input('Insira o nome do grupo: '))
aluno2 = str(input('Insira o nome do grupo: '))
aluno3 = str(input('Insira o nome do grupo: '))
aluno4 = str(input('Insira o nome do grupo: '))

#criei uma lista com os nomes inseridos pelos usuários e usei shuffle do módulo random para embaralhar as variáveis
lista = [aluno1, aluno2, aluno3, aluno4] 
random.shuffle(lista)

#ordem definida
print(f'A ordem para as apresentações é a seguinte:  {lista}')