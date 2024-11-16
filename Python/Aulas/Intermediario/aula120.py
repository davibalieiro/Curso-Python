# Manipulado chaves e valores em dicionarios

pessoa = {}


chave = 'nome'
pessoa[chave] = 'Davi Balieiro'
pessoa['sobrenome'] = 'Costa'

del pessoa['sobrenome']

print(pessoa)

print(pessoa['nome'])

if pessoa.get('sobrenome', None):  # .get() - tenta obter uma chave, padrao None
    print('existe')
