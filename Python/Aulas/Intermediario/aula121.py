# Metodos uteis dos dicionarios em Python
'''
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com o valores
items - iteravel com o valores e as chaves
setdefaut - adiciona valor se a chave nao existe
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chaves especifica (del)
popitem - Apaga o ultimo item adicionado
update - Atualiza um dicionario com o outro

'''

import copy
# import copy - isso é uma copy profunda ou seja um dicionario nao vai afetar o outro, provavel que vou utilizar muito em lista
# .copy - é uma copy mais rasa so o basico

pessoa = {
    'nome': 'Davi',
    'sobrenome': 'Balieiro',
    'idade': 900,
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])

# print(pessoa.__len__()) mesma coisa que isso
print(len(pessoa))

print(list(pessoa.keys()))

print(list(pessoa.values()))

print(list(pessoa.items()))


for chaves in pessoa.values():
    print(chaves)


for chaves, valor in pessoa.items():
    print(chaves, valor)

# .update - é para atualizar uma lista ou adicionar algo nela mesma
'''
pessoa.update({
    'nome': 'Cr7',
})
'''

pessoa.update(nome='Junior,', idade=90)
print(pessoa)
