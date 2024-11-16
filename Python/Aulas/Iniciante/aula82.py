# Aula de lista
'''
Lista em Python
Tipo list - Mutável
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indice e fatiamento
Metodos uteis: 
    append = Adiciona um item no final
    insert = Adiciona um item no indice escolhido
    pop = Remove do final ou do indicie escolhido
    del = apaga um indice
    celar = limpa lista
    extend = espende a lista
    + = concatena listas

Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

# ISSO É AULA 82
'''
lista = ['Suiiii', 10, 20, 30, 40]
lista.append('Cristiano')
nome = lista.pop()
lista.append('Ronaldo')
del lista[-1]
lista.insert(0, 'Davi')

# lista.clear()
print(lista, nome)
'''

# AULA 83

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)


print(lista_c)
print(lista_a)
