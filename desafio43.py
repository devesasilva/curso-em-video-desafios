'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 a 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: obesidade
- Acima de 40: Obesidade mórbida
'''
print('-=' * 10)
print('    Cálculo IMC')
print('-=' * 10)
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / altura**2
if imc < 18.5:
    print(f'O seu IMC é de {imc:.1f}, você está ABAIXO DO PESO.')
elif imc <= 25:
    print(f'O seu IMC é de {imc:.1f}, você está no PESO IDEAL')
elif imc <= 30:
    print(f'O seu IMC é de {imc:.1f}, você está com SOBREPESO')
elif imc <= 40:
    print(f'O seu IMC é de {imc:.1f}, você está com OBESIDADE')
else:
    print(f'O seu IMC é de {imc:.1f}, você está com OBESIDADE MÓRBIDA')

    