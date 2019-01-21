carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dolares = (carteira / 3.76)
print('Com R${} você pode comprar US${:.2f}'.format(carteira, dolares))
