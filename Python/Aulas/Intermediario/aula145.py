import sys

# Generator expression, Iterable e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterador = iterable.__iter__()  # tem__iter__e__next__
print(next(iterador))

# O Iterador não sabe nada, ele so sabe te entregar o proximo valor

lista = [n for n in range(1000000)]
gerenator = (n for n in range(1000000))
print(sys.getsizeof(lista))
print(sys.getsizeof(gerenator))

for n in gerenator:
    print(n)
