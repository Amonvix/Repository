n1 = float(input('Sobre qual valor vamos descontar 5%? R$'))
per = (n1 * 0.05)
des = (n1 - per)
print('O valor de desconto será de R${:.2f}'.format(per))
print('O total de sua compra será de R$ {:.2f} à vista'.format(des))
