'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e o valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
numeros = []
pares = []
impares = []
con = 'S'
while con == 'S':
    numeros.append(int(input('Insira um número: ')))
    while True:
        con = str(input('Quer continuar? [S/N] ')).upper().strip()
        if con in ['S', 'N']:
            break
        print('Tente novamente, apenas S ou N!')
print('=' * 20)
print(f'Você adicionou os números: {numeros}')
for p in numeros:
    if p % 2 == 0:
       pares.append(p)
    else:
        impares.append(p)
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
