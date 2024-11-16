'''
Flag (Bandeira) - Marcal um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
'''
condicao = True
passou = None
if condicao:
    passou = True
    print('algo')
else:
    print('algo nao')

if passou is None:
    print('Nao passou no if')

# if passou is not None:
else:
    print('Passou no if')
