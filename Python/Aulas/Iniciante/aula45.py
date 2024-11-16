'''
Interpolaração basica de strings
s - strings
d - int
f - float
.<numero de digitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
Conversion flags - !r !s !a
'''
valor = 'Suii'
print(f'{valor}')
print(f'{valor: <10}')
print(f'{valor: >10}')
print(f'{valor: ^10}')
print(f'{1000.9897835:.3f}')
