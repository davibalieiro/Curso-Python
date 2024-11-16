# Aula de lista
'''
Lista em Python
Tipo list - Mutável
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indice e fatiamento
Metodos uteis: 
    append, insert, pop, del, celar, extend, +
    Create Read Update Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista = [1, 2, 3, 4]

lista[2] = 30

del lista[1]

print(lista)
print(lista[2])

lista.append(5)  # append() = ele adiciona um item ao final da lista
lista.pop()  # pop() = ele retira o ultimo item da minha lista
lista.append(6)
lista.append(7)
lista.pop()
print(lista)
