'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
- A média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos.
'''
#variáveis para calcular a média de idade do grupo
somaidade = 0
médiaidade = 0
#Variáveis para verificar nome do homem mais velho
homem = 0
nomevelho = ''
#variável para verificar a quantidade de mulheres que possuem menos de 20 anos
mulheres = 0
#Laço de repetição que itera de 1 a 4 para receber as informações e fazer as condições para obter os resultados do enunciado.
for pess in range(1, 5):
    print(f'-----{pess}ª PESSOA-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade
    #Condição para verificar qual o homem mais velho
    if pess == 1 and sexo in 'Mm': 
       homem = idade
       nomevelho = nome
    if sexo in 'Mm' and idade > homem:
       homem = idade
       nomevelho = nome
    #Condição para verificar mulheres menores de 20 anos
    if sexo in 'Ff' and idade <= 20 :
      mulheres += 1
médiaidade = somaidade / 4

print(f'A média de idade do grupo é igual a: {médiaidade}')
print(f'O homem mais velho se chama {nomevelho} e possui {homem} anos.')
print(f'{mulheres} mulheres possuem menos de 20 anos')  