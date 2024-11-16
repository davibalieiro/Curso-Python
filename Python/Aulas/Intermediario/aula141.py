# Dicionary Comprehension e Set Comprehension

product = {
    'name': 'Davi',
    'price': 2.5,
    'Categoria': 'Escritorio',

}

for chave, value in product.items():
    print(chave, value)

dicionario = {
    chave: value.upper()
    if isinstance(value, str) else value
    for chave, value
    in product.items()
    if chave != 'Categoria'

}
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
dc = {
    chave: value
    for chave, value in lista
}

# ou da pra fazer assim
# print(dict(lista))

print(dicionario)


# s1 = {i for i in range(10)}
print(set(range(10)))
