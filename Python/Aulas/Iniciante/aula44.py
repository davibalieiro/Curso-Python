'''
Interpolaração basica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''
nome = 'Davi'
preco = 100.89769
valores = '%s, o preço é R$%.2f' % (nome, preco)
print(valores)
print('O hexadecimal de %d é %x' % (15, 15))
