#Menu de Opções
'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
print('-=' * 10 )
print('       PAINÉL')
print('-=' * 10)
from time import sleep
#Lê dois valores inteiros
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))

#Atribui o valor 0 para opção
opção = 0 

#Enquanto opção tiver um valor diferente de 0, o usuário atribui um novo valor a opção que fará algo de acordo com as condições.
while opção != 5:
    print('Selecione a opção que deseja: ')
    opção = int(input('[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do programa\n '))
    if opção == 1:
        print(f'A soma entre {v1} e {v2} é: {v1 + v2}')
    elif opção == 2:
        print(f"A multiplicação entre {v1} e {v2} é: {v1 * v2}")
    elif opção == 3:
        if v1 > v2:
            print(f"O maior número entre {v1} e {v2} é: {v1}")
        elif v2 > v1:
            print(f"O maior número entre {v1} e {v2} é: {v2}")
    elif opção == 4:
        print('Informe os valores novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print(f'A opção informada é inválida! Tente novamente.')
    print('-=' * 10)
    sleep(2)
print('Fim do programa.')

