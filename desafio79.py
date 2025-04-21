'''
Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valores = []
con = 'S'
while con == 'S':
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print(f'Valor adicionado...')
    else:
        print(f'Valor duplicado! Não será adicionado...')
    while True:
        con = str(input('Quer continuar? [S/N] ')).upper().strip()
        if con in ['S', 'N']:
            break
        print('Apenas S ou N!')
valores.sort()
print(f'Os valores digitados foram: {valores}')


#Solução alternativa
'''
valores = []
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado...')
    else:
        print('Valor duplicado! Não será adicionado...')
    
    # Perguntar se deseja continuar
    con = input('Quer continuar? [S/N] ').strip().upper()
    while con not in ['S', 'N']:
        con = input('Apenas S ou N! Quer continuar? [S/N] ').strip().upper()
    
    if con == 'N':
        break

valores.sort()
print(f'Os valores digitados foram: {valores}')
'''