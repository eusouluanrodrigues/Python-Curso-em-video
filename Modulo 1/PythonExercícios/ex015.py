dias = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Informe a quantidade de Km percorridos: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

