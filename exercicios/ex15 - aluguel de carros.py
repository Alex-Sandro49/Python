#Calcula o aluguel de um carro (R$60/dia e R$0.15/km).

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pagar = 60 * d + km * 0.15
print(f'O total a pagar é de R${pagar:.2f}')
