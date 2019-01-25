km = int(input('Digite a quantidade de km percorridos por um carro: '))
dias = int(input('Digite a quantidade de dias pelos quais ele foi alugado: '))
custo = (dias * 60) + (km * 0.15)
print('Preço a pagar pelo veículo é {} R$'.format(custo))

