# List comprehension em Python
# List comprehension - é uma forma rapida para criar lista a partir de iteraveis

import pprint


def p(v):
    pprint.pp(v, sort_dicts=False, width=40)


# print(list(range(10)))
# lista = []
# for n in range(10):

#    lista.append(n)

# print(lista)

# lista = [n for n in range(10)]
# print(lista)

# posso fazer com duas linhas kkkkkkk
# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'price': 20, },
    {'nome': 'p2', 'price': 10, },
    {'nome': 'p3', 'price': 30, },
]

# novo_produto = [
#    {**produto, 'price': produto['price']*1.05}
#    if produto['price'] > 20 else {**produto}
#    for produto in produtos
# ]

# print(*novo_produto, sep='\n')
# p(novo_produto)

lista = [n for n in range(10) if n < 5]
print(lista)

novo_produto = [
    {**produto, 'price': produto['price']*1.05}
    if produto['price'] > 20 else {**produto}
    for produto in produtos
    if (produto['price']*1.05) > 10
]
