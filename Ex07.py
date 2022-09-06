p1 = float(input('Produto 1:R$ '))

p2 = float(input('Produto 2:R$ '))

p3 = float(input('Produto 3:R$ '))

p4 = float(input('Produto 4:R$ '))

p5 = float(input('Produto 5:R$ '))

pg = float(input('Pagamento:R$ '))

T = pg - (p1 + p2 + p3 + p4 + p5)

print('Troco:R$ %.2f' % T)

