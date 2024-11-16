'''
Iterável = str, range ,etc (__iter__)
Iterador = quem sabe entregar um valor de cada vez
next = me entrague o proximo valor
iter = me entrague seu iterador
'''
'''
nome = 'Davi'.__iter__()
nome = iter('Davi')
print(next(nome))
print(nome.__next__())
'''
# Tudo isso é o que o FOR faz por "debaixo dos panos"
'''
nome = 'Davi'
iterator = iter(nome)

while True:

    try:
        print(next(iterator))

    except StopIteration:
        break
'''

# TUDO ISSO É IGUAL A = ISSO:
nome = 'Davi'
for letra in nome:
    print(letra)
