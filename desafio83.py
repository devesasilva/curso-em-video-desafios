'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expr = str(input('Digite a sua expressão: '))
pilha = []
for sim in expr:
    if sim == '(':
        pilha.append('(')
        print(pilha)
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
            print(pilha)
        else:
            pilha.append(')')
            print(pilha)
            break
if len(pilha) == 0:
    print(pilha)
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')
#Toda string é uma lista


'''
expr = str(input('Digite a sua expressão: '))
if expr.count('(') == expr.count(')'):
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
'''