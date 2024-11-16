# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
pessoa = {
    'nome': 'Davi',
    'sobrenome': 'Balieiro',
    'idade': 17,
    'altura': 1.9,
    'endereços': [
         {'rua': 'suiiiii', 'número': 570},
         {'rua': 'outra rua', 'número': 989},
    ]
}

# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])
