#Aluguel de carros
km = float(input('Qual a quantidade de quilômetros percorridos? '))
dias = int(input('Qual a quantidade de dias que ficou com o carro? '))

totalkm = km * 0.15
totaldias = dias * 60
print(f'O valor a ser pago pelos quilômetros é: R$ {totalkm} e pelos dias é: {totaldias}. E o total a pagar é: R$ {totalkm + totaldias}')